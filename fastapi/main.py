from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/item/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    letnet = "letnet"

@app.get("/enum-path/{enum_path}")
async def get_model(enum_path: ModelName):
    if enum_path is ModelName.alexnet:
        return {"model_name": enum_path, "message": "Deep Learning FTW!"}

    if enum_path.value == "lenet":
        return {"model_name": enum_path, "message": "LeCNN all the images"}

    return {"model_name": enum_path, "message": "Have some residuals"}

@app.get("/file/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

@app.get("/items/{item_id}")
async def read_items(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}