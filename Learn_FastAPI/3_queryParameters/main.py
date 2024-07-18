# Khi bạn khai báo các tham số hàm khác không phải là một phần của tham số đường dẫn,
# chúng sẽ tự động được hiểu là tham số "truy vấn".

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

#Truy vấn là tập hợp các cặp khóa-giá trị theo sau '?' trong một URL, được phân tách bằng ký tự '&'
# http://127.0.0.1:8000/items/
# would be the same as going to:
# http://127.0.0.1:8000/items/?skip=0&limit=10

# But if you go to, for example:
# http://127.0.0.1:8000/items/?skip=20
# The parameter values in your function will be:
# skip=20: because you set it in the URL
# limit=10: because that was the default value


# Có thể khai báo các tham số truy vấn tùy chọn bằng cách đặt mặc định của chúng thành 'None':
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

