import aiohttp

async def float(rungame_url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://api.csgofloat.xyz/?item_url={rungame_url}"
            ) as response:
                response.raise_for_status()
                data = await response.json()

                if data.get("success"):
                    item_info = data.get("iteminfo", {})
                    return {
                        "success":True,
                        "origin": item_info.get("origin"),
                        "paint_seed": item_info.get("paintseed"),
                        "paint_index": item_info.get("paintindex"),
                        "float_value": item_info.get("floatvalue"),
                    }
                else:
                    error_message = data.get("error", "Unknown error")
                    raise Exception(f"Error in response: {error_message}")

    except aiohttp.ClientError as e:
        raise Exception(f"Error fetching float data: {e}")

