from sqlalchemy import create_engine    # đc sd để thiết ập kết nối với CSDL
from sqlalchemy.ext.declarative import declarative_base     # tạo ra 1 lớp cơ sở mà từ đó tất cả các mô hình ORM sẽ kế thừa
from sqlalchemy.orm import sessionmaker     # đc sd để tạo các phiên làm việc với CSDL 


DATABASE_URL = "mysql+mysqlconnector://root:22312125@localhost/manage_group"  #Thay thế username và password bằng thông tin đăng nhập MySQL của bạn.
engine = create_engine(DATABASE_URL,connect_args={}) # connect_args={"check_same_thread": False} : dùng để tắt ktra luồng với SQLite; với MYSQL thì ko cần thiết
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base() # Tạo lớp cơ sở cho mô hình ORM

def get_db(): # Quản lý phiên làm vc với CSDL
    db = SessionLocal() # Tạo 1 phiên làm vc mới
    try:
        yield db  #Trả về phiên làm vc, cho phép sd nó trong 1 phạm vi hạn chế 
    finally:
        db.close() # đảm bảo phiên làm vc sẽ đc đóng lại sau khi hoàn thành để giải phóng tài nguyên


# Đoạn code dưới đây sẽ tạo bảng từ models nếu chưa có bảng trong CSDL, nếu đã có bảng sẵn thì sẽ ko thay đổi cấu trúc gì trong bảng 
# Import các mô hình của bạn
# from .models import * 

# def init_db():
#     # Tạo tất cả các bảng trong cơ sở dữ liệu
#     Base.metadata.create_all(bind=engine)

# # Gọi hàm init_db() để khởi tạo cơ sở dữ liệu
# if __name__ == "__main__":
#     init_db()   