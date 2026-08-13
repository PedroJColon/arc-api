from sqlmodel import Field, SQLModel

# Follows FastAPI documentations of SQLModels
# Link: https://fastapi.tiangolo.com/tutorial/sql-databases/
# Additional Link: https://sqlmodel.tiangolo.com/tutorial/fastapi/multiple-models/#review-creation-schema

class ItemBase(SQLModel):
    name: str = Field(index=True)
    description: str
    price: float = Field(default=None, index=True)
    in_stock: bool | None = Field(default=None, index=True)

class Item(ItemBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class ItemCreate(ItemBase):
    pass

class ItemPublic(ItemBase):
    id: int

class ItemUpdate(SQLModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    in_stock: bool  | None = None