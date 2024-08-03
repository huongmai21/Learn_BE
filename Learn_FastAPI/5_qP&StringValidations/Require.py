# 1. tham số truy vấn có giá trị mặc định -> không bắt buộc phải có trong URL 
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"): # giá trị mặc định là fixedquery
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# 2. tham số truy vấn bắt buộc phải có trong URL
    # Cách 1. Bỏ giá trị mặc định : async def read_items(q: Annotated[str, Query(min_length=3)]):
    # Cách 2. thêm dấu "..." vào query và bỏ giá trị mặc định : async def read_items(q: Annotated[str, Query(...,min_length=3)]):


@app.get("/get_item/")
async def read_items(q: Annotated[str | None, Query(...,min_length=3)]): # q nhận giá trị ở dạng string hoặc None, và q bắt buộc => khi q = None thì cũng phải khai báo vào URL
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results