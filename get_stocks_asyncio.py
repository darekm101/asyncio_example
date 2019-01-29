import asyncio
import aiohttp
import json


# Generate a list of symbols 
symbols = "SPY AAPL NVDA MDB V OKTA".split()


def generate_futures(symbols):
    futures = []
    for symbol in symbols:
        url = f"https://api.iextrading.com/1.0/stock/{symbol}/quote"
        future = asyncio.ensure_future(main(url))
        futures.append(future)
    return futures

async def fetch(session, url):
    async with session.get(url) as response: 
        return json.loads(await response.text())

async def main(url):
    async with aiohttp.ClientSession() as session: 
     json = await fetch(session, url)
     print(json)

futures = generate_futures(symbols)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))
