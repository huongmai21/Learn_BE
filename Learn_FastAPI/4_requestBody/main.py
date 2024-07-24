from fastapi import FastAPI
from pydantic import BaseModel   # đc sd để xđ các mô hình dl(data models) mmà API sẽ nhận và trả về


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):  # hàm nhận 1 obj 'Item' từ nd yêu cầu (request body)
    return item