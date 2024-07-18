from fastapi import FastAPI

app = FastAPI()

#Tham số truy vấn bắt buộc needy
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

# URL: /items/abc?needy=true&skip=10&limit=100
# Kết quả: 
# {
#   "item_id": "abc",
#   "needy": "true",
#   "skip": 10,
#   "limit": 100
# }