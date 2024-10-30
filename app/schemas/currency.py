# app/schemas/currency.py
from datetime import datetime
from pydantic import BaseModel

class CurrencyBase(BaseModel):
    name: str
    ratio: float

class CurrencyCreate(CurrencyBase):
    pass

class Currency(CurrencyBase):
    id: int
    time: datetime

    class Config:
        orm_mode = True
