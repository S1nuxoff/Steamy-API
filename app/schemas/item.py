# app/schemas/steam_item.py
from pydantic import BaseModel

class ItemBase(BaseModel):
    nameid: int
    hash_name: str
    game: int

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
