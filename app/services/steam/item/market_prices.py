import asyncio
from app.services.steam.item.price import price
from app.services.steam.markets.dmarket import dmarket_price
from app.services.steam.markets.skinport import skinport_price
from app.utils.reference_data_loader import load_reference_data
from app.exceptions.custom_exceptions import GameNotFoundException

reference_data = load_reference_data()

async def markets_prices(game:str, item:str):
    game_data = reference_data["games"].get(game)
    if not game_data:
        raise GameNotFoundException()
    dmarket_id = game_data.get("dmarket_id")
    steam_id = game_data.get("steam_id")
    steam_data_response, dmarket_data_response, skinport_data_response = await asyncio.gather(
        price(game, item),
        dmarket_price(dmarket_id, item),
        skinport_price(steam_id, item)
    )

    steam_data = None
    if steam_data_response:
        steam_data = {
            "success":True,
            "market": "Steam",
            "min": steam_data_response["data"].get("lowest_price"),
            "avg": steam_data_response["data"].get("median_price"),
            "volume": steam_data_response["data"].get("volume"),
        }

    dmarket_data = None

    if dmarket_data_response:
        dmarket_data = {
            "market": "DMarket",
            "min": dmarket_data_response.get('min'),
            "avg": dmarket_data_response.get('avg'),
            "volume": dmarket_data_response.get('volume'),
        }

    skinport_data = None

    if skinport_data_response:
        skinport_data = {
            "market": "Skinport",
            "min": skinport_data_response.get('min'),
            "avg": skinport_data_response.get('avg'),
            "volume": skinport_data_response.get('volume'),
        }


    markets_data = []

    if steam_data:
        markets_data.append(steam_data)

    if dmarket_data:
        markets_data.append(dmarket_data)

    if skinport_data:
        markets_data.append(skinport_data)

    result = {
        "success": True,
        "markets": markets_data
    }

    return result
