from enum import Enum

from fastapi import FastAPI

app = FastAPI()

class PossibleChoices(str, Enum):
    option_a = "A"
    option_b = "B"
    option_c = "C"

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Order matters
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "The current user"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/options/{option}")
async def get_options(option: PossibleChoices):
    if option == PossibleChoices.option_a:
        return {"option": "A"}
    elif option == PossibleChoices.option_b:
        return {"option": "B"}
    
    return {"option": "C"}

# When the argument is a path itself, use :path
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# Query params (?key=value)
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/query-params")
async def get_params(skip: int = 0, limit: int = 10):
    return fake_items_db[skip:skip + limit]

@app.get("/new-items/{item_id}")
# Python Version < 3.10:
## from typing import Union
## async def get_new_items(item_id: int, q: Union[str, None] = None):
# Python Version >= 3.10:
async def get_new_items(item_id: int, q: str | None = None, short: bool = False):
    if q:
        return {"item_id": item_id, "q": q}
    if not short:
        return {"item_id": item_id, "q": "Hello World this is a really long description!"}
    return {"item_id": item_id}

# Multiple Path and Query Params
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: str, item_id: int, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "user_id": user_id}
    if q:
        item["q"] = q
    if not short:
        item["description"] = "Hello World this is a really long description!"
    return item