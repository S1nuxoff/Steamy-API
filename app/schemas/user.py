from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    steam_id: Optional[int]
    premium: bool
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    tg_id: int
    username: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    steam_id: Optional[int] = None
    premium: Optional[bool] = None
class UserAddFavorite(BaseModel):
    item: str
    game: str

class UserRemoveFavorite(BaseModel):
    item: str
    game: str


