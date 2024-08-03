from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# Bạn có thể khai báo tất cả các tham số tương tự như đối với Query.
# Tham số đường dẫn luôn được yêu cầu vì nó phải là một phần của đường dẫn.
# Ngay cả khi bạn khai báo nó bằng None hoặc đặt giá trị default, nó sẽ không ảnh hưởng gì,
# nó vẫn luôn được yêu cầu.