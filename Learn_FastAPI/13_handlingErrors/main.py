from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found") #Hàm sẽ ko chạy phần còn lại của đường dẫn, mà sẽ chấm dứt yêu cầu đó nay lập tức và gửi lỗi HTTP đến máy khách
    return {"item": items[item_id]}

# Result:

# th1: http://example.com/items/foo(một item_id "foo"), máy khách đó sẽ nhận được mã trạng thái HTTP là 200 
# và phản hồi JSON là:
#{
#   "item": "The Foo Wrestlers"
# }

#t th2: http://example.com/items/bar(không tồn tại item_id "bar"), máy khách đó sẽ nhận được mã trạng thái HTTP là 404 (lỗi "không tìm thấy") 
# và phản hồi JSON là:
# {
#   "detail": "Item not found"
# }