from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from sqlmodel import Session, SQLModel, create_engine, select
import models as api_models

# SQL Engine

# Set the necessary variables needed for this sqllite to properly work
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Once set, create engine and connections arguments needed
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

# Put it all together to create database file
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# With setup done, call FastAPI to run app
app = FastAPI()

# Async function for handling lifespan of application
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()

# Create item and have it be saved to sql database thanks to session and engine
@app.post("/items/", response_model=api_models.ItemPublic)
def create_item(item: api_models.ItemCreate):
    with Session(engine) as session:
        db_item = api_models.Item.model_validate(item)
        session.add(db_item)
        session.commit()
        session.refresh(db_item)
        return db_item

# Read all items, no limits given for this smaller scale project. Might be added in quick patch
@app.get("/items/", response_model=list[api_models.ItemPublic])
def read_items():
    with Session(engine) as session:
        items = session.exec(select(api_models.Item)).all()
        return items

# Read item of selected ID, follows similar steps as previous function
@app.get("/items/{item_id}", response_model=api_models.ItemPublic)
def read_selected_item(item_id: int):
    with Session(engine) as session:
        item = session.get(api_models.Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail=f"Item of id {item_id} not Found")
        return item

# Update the selected Item, will raise if item is not found in case user tries to use it as a way to create an item
@app.patch("/items/{item_id}", response_model=api_models.ItemPublic)
def update_item(item_id: int, item: api_models.ItemUpdate):
    with Session(engine) as session:
        current_item = session.get(api_models.Item, item_id)
        if not current_item:
            raise HTTPException(status_code=404, detail="Item of {item_id} Not Found")
        item_data = item.model_dump(exclude_unset=True)
        current_item.sqlmodel_update(item_data)
        session.add(current_item)
        session.commit()
        session.refresh(current_item)
        return current_item


# Delete item from database file, simple as read and read selected
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    with Session(engine) as session:
        item = session.get(api_models.Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail=f"Item of id {item_id} not Found")
        session.delete(item)
        session.commit()
        return {"Ok": True}
