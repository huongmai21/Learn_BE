# Hãy nhớ rằng khi sử dụng Truy vấn bên trong Annotated, bạn không thể sử dụng tham số mặc định cho Truy vấn.
# Thay vào đó hãy sử dụng giá trị mặc định thực tế của tham số hàm. Nếu không, nó sẽ không nhất quán.

# For example, this is not allowed:
# q: Annotated[str, Query(default="rick")] = "morty"
# Vì ko rõ giá trị mặc định là "rick" or "morty".
# Vì vậy, bạn nên sử dụng (tốt nhất là): q: Annotated[str, Query()] = "rick" 

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

