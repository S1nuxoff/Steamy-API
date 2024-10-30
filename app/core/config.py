# app/core/config.py
import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Steamy API"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "A description of your API"
    API_KEY: str = os.getenv("API_KEY")
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    STEAM_WEB_API_KEY: str = os.getenv("STEAM_WEB_API")
    DMARKET_API_KEY: str = os.getenv("DMARKET_API")
    SHADOWPAY_API_KEY: str = os.getenv("SHADOWPAY_API")

    # Steam settings
    STEAM_COMMISSION_RATE: float = 0.1233
    STEAM_BASE_URL: str = "https://steamcommunity.com/market/listings"
    ITEM_ORDERS_HISTOGRAM_URL: str = "https://steamcommunity.com/market/itemordershistogram"
    STEAM_PRICE_OVERVIEW_URL: str = "https://steamcommunity.com/market/priceoverview/"
    STEAM_MARKET_LISTINGS_URL: str = "https://steamcommunity.com/market/listings/"
    # DMarket settings
    DMARKET_MARKET_ITEMS_URL: str = "https://api.dmarket.com/exchange/v1/market/items"

    # Skinport settings
    SKINPORT_MARKET_ITEMS_URL: str = "https://api.skinport.com/v1/items"

    class Config:
        case_sensitive = True

settings = Settings()
