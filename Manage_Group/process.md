*B1:* Setup FastAPI and Dependencies
- pip install fastapi uvicorn
- pip install sqlalchemy databases
-...


*B2:* Create the Basic Project Structure
- Tạo 1 đường dẫn cho Project
- Trong đường dẫn, tạo các file:
    + main.py           : Tệp chính để khởi chạy ứng dụng FastAPI.
    + model.py          : Định nghĩa các mô hình cơ sở dữ liệu bằng SQLAlchemy.
    + database.py       : Thiết lập kết nối với cơ sở dữ liệu.
    + schemas.py        : Xác định lược đồ dữ liệu bằng Pydantic để xác thực và giao tiếp.
    + crud.py           : Chứa các hàm CRUD để tương tác với cơ sở dữ liệu.
    + requirements.txt  : Danh sách các thư viện cần thiết cho dự án
    + utils
    + enums.py

*B3:* Setup the database connection in database.py
- NHIỆM VỤ:
    + Thiết lập kết nối với CSDL
    + Nó thường chứa cấu hình CSDL
    + Khởi tạo công cụ "engine" và phiên làm việc "sesion" với CSDL

- CODE cơ bản:

    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker

    SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()


*B4:* Xác định mô hình cơ sở dữ liệu của bạn in models.py 
- NHIỆM VỤ:
    + Chứa các mô hình dữ liệu (models) được định nghĩa bằng SQLAlchemy để tương tác với CSDL.
    + Mỗi mô hình thường biểu diễn một bảng trong CSDL.

-CODE cơ bản:

    from sqlalchemy import Column, Integer, String
    from .database import Base

    class User(Base):
        __tablename__ = "users"

        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        email = Column(String, unique=True, index=True)



*B5:* Tạo các mô hình Pydantic (lược đồ) sẽ được sử dụng để xác thực
     và phản hồi yêu cầu in schemas.py
- NHIỆM VỤ:
    + Chứa các lược đồ (schemas) Pydantic
    + Những lược đồ này xác định hình dạng dữ liệu mà API sẽ nhận vào hoặc trả về
    + Chúng đc dùng để xác thực dữ liệu

- CODE cơ bản:

    from pydantic import BaseModel

    class UserBase(BaseModel):
        name: str
        email: str

    class UserCreate(UserBase):
        password: str

    class User(UserBase):
        id: int

        class Config:
            orm_mode = True



*B6:* Implement CRUD Operations (Triển khai các hoạt động CRUD)
- NHIỆM VỤ:
    + Viết các hàm để thực hiện các thao tác CRUD từ CSDL (Create, Read, Update, Delete)
    + Đây là nơi tập trung các logic tương tác với CSDL qua models (mô hình)

- CODE cơ bản:

    from sqlalchemy.orm import Session
    from . import models, schemas

    def get_user(db: Session, user_id: int):
        return db.query(models.User).filter(models.User.id == user_id).first()

    def create_user(db: Session, user: schemas.UserCreate):
        db_user = models.User(name=user.name, email=user.email, hashed_password=user.password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


*B7:* Set Up FastAPI Routes
Trong main.py, tạo FastAPI instance và xác định các routes:

- NHIỆM VỤ: 
    + Là tệp chính của ứng dụng FastAPI
    + Chứa các tuyến (routes) và các middleware
    + Khởi tạo ứng dụng FastAPI

- CODE cơ bản:

    from fastapi import FastAPI
    from . import models, database, schemas, crud

    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"message": "Welcome to the FastAPI blog !"}


*B8:* Run the app:
- uvicorn main:app --reload

*B9:* Testing the FastAPI
- Bạn có thể kiểm tra API bằng công cụ như Postman hoặc trực tiếp thông qua tài liệu được tạo tự động mà FastAPI cung cấp
  tại http://127.0.0.1:8000/docs.

  
*B10:* Expanding the Application (Mở rộng ứng dụng)
    - To expand this application, consider adding:
    + User Authentication: Use FastAPI's OAuth2PasswordBearer for token-based authentication.
     +Comments: Create a Comment model linked to Blog.
    + Tags/Categories: Add models to organize blogs.
    + Admin Interface: Create routes for managing content.
    + This basic setup should give you a solid foundation for creating a FastAPI-based blog.


    - Để mở rộng ứng dụng này, hãy xem xét thêm:
    + Xác thực người dùng: Sử dụng OAuth2PasswordBearer của FastAPI để xác thực dựa trên mã thông báo.
    + Bình luận: Tạo mô hình Bình luận được liên kết với Blog.
    + Thẻ/Danh mục: Thêm mô hình để sắp xếp blog.
    + Giao diện quản trị: Tạo tuyến đường để quản lý nội dung.
    + Thiết lập cơ bản này sẽ cung cấp cho bạn nền tảng vững chắc để tạo blog dựa trên FastAPI.


**THÊM**

*1. File "utils.py" *
- Chứa các hàm tiện ích (Utility Functions)
+ File này có thể chứa các hàm tiện ích giúp thực hiện các tác vụ lặp đi lặp lại hoặc các phép toán phổ biến. 
+ Ví dụ:

    def generate_unique_id() -> str:
        import uuid
        return str(uuid.uuid4())

    def format_date(date: datetime) -> str:
        return date.strftime("%Y-%m-%d")


- Hàm Xử Lý Chuỗi và Dữ Liệu
+  Cắt chuỗi, thay đổi định dạng, hoặc xác thực dữ liệu...
+ Ví dụ:

    def sanitize_input(input_string: str) -> str:
        return input_string.strip().lower()


- Hàm Xác Thực và Mã Hóa
+ Nếu bạn cần thực hiện các phép mã hóa hoặc xác thực như hash mật khẩu, mã hóa dữ liệu, hoặc xác thực JWT, bạn có thể đặt các hàm này vào util.py.
+ Ví dụ:

    from passlib.context import CryptContext

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)


- Hàm Tương Tác với Cơ Sở Dữ Liệu
+ Chẳng hạn như xây dựng truy vấn, chuyển đổi dữ liệu, hoặc xử lý các thao tác dữ liệu chung.
+ Ví dụ:

    from sqlalchemy.orm import Session
    from .models import User

    def get_user_by_id(db: Session, user_id: int) -> User:
        return db.query(User).filter(User.id == user_id).first()


- Cấu Hình và Tùy Chỉnh
+ Các hàm để tải cấu hình, thiết lập cài đặt, hoặc xử lý các tùy chỉnh cụ thể.
+ Ví dụ:
 
    import os

    def load_config(filename: str) -> dict:
        with open(filename, 'r') as f:
            return json.load(f)


- Hàm Xử Lý Lỗi và Ghi Log
+ Ví dụ:

    import logging

    logger = logging.getLogger(__name__)

    def log_error(message: str):
        logger.error(message)


- Ví dụ cách sử dụng:
    # main.py

    from util import generate_unique_id, format_date, hash_password, verify_password

    @app.post("/register")
    async def register(user: UserCreate):
        user_id = generate_unique_id()
        hashed_password = hash_password(user.password)
        # Lưu người dùng với user_id và hashed_password vào cơ sở dữ liệu
        return {"user_id": user_id, "username": user.username}


*2. File "enums.py" *

- Định nhĩa các Enum:
+ Giúp mã nguồn dễ hiểu hơn và dễ bảo trì hơn bằng cách thay thế các giá trị hằng số bằng các tên ý nghĩa.
+ Ví dụ:

    from enum import Enum

    class Status(Enum):
        ACTIVE = "active"
        INACTIVE = "inactive"
        PENDING = "pending"

- Tăng Cường Tính Chính Xác và Dễ Đọc:
+ Ví dụ:

    def get_status_message(status: Status) -> str:
    if status == Status.ACTIVE:
        return "The item is active."
    elif status == Status.INACTIVE:
        return "The item is inactive."
    elif status == Status.PENDING:
        return "The item is pending."

- Hỗ Trợ Trong Các Mô Hình Dữ Liệu và API:
+ Ví dụ:

    from pydantic import BaseModel
    from enums import Status

    class Item(BaseModel):
        name: str
        status: Status

- Sử Dụng Trong Truy Vấn và Xử Lý Dữ Liệu:
+ Ví dụ:

    from sqlalchemy import Enum as SQLAlchemyEnum

    class Post(Base):
        __tablename__ = "posts"
        id = Column(Integer, primary_key=True)
        status = Column(SQLAlchemyEnum(Status), nullable=False, default=Status.PENDING)

- Ví dụ cách sử dụng:

    # main.py

    from enums import PostStatus, UserRole

    def get_post_status(post_id: int) -> str:
        # Giả sử chúng ta đã lấy trạng thái từ cơ sở dữ liệu
        status = PostStatus.PUBLISHED  # Ví dụ
        return f"The status of post {post_id} is {status.value}."

    def check_user_role(role: UserRole) -> str:
        if role == UserRole.ADMIN:
            return "You have administrator privileges."
        elif role == UserRole.USER:
            return "You have user privileges."
        elif role == UserRole.GUEST:
            return "You have guest privileges."
