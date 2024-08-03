from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str

# Tạo đối tượng pwd_context để thực hiện hash mật khẩu và xác thực mật khẩu
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Tạo đối tượng để thực hiện việc tách token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

# Xác thực mật khẩu ban đầu với mật khẩu đã hash
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Hash mật khẩu
def get_password_hash(password):
    return pwd_context.hash(password)

# Lấy user trong database
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

#====================== 1.1. Xác thực username và password
def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

#====================== 1.2. Tạo mã jwt
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()                                                             # thông tin cần mã hóa jwt
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta                              
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)                     # nếu thời gian hết hạn token không được cung cấp thì mặc đinh thời gian hết hạn là 15 phút
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)                # mã hóa jwt
    return encoded_jwt


# ====================== 2.1. Kiểm tra sự tồn tại của user (giải mã token) 
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):              # tách token
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])                 # token hợp lệ, chưa hết hạn thì giải mã token
        username: str = payload.get("sub")                                              # lấy username 
        if username is None:                                                           
            raise credentials_exception
        token_data = TokenData(username=username)                                       
    except InvalidTokenError:                                                           # Nếu code trong Try có lỗi về Token (hết hạn, token không hợp lệ) trả về lỗi
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)                        # tìm user trong database
    if user is None:
        raise credentials_exception
    return user


#====================== 2.2. Kiểm tra trạng thái hoạt động của user
async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


#============================= 1.Xác thực thông tin đăng nhập và trả về token
@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)       # xác thực username và password
    if not user:                                                                          # nếu không tìm được user thỏa mãn trả về lỗi
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)                 # Tạo time hết hạn token
    access_token = create_access_token(                                                   # Tạo token
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user

#============================= 2.Lấy dữ liệu của user
@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]