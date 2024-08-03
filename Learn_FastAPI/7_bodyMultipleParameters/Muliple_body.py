from fastapi import FastAPI
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
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results

# Trong trường hợp này, FastAPI sẽ nhận thấy rằng có nhiều hơn một tham số nội dung trong hàm (hai tham số là mô hình Pydantic).
#Vì vậy, sau đó nó sẽ sử dụng tên tham số làm khóa (tên trường) trong phần nội dung và mong đợi phần nội dung như:
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
    #     }
    # }