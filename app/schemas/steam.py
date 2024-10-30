from typing import Any, Dict, List
from pydantic import BaseModel

class SteamItemPrice(BaseModel):
    lowest_price: float
    median_price: float
    volume: int

class SteamItemSalesHistory(BaseModel):
    min: float
    min_volume: int
    max: float
    max_volume: int
    avg: float
    avg_volume: int
    volume: int
    dates: List[str]
    prices: List[float]

class SteamUserDetails(BaseModel):
    pass

