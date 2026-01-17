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

items = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items")
def read_all_items():
    return items

@app.get("/items/{item_id}")
def read_item_id(item_id : int, in_stock: bool = True) -> Item:
    if item_id < len(items) and in_stock:
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item of id {item_id} Not Found or query parameter is invalid")


@app.post("/items")
def create_item(item_id: int, item_name: str, item_description: str,
    item_price: float, item_in_stock: bool, item: Item):
    item.id = item_id
    items.append(item)
    return items

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id < len(items):  
        item.id = item_id
        item.id = item_id
        item.name = item_name
        item.description = item_description
        item.price = item_price
        item.in_stock = item_in_stock
        items[item_id] = item
    else:
        raise HTTPException(status_code=404, detail=f"Item of id {item_id} not found")
    return items

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < len(items):
        items.remove(items[item_id])    
    else:
        raise HTTPException(status_code=404, detail=f"Item of id {item_id} Not found")
    return {"Message": f"Item {item_id} deleted successfully"}