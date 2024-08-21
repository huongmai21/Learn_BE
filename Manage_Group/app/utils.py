from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Mã hóa và xác thực mật khẩu
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserCreate(BaseModel):
    username: str
    password: str

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

@app.post("/register")
async def register(user: UserCreate):
    hashed_password = hash_password(user.password)
    # Lưu người dùng với mật khẩu đã mã hóa vào cơ sở dữ liệu
    return {"username": user.username, "hashed_password": hashed_password}

@app.post("/login")
async def login(user: UserCreate):
    # Truy xuất mật khẩu đã mã hóa từ cơ sở dữ liệu
    # giả sử hashed_password từ cơ sở dữ liệu
    hashed_password = ...  
    if verify_password(user.password, hashed_password):
        return {"message": "Login successful !"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
