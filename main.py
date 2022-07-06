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