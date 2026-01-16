from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float
    in_stock: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items")
def read_all_items():
    return items

@app.get("/items/{item_id}")
def read_item(item_id : int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item of id {item_id} Not Found")
        
@app.post("/items")
def create_item(item_id: int, item: Item):
    item.id = item_id
    items.append(item)
    return items

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}