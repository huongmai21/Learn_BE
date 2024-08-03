from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User, importance: Annotated[int, Body()]
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results

#Tương tự như cách có Truy vấn và Đường dẫn để xác định dữ liệu bổ sung cho các tham số truy vấn và đường dẫn,
# FastAPI cũng cung cấp tương tự cho phần nội dung : sử dụng từ khoá "importance" và "Body()"
#Kq:
    # {
    #     "item": {
    #         "name": "Foo",
    #         "description": "The pretender",
    #         "price": 42.0,
    #         "tax": 3.2
    #     },
    #     "user": {
    #         "username": "dave",
    #         "full_name": "Dave Grohl"
    #     },
    #     "importance": 5
    # }