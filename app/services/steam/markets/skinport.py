import requests
import time
from app.core.config import settings

cache = {}

async def skinport_price(app_id, item):
    current_time = time.time()
    if app_id in cache:
        cached_time, response = cache[app_id]
        if current_time - cached_time < 300:
            pass
        else:

            response = requests.get(settings.SKINPORT_MARKET_ITEMS_URL, params={
                "app_id": app_id,
                "currency": "USD",
                "tradable": 0
            }).json()
            cache[app_id] = (current_time, response)
    else:

        response = requests.get(settings.SKINPORT_MARKET_ITEMS_URL, params={
            "app_id": app_id,
            "currency": "USD",
            "tradable": 0
        }).json()
        cache[app_id] = (current_time, response)

    for market_item in response:
        if market_item.get('market_hash_name') == item:
            result = {
                'page': market_item.get('item_page'),
                'min': market_item.get('min_price'),
                'avg': market_item.get('median_price'),
                'volume': market_item.get('quantity')
            }
            return result
    return None
