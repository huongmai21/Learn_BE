#1. import FastAPI
from fastapi import FastAPI

#2. Tạo 1 instance từ FastAPI
app = FastAPI()

#3. Tạo đường dẫn (path/route)
@app.get("/Welcome")        # @something : decorator
def read_root():
    return "Welcome to my project !"

# Để chạy app sd câu lệnh : uvicorn main:app --reload