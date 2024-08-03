# Bạn có thể khai báo một phản hồi là Sự kết hợp của hai types, 
# điều đó có nghĩa là phản hồi đó sẽ là một trong hai loại.
# Nó sẽ được xác định trong OpenAPI với AnyOf.

# Khi định nghĩa 1 Union , hãy bao gồm loại cụ thể nhất trước tiên, tiếp theo là loại ít cụ thể hơn. 
# Trong ví dụ bên dưới, PlaneItem cụ thể hơn xuất hiện trước CarItem trong Union[PlaneItem, CarItem].

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type: str = "car"


class PlaneItem(BaseItem):
    type: str = "plane"
    size: int


items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    return items[item_id]