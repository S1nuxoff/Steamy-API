import aiohttp

from app.core.config import settings
from app.utils.common import clean_price
from app.utils.reference_data_loader import load_reference_data
from app.exceptions.custom_exceptions import GameNotFoundException, CurrencyNotFoundException, SteamAPIRequestException
from app.services.currency.get_currency_ratio import get_currency_ratio

reference_data = load_reference_data()


async def price(game: str, item: str, currency: str):
    game_data = reference_data["games"].get(game)
    if not game_data:
        raise GameNotFoundException()
    steam_id = game_data.get("steam_id")

    currency_data = reference_data["currencies"].get(currency)
    if not currency_data:
        raise CurrencyNotFoundException()

    ratio = await get_currency_ratio(currency)

    url = settings.STEAM_PRICE_OVERVIEW_URL
    params = {
        "appid": steam_id,
        "market_hash_name": item,
        "currency": "USD",
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()

                lowest_price_str = data.get("lowest_price")
                median_price_str = data.get("median_price")
                volume = data.get("volume")

                lowest_price = await clean_price(lowest_price_str) * ratio
                median_price = await clean_price(median_price_str) * ratio

                data = {
                    "min": round(lowest_price, 2),
                    "avg": round(median_price, 2),
                    "volume": volume,
                }
                return data
            else:
                raise SteamAPIRequestException()
