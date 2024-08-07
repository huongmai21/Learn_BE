from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}

# nếu bạn yêu cầu /unicorns/yolo, thao tác đường dẫn sẽ raise là UnicornException.
# Nhưng nó sẽ được xử lý bởi unicorn_exception_handler.
# Vì vậy, bạn sẽ nhận được một lỗi sạch, với mã trạng thái HTTP là 418 và nội dung JSON là:
# {"message": "Oops! yolo did something. There goes a rainbow..."}