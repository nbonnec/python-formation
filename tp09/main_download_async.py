#!/usr/bin/env python
import asyncio
import time

import httpx
from bs4 import BeautifulSoup

URL: str = 'https://logs.eolem.com/'


async def download(log: str) -> None:
    async with httpx.AsyncClient() as client:
        rsp = await client.get(log)
        filename = log.split('/')[-1]
        with open(filename, 'w') as f:
            f.write(rsp.text)


async def main():
    start = time.perf_counter()

    rsp = httpx.get(URL)
    soup = BeautifulSoup(rsp.text, 'html.parser')
    all_a = soup.find_all('a')

    all_logs = [f'{URL}/{a["href"]}' for a in all_a if a['href'].endswith('.log')]

    tasks = [download(log) for log in all_logs]
    await asyncio.gather(*tasks)

    print(time.perf_counter() - start)


if __name__ == '__main__':
    asyncio.run(main())
