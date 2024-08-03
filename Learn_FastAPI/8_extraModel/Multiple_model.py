# Đây là ý tưởng chung về cách các mô hình có thể trông như thế nào 
# với các trường mật khẩu của chúng và những nơi chúng được sử dụng:

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str | None = None


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

# Trong Pydantic v1, phương thức này được gọi là .dict(), nó không được dùng nữa (nhưng vẫn được hỗ trợ) trong Pydantic v2 và được đổi tên thành .model_dump().
# Các ví dụ ở đây sử dụng ".dict()" để tương thích với Pydantic v1, nhưng bạn nên sử dụng ".model_dump()" thay thế nếu bạn có thể sử dụng Pydantic v2.

#1. Unwrapping a dict
# Nếu chúng ta lấy một lệnh như user_dict và chuyển nó đến một hàm (hoặc lớp) với **user_dict, Python sẽ "mở gói" nó. Nó sẽ chuyển trực tiếp các khóa và giá trị của user_dict dưới dạng đối số khóa-giá trị.
# Vì vậy, tiếp tục với user_dict ở trên, viết:
# UserInDB(**user_dict) với :
    #user_in = UserIn(username="john", password="secret", email="john.doe@example.com")
    #user_dict = user_in.dict()
# Result:
    # UserInDB(
    #     username = user_dict["username"],
    #     password = user_dict["password"],
    #     email = user_dict["email"],
    #     full_name = user_dict["full_name"],
    # )

#2. A Pydantic model from the contents of another
# user_dict = user_in.dict()      
# UserInDB(**user_dict)          =       UserInDB(**user_in.dict())

#3. Unwrapping a dict and extra keywords
# UserInDB(**user_in.dict(), hashed_password=hashed_password)
    # UserInDB(
    #     username = user_dict["username"],
    #     password = user_dict["password"],
    #     email = user_dict["email"],
    #     full_name = user_dict["full_name"],
    #     hashed_password = hashed_password,
    # )