# app/api/v1/endpoints/steam.py
from fastapi import APIRouter, HTTPException, Query

from app.services.steam.item.price import price
from app.services.steam.item.sales import sales
from app.services.steam.item.liquidity import iquidity
from app.services.steam.item.market_prices import markets_prices
from app.services.steam.item.float import float
from app.services.steam.item.nameid import nameid

router = APIRouter()

@router.get("/price")
async def price_endpoint(game: str, item: str):
    data = await price(game, item)
    if not data.get("success"):
        raise HTTPException(status_code=404, detail="Item price not found")
    return data

@router.get("/sales")
async def sales_history_endpoint(
    game: str,
    item: str,
    period: str = Query("week", pattern="^(day|week|month|lifetime)$"),
):
    data = await sales(game, item, period)
    if not data.get("success"):
        raise HTTPException(status_code=404, detail="Sales history not found")
    return data

@router.get("/liquidity")
async def liquidity_endpoint(nameid: int):
    data = await iquidity(nameid)
    if not data.get("success"):
        raise HTTPException(status_code=404, detail="Sales history not found")
    return data

@router.get("/markets_prices")
async def markets_prices_endpoint(game: str, item:str):
    data = await markets_prices(game, item)
    if not data.get("success"):
        raise HTTPException(status_code=404, detail="Sales history not found")
    return data

@router.get("/float")
async def float_endpoint(rungame_url: str):
    data = await float(rungame_url)
    if not data.get("success"):
        raise HTTPException(status_code=404, detail="Sales history not found")
    return data

@router.get("/nameid")
async def nameid_endpoint(game: str, item:str):
    data = await nameid(game,item)
    if not data.get("success"):
        raise HTTPException(status_code=404, detail="Sales history not found")
    return data

