# app/utils/common.py
import re
import urllib.parse

from app.core.config import settings

async def is_url(url):
    url_pattern = re.compile(
        r"^(https?:\/\/)?"
        r"(([A-Za-z0-9-]+\.)+[A-Za-z]{2,})"
        r"(\/[A-Za-z0-9-._~:/?#\[\]@!$&\'()*+,;=%]*)?$"
    )
    return re.match(url_pattern, url) is not None

async def clear_url(url, appid):
    if not await is_url(url):
        return url

    appid_pattern = r"/listings/(\d+)/([^/?#]+)"
    match = re.search(appid_pattern, url)
    if not match:
        return False
    url_appid = int(match.group(1))
    if url_appid != appid:
        return False
    else:
        encoded_item = match.group(2)
        encoded_item = encoded_item.split("https://")[0]
        decoded_item = urllib.parse.unquote(encoded_item)
        return decoded_item

async def clean_price(price_str):
    if not price_str:
        return 0.0
    clean_str = re.sub(r"[^\d.,]", "", price_str)
    clean_str = clean_str.replace(",", ".")
    clean_str = clean_str.rstrip(".")
    return float(clean_str)

async def calculate_margin(item_lowest_sell_order, item_highest_buy_order):
    sell_order_after_commission = round(
        item_lowest_sell_order * (1 - settings.STEAM_COMMISSION_RATE), 2
    )
    margin_value = round(sell_order_after_commission - item_highest_buy_order, 2)
    margin_percentage = round(
        (margin_value / item_highest_buy_order) * 100
    )
    return sell_order_after_commission, margin_value, margin_percentage
