from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

# item_id dc định dạng kiểu 
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
