from fastapi import APIRouter, HTTPException, Query

from app.schemas.item import Item
from app.services.item.get_item_by_hash_name import get_item_by_hash_name

router = APIRouter()

@router.get("/", response_model=Item, summary="Get item by name")
async def item_by_name(market_hash_name: str):
    item = await get_item_by_hash_name(market_hash_name)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

