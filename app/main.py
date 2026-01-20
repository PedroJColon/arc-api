from typing import Annotated, Union
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Depends, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import BaseModel


# SQL Engine
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str
    price: float = Field(index=True)
    in_stock: bool | None = Field(default=None, index=True)    

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    yield
    print("Shutdown")


app = FastAPI(lifespan=lifespan)

# class Item(BaseModel):
#     id: int
#     name: str
#     description: str
#     price: float
#     in_stock: Union[bool, None] = None

# items = []

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items")
# def read_all_items():
#     return items

# @app.get("/items/{item_id}")
# def read_item_id(item_id : int, in_stock: bool = True) -> Item:
#     if item_id < len(items) and in_stock:
#         return items[item_id]
#     else:
#         raise HTTPException(status_code=404, detail=f"Item of id {item_id} Not Found or query parameter is invalid")


# @app.post("/items")
# def create_item(item_id: int, item_name: str, item_description: str,
#     item_price: float, item_in_stock: bool, item: Item):
#     item.id = item_id
#     item.name = item_name
#     item.description = item_description
#     item.price = item_price
#     item.in_stock = item_in_stock
#     items.append(item)
#     return items

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item_name: str, item_description: str,
#     item_price: float, item_in_stock: bool, item: Item):
#     if item_id < len(items):  
#         item.id = item_id
#         item.id = item_id
#         item.name = item_name
#         item.description = item_description
#         item.price = item_price
#         item.in_stock = item_in_stock
#         items[item_id] = item
#     else:
#         raise HTTPException(status_code=404, detail=f"Item of id {item_id} not found")
#     return items

# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     if item_id < len(items):
#         items.remove(items[item_id])    
#     else:
#         raise HTTPException(status_code=404, detail=f"Item of id {item_id} Not found")
#     return {"Message": f"Item {item_id} deleted successfully"}