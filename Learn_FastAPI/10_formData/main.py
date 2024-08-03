# Khi bạn cần nhận các trường biểu mẫu thay vì JSON, bạn có thể sử dụng Form.
# Trc tiên cần cài đặt "python-multipart" : pip install python-multipart

from typing import Annotated

from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}