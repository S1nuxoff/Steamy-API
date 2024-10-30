from pydantic import BaseModel
from datetime import datetime

class FavouriteResponse(BaseModel):
    id: int
    user_id: int
    item: str
    game: str
    added_at: datetime

    class Config:
        orm_mode = True
