from fastapi import FastAPI, HTTPException
from sqlmodel import Session, SQLModel, create_engine, select
import models as api_models

# SQL Engine
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/items/", response_model=api_models.Item)
def create_item(item: api_models.Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

@app.get("/items/", response_model=list[api_models.ItemPublic])
def read_items():
    with Session(engine) as session:
        items = session.exec(select(api_models.Item)).all()
        return items
    
@app.get("/items/{item_id}", response_model=api_models.ItemPublic)
def read_selected_item(item_id: int):
    with Session(engine) as session:
        item = session.get(api_models.Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail=f"Item of id {item_id} not Found")
        return item
    
@app.patch("/items/{item_id}", response_model=api_models.ItemPublic)
def update_item(item_id: int, item: api_models.ItemUpdate):
    with Session(engine) as session:
        current_item = session.get(api_models.Item, item_id)
        if not current_item:
            raise HTTPException(status_code=404, detail="Hero Not Found")
        item_data = item.model_dump(exclude_unset=True)
        current_item.sqlmodel_update(item_data)
        session.add(current_item)
        session.commit()
        session.refresh(current_item)
        return current_item
        

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    with Session(engine) as session:
        item = session.get(api_models.Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail=f"Item of id {item_id} not Found")
        session.delete(item)
        session.commit()
        return {"Ok": True}