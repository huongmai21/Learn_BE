from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# tokenUrl="token" : khai báo đường dẫn tương đối '/token' nơi client gửi thông tin đăng nhập, xử lý, tạo token và trả về cho client để sử dụng trong các yêu cầu sau này.

# OAuth2PasswordBearer cần tokenUrl để cấu hình và tài liệu hóa OAuth2 flow, nhưng nó không tương tác trực tiếp với tokenUrl trong quá trình trích xuất và xác thực token.
# mà nó chỉ tương tác với (Authorization: Bearer <token>).

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

# khi yêu cầu truy cập tài nguyên. Gửi yêu cầu GET với token trong header (Authorization: Bearer <token>).

# OAuth2PasswordBearer là 1 class 
# oauth2_scheme là 1 object của OAuth2PasswordBearer.
# Depends(oauth2_scheme) : FastAPI sẽ gọi oauth2_scheme.__call__() để trích xuất token từ Authorization: Bearer <token>.

# FastAPI sẽ tự động trích xuất token từ header và đưa nó vào tham số token của hàm xử lý.

