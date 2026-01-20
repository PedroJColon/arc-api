from fastapi import FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select

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

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

@app.get("/items/", response_model=list[Item])
def read_items():
    with Session(engine) as session:
        items = session.exec(select(Item)).all()
        return items
    
@app.get("/items/{item_id}", response_model=Item)
def read_selected_item(item_id: int, in_stock_field: bool = True):
    with Session(engine) as session:
        item = session.get(Item, item_id | in_stock_field,)
        if not item:
            raise HTTPException(status_code=404, detail=f"Item of id {item_id} not Found")
        return item

@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail=f"Item of id {item_id} not Found")
        session.delete(item)
        session.commit()
        return {"Ok": True}