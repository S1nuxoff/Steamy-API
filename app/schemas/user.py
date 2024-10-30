from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    steam_id: Optional[int]
    premium: bool
    language: str
    currency: str
    game: str
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    tg_id: int
    username: str
    language: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    steam_id: Optional[int] = None
    premium: Optional[bool] = None
    language: Optional[str] = None
    currency: Optional[str] = None
    game: Optional[str] = None

class UserAddFavorite(BaseModel):
    item: str
    game: str

class UserRemoveFavorite(BaseModel):
    item: str
    game: str


