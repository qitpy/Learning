
from uuid import UUID
from datetime import datetime, time, timedelta
from fastapi import FastAPI, Query, Path, Body, Cookie, Response
from fastapi.responses import RedirectResponse
from pydantic import Field, EmailStr
from enum import Enum
from typing import Any

app = FastAPI()

# Path-parameter & Query-parameter

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

@app.get("/users/{useri_id}/items/{item_id}")
async def read_items(item_id: int, user_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "user_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# Request Body

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = Field(default=None, max_length=300, example="some description")
    price: float
    tax: float | None = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }

@app.post("/items/")
async def create_item(item: Item, q: str) -> Item:
    a = item.dict()
    a["q"] = q
    return item

# Query Validation

@app.get("/items/validate")
async def item_validate(q: str | None = Query(default=None, max_length=50, min_length=3)):
    results = {"items": "Foo"}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/validate/require")
async def read_items(q: str | None = Query(default=..., min_length=3)):
    result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result

# multiple values parameter
@app.get("/items/multi-query")
async def read_items(q: list[str] | None = Query(default=None, title="Query params list", description="Query string for the items to search in the database that have a good match", alias='item query', deprecated=True)):
    query_items = {"q": q}
    return query_items

# Path Validation
@app.get("/items/{item_id}/star")
async def read_items(*, item_id: int = Path(title="The ID of the item to get", gt=8, le=1000), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# multiple request body
@app.post("/items/multi-body")
async def read_items(item: Item, extra: str | None = Body(default="hihi")):
    results = {"item": item}
    if extra:
        results.update({"extra": extra})
    return results


# datatype

@app.put("/items/{item_id}/datetime")
async def read_items(
    item_id: UUID,
    start_datetime: datetime | None = Body(default=None),
    end_datetime: datetime | None = Body(default=None),
    repeat_at: time | None = Body(default=None),
    process_after: timedelta | None = Body(default=None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }

# Cookie

@app.get("/items/")
async def read_items2(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}

# Response Model
@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item


@app.get("/items/", response_model=list[Item])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user

@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}