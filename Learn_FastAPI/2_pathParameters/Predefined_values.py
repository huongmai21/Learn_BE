# Nếu muốn các đường dẫn của bạn nhận những tham số đã đc định nghĩa trc (đã xác định)

from enum import Enum
from fastapi import FastAPI

# Import Enum and create a sub-class that inherits from str and from Enum.
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}



# from enum import Enum
# class Color(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3

# print(Color.RED)        # Output: Color.RED
# print(Color.RED.name)   # Output: RED
# print(Color.RED.value)  # Output: 1
