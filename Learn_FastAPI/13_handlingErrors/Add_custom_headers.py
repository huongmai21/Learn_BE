from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}

# Có một số trường hợp mà việc có thể thêm tiêu đề tùy chỉnh vào lỗi HTTP là hữu ích. Ví dụ, đối với một số loại bảo mật.
# Có lẽ bạn sẽ không cần sử dụng nó trực tiếp trong mã của mình.
# Nhưng trong trường hợp bạn cần nó cho một kịch bản nâng cao, bạn có thể thêm tiêu đề tùy chỉnh: