# Biểu thức chính quy : pattern

from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Pydantic v1 "regex" thay vì "pattern"
# Trước Pydantic phiên bản 2 và trước FastAPI 0.100.0, tham số này được gọi là biểu thức chính quy (regex) thay vì mẫu (pattern) nhưng hiện tại nó không được dùng nữa.

# q: Annotated[
#         str | None, Query(min_length=3, max_length=50, regex="^fixedquery$")
#     ] = None,
