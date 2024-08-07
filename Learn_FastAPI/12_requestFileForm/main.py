# Trc tiên cần cài đặt "python-multipart" : pip install python-multipart
from typing import Annotated

from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }

# Các tệp và trường biểu mẫu sẽ được tải lên dưới dạng dữ liệu biểu mẫu và bạn sẽ nhận được các tệp và trường biểu mẫu.
# Và bạn có thể khai báo một số tệp dưới dạng byte và một số dưới dạng UploadFile.