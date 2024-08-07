# import thư viện
from sqlalchemy import create_engine    # create_engine: Hàm này từ SQLAlchemy được sử dụng để thiết lập kết nối với cơ sở dữ liệu
from sqlalchemy.ext.declarative import declarative_base     # declarative_base: Hàm này tạo ra một lớp cơ sở mà tất cả các models ORM của bạn sẽ kế thừa. Nó là phần cơ bản của mô hình đối tượng quan hệ (ORM).

from sqlalchemy.orm import sessionmaker     # sessionmaker: Hàm này tạo ra một lớp Session mà bạn sẽ sử dụng để tương tác với cơ sở dữ liệu.


# cấu hình kết nối CSDL
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:22312125@localhost:3306/learn_fastapi"
# tạo engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# tạo SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# tạo base
Base = declarative_base()