# Giảm trùng lặp mã là một trong những ý tưởng cốt lõi của FastAPI.
# Vì việc trùng lặp mã sẽ làm tăng nguy cơ xảy ra lỗi, sự cố bảo mật,
# sự cố không đồng bộ hóa mã(desynchronization) (khi bạn cập nhật ở một nơi nhưng không cập nhật ở nơi khác), v.v.

# Chúng ta có thể khai báo một mô hình "UserBase" làm cơ sở cho các mô hình khác của chúng ta.
# Và sau đó chúng ta có thể tạo các lớp con của mô hình đó kế thừa các thuộc tính của nó (khai báo kiểu, xác thực, v.v.).
#Bằng cách đó, chúng ta có thể khai báo sự khác biệt giữa các mô hình (với mật khẩu văn bản gốc, với hashed_password và không có mật khẩu):

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved