#!/usr/bin/env python3
import asyncio
import re
import sys
from datetime import datetime, timezone

import httpx
from sqlalchemy import select
from app.db.session import async_session
from app.models.currency import Currency


if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


url = "https://steamcommunity.com/market/priceoverview/"
appid = 730
market_hash_name = "AWP | Atheris (Field-Tested)"
currencies = {
    "USD": 1,
    "UAH": 18,
    "PLN": 6,
    "RUB": 5,
    "EUR": 3
}


def extract_price(price_str):
    # Remove all characters except digits and commas
    clean_str = re.sub(r'[^\d,]', '', price_str)
    # Replace the last comma with a dot for correct float conversion
    if ',' in clean_str:
        clean_str = clean_str[::-1].replace(',', '.', 1)[::-1]
    return float(clean_str)

async def main():
    base_price = None

    async with httpx.AsyncClient() as client, async_session() as session:
        for currency_name, currency_code in currencies.items():
            params = {
                "appid": appid,
                "market_hash_name": market_hash_name,
                "currency": currency_code
            }

            # Perform the request
            response = await client.get(url, params=params)
            data = response.json()

            # Check for a successful response
            if data.get("success"):
                # Extract and process lowest_price
                price_str = data.get("lowest_price", "0")
                price = extract_price(price_str)

                # Record USD price for exchange rate calculations
                if currency_name == "USD":
                    base_price = price
                    print(f"{currency_name}: {price} USD")
                    ratio = 1.0  # USD to USD ratio is 1
                else:
                    # Calculate exchange rate relative to USD
                    ratio = (price / base_price) * 100 if base_price else 0
                    print(f"{currency_name}: {price_str} -> {price} ({ratio:.4f} {currency_name}/USD)")

                # Save ratio and time to the database
                currency_id = currencies[currency_name]

                # Find the currency with the same id
                result = await session.execute(
                    select(Currency).where(Currency.id == currency_id)
                )
                currency_obj = result.scalar_one_or_none()

                if currency_obj:
                    currency_obj.ratio = ratio
                    currency_obj.time = datetime.now(timezone.utc)
                else:
                    currency_obj = Currency(
                        id=currency_id,
                        name=currency_name,
                        ratio=ratio,
                        time=datetime.now(timezone.utc)
                    )
                    session.add(currency_obj)

                await session.commit()
            else:
                print(f"Failed to retrieve price for {currency_name}")

            # Delay between requests
            await asyncio.sleep(3)

if __name__ == "__main__":
    asyncio.run(main())
