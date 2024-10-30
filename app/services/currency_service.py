# app/services/currency_service.py
import aiohttp
import asyncio
import re
from datetime import datetime
from typing import Optional, Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.currency import Currency
from app.db.session import async_session
from app.core.config import settings

CURRENCY_ID_MAP: Dict[int, str] = {1: "USD", 5: "RUB", 6: "PLN", 18: "UAH"}

async def currencies() -> Optional[list]:
    async with async_session() as session:
        result = await session.scalars(select(Currency))
        data = result.all()
        if not data:
            return None
        else:
            return [{"id": currency.id, "name": currency.name, "ratio": currency.ratio} for currency in data]

async def fetch_price(session: aiohttp.ClientSession, url: str, params: Dict) -> Optional[str]:
    try:
        async with session.get(url, params=params) as response:
            response.raise_for_status()
            data = await response.json()
            if data.get("success"):
                return data.get("lowest_price")
            else:
                return None
    except (aiohttp.ClientError, asyncio.TimeoutError, Exception) as e:
        print(f"Error fetching price: {e}")
        return None

def parse_price(price_str: str) -> float:
    price_str_nospace = price_str.replace(" ", "")
    match = re.search(r"[\d.,]+", price_str_nospace)
    if not match:
        raise ValueError(f"Cannot parse price string: {price_str}")

    amount_str = match.group(0)
    if amount_str.count(",") > amount_str.count("."):
        amount_str_clean = amount_str.replace(".", "").replace(",", ".")
    else:
        amount_str_clean = amount_str.replace(",", "")

    return float(amount_str_clean)

async def update_currencies_db(
        session: AsyncSession,
        currency_ratios: Dict[str, float],
        request_time: str
) -> None:
    try:
        async with session.begin():
            stmt = select(Currency).where(Currency.name.in_(currency_ratios.keys()))
            result = await session.execute(stmt)
            currencies = result.scalars().all()

            if not currencies:
                print("No currencies found in the database to update.")
                return

            for currency in currencies:
                new_ratio = currency_ratios.get(currency.name)
                if new_ratio is not None:
                    currency.ratio = new_ratio
                    currency.time = request_time
    except Exception as e:
        print(f"Error updating database: {e}")
        raise  # Re-raise exception after logging

async def update_currencies() -> Dict[str, Optional[str]]:
    appid = 730
    item = "AWP | Atheris (Field-Tested)"
    currency_ids = [1, 5, 6, 18]
    url = settings.STEAM_PRICE_OVERVIEW_URL
    params_base = {"appid": appid, "market_hash_name": item}

    async with aiohttp.ClientSession() as http_session, async_session() as db_session:
        tasks = []
        for currency_id in currency_ids:
            params = params_base.copy()
            params["currency"] = currency_id
            tasks.append(fetch_price(http_session, url, params))

        results = await asyncio.gather(*tasks, return_exceptions=True)

        lowest_prices: Dict[int, float] = {}
        for currency_id, result in zip(currency_ids, results):
            if isinstance(result, Exception):
                print(f"Exception for currency ID {currency_id}: {result}")
                continue

            price_str = result
            if price_str:
                try:
                    amount = parse_price(price_str)
                    lowest_prices[currency_id] = amount
                except ValueError as ve:
                    print(f"Error parsing price for currency ID {currency_id}: {ve}")
                    continue

        base_amount = lowest_prices.get(1)
        if not base_amount:
            return {"success": False, "error": "Base price not available"}

        request_time = datetime.utcnow().isoformat()
        currency_ratios = {}
        for currency_id in [5, 6, 18]:
            amount = lowest_prices.get(currency_id)
            if amount:
                ratio = amount / base_amount
                currency_ratios[CURRENCY_ID_MAP.get(currency_id, "UNKNOWN")] = ratio

        if currency_ratios:
            try:
                await update_currencies_db(db_session, currency_ratios, request_time)
            except Exception:
                return {"success": False, "error": "Database update failed"}

        return {"success": True, "request_time": request_time}
