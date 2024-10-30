import aiohttp

from app.core.config import settings
from app.utils.common import clean_price, calculate_margin


async def iquidity(nameid: int):
    item_orders_histogram_url = f"{settings.ITEM_ORDERS_HISTOGRAM_URL}?country=USA&language=english&currency=1&item_nameid={nameid}&two_factor=0&norender=1"
    async with aiohttp.ClientSession() as session:
        async with session.get(item_orders_histogram_url) as response:
            response.raise_for_status()
            item_orders_histogram_data = await response.json()
    item_lowest_sell_order_str = item_orders_histogram_data.get("sell_order_price")
    item_highest_buy_order_str = item_orders_histogram_data.get("buy_order_price")
    if not item_lowest_sell_order_str or not item_highest_buy_order_str:
        raise ValueError("Missing necessary pricing data from Steam.")
    item_lowest_sell_order = await clean_price(item_lowest_sell_order_str)
    item_highest_buy_order = await clean_price(item_highest_buy_order_str)

    sell_order_after_commission, margin_value, margin_percentage = await calculate_margin(
        item_lowest_sell_order, item_highest_buy_order
    )
    margin_status = False if margin_value < 0 else True
    data = {
        "success": True,
        "highest_buy_order": item_highest_buy_order_str,
        "highest_sell_order_no_fee": sell_order_after_commission,
        "lowest_sell_order": item_lowest_sell_order_str,
        "margin_value": margin_value,
        "margin": margin_percentage,
        "margin_status": margin_status,
    }
    return data

