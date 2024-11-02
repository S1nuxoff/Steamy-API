from datetime import datetime
from pydantic import BaseModel


class Currency(BaseModel):
    id: int
    name: str
    ratio: float
    time: datetime

    class Config:
        orm_mode = True
