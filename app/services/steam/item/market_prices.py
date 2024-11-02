import asyncio

from app.services.steam.item.price import price
from app.services.steam.markets.dmarket import dmarket_price
from app.services.steam.markets.skinport import skinport_price
from app.services.currency.get_currency_ratio import get_currency_ratio
from app.utils.reference_data_loader import load_reference_data
from app.exceptions.custom_exceptions import GameNotFoundException, CurrencyNotFoundException

reference_data = load_reference_data()


async def markets_prices(game: str, item: str, currency: str):
    game_data = reference_data["games"].get(game)
    if not game_data:
        raise GameNotFoundException()

    currency_data = reference_data["currencies"].get(currency)
    if not currency_data:
        raise CurrencyNotFoundException()

    dmarket_id = game_data.get("dmarket_id")
    steam_id = game_data.get("steam_id")

    ratio = await get_currency_ratio(currency)

    steam_data_response, dmarket_data_response, skinport_data_response = await asyncio.gather(
        price(game, item, currency),
        dmarket_price(dmarket_id, item),
        skinport_price(steam_id, item)
    )

    steam_data = None
    if steam_data_response:
        steam_data = {
            "market": "Steam",
            "min": steam_data_response.get("min"),
            "avg": steam_data_response.get("avg"),
            "volume": steam_data_response.get("volume"),
        }

    dmarket_data = None

    if dmarket_data_response:
        dmarket_data = {
            "market": "DMarket",
            "min": round(dmarket_data_response.get('min') * ratio, 2),
            "avg": round(dmarket_data_response.get('avg') * ratio, 2),
            "volume": dmarket_data_response.get('volume'),
        }

    skinport_data = None

    if skinport_data_response:
        skinport_data = {
            "market": "Skinport",
            "min": round(skinport_data_response.get('min') * ratio, 2),
            "avg": round(skinport_data_response.get('avg') * ratio, 2),
            "volume": skinport_data_response.get('volume')
        }

    markets_data = []

    if steam_data:
        markets_data.append(steam_data)

    if dmarket_data:
        markets_data.append(dmarket_data)

    if skinport_data:
        markets_data.append(skinport_data)

    return markets_data
