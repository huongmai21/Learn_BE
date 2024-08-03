# Bạn cũng có thể khai báo phản hồi bằng cách sử dụng một lệnh tùy ý đơn giản, chỉ khai báo loại khóa và giá trị mà không cần sử dụng mô hình Pydantic.
# Điều này hữu ích nếu bạn không biết trước tên trường/thuộc tính hợp lệ (điều này cần thiết cho mô hình Pydantic).

from fastapi import FastAPI

app = FastAPI()


@app.get("/keyword-weights/", response_model=dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}