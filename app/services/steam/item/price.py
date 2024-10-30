import aiohttp

from app.core.config import settings
from app.utils.common import clean_price
from app.utils.reference_data_loader import load_reference_data
from app.exceptions.custom_exceptions import GameNotFoundException

reference_data = load_reference_data()


async def price(game: str, item: str):
    game_data = reference_data["games"].get(game)
    if not game_data:
        raise GameNotFoundException()
    steam_id = game_data.get("steam_id")

    url = settings.STEAM_PRICE_OVERVIEW_URL
    params = {
        "appid": steam_id,
        "market_hash_name": item,
        "currency": "USD",
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            response.raise_for_status()
            data = await response.json()
            if data.get("success"):
                lowest_price_str = data.get("lowest_price")
                median_price_str = data.get("median_price")
                volume = data.get("volume")
                lowest_price = await clean_price(lowest_price_str)
                median_price = await clean_price(median_price_str)
                data = {
                    "lowest_price": lowest_price,
                    "median_price": median_price,
                    "volume": volume,
                }
                return {"success": True, "data": data}
            else:
                return {"success": False}
