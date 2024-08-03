# Xác thực số: lớn hơn hoặc bằng
# Với Truy vấn và Đường dẫn (và những thứ khác bạn sẽ thấy sau), bạn có thể khai báo các ràng buộc về số.

from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()

# 1. greater than or equal
# Ở đây, với ge=1, item_id sẽ cần phải là số nguyên "lớn hơn hoặc bằng" 1.
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# 2.greater than and less than or equal
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)],
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# 3.floats, greater than and less than
from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# gt: greater than
# ge: greater than or equal
# lt: less than
# le: less than or equal