from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None): 
    query_items = {"q": q}
    return query_items

# tham số q sẽ ở dạng list với kiểu dữ liệu là string
# nếu thay list[str] bằng list thì q sẽ nhận list với kiểu dữ liệu bất kì mà không cần xác thực kiểu dữ liệu đó là string.
# nếu trong URL không có thì mặc định là None, giá trị mặc định chỉ có thể là None hoặc 1 list với kiểu dữ liệu là string, những kiểu khác bị lỗi 