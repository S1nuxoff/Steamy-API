# app/api/v1/api.py
from fastapi import APIRouter
from app.api.v1.endpoints import user, items, currencies
from app.api.v1.endpoints.steam import steam_user, steam_item

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user", tags=["User"])
api_router.include_router(items.router, prefix="/items", tags=["Items"])
api_router.include_router(currencies.router, prefix="/currencies", tags=["Currencies"])
api_router.include_router(steam_user.router, prefix="/steam/user", tags=["Steam User"])
api_router.include_router(steam_item.router, prefix="/steam/item", tags=["Steam Item"])
