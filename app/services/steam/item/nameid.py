import aiohttp
import re
import urllib.parse

from app.core.config import settings
from app.utils.reference_data_loader import load_reference_data
from app.exceptions.custom_exceptions import GameNotFoundException

reference_data = load_reference_data()

regex = re.compile(r"Market_LoadOrderSpread\( (\d+) \)")

async def nameid(game: str, item: str, timeout: int = 10):
    game_data = reference_data["games"].get(game)
    if not game_data:
        raise GameNotFoundException()
    steam_id = game_data.get("steam_id")

    encoded_name = urllib.parse.quote(item)
    url = f"{settings.STEAM_MARKET_LISTINGS_URL}{steam_id}/{encoded_name}"

    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=timeout)) as session:
        async with session.get(url) as response:
            response.raise_for_status()
            html_data = await response.text()

    id_match = regex.search(html_data)

    if not id_match:
        return {"success": False}

    item_nameid = int(id_match.group(1))
    return {'success': True, 'nameid': item_nameid}


