from fastapi import FastAPI

app = FastAPI()

# Tham số đường dẫn chứa đường dẫn

# 1. Path convertor ( trình chuyển đổi đường dẫn)
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# URL: /files//home/johndoe/myfile.txt