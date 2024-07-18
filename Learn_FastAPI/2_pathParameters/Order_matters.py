from fastapi import FastAPI

app = FastAPI()

# Vấn đề thứ tự
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

#Đường dẫn cho "/users/{user_id}"" cũng khớp với "/users/me",
# nó sẽ nghĩ rằng đang nhận tham số user_id có giá trị là "me".
#Similarly, you cannot redefine a path operation 