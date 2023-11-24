#!/usr/bin/env python
import asyncio
import time

import httpx
from bs4 import BeautifulSoup

URL: str = 'https://logs.eolem.com/'


# async def download(log: str) -> None:
#     async with httpx.AsyncClient() as client:
#         rsp = await client.get(log)  # Nope, this is a synchronous call!
#         filename = log.split('/')[-1]
#         with open(filename, 'w') as f:
#             f.write(rsp.text)

async def download(dl_queue: asyncio.Queue, save_queue: asyncio.Queue) -> None:
    while True:
        url = await dl_queue.get()
        async with httpx.AsyncClient() as client:
            rsp = await client.get(url)
            save_queue.put_nowait({'filename': url.split('/')[-1], 'data': rsp.text})
        dl_queue.task_done()


async def write(save_queue: asyncio.Queue) -> None:
    while True:
        to_save = await save_queue.get()
        with open(to_save['filename'], 'w') as f:
            f.write(to_save['data'])
        save_queue.task_done()


async def main():
    start = time.perf_counter()

    download_queue = asyncio.Queue()
    save_queue = asyncio.Queue()
    download_queue_worker_cnt = 5
    save_queue_worker_cnt = 3

    rsp = httpx.get(URL)
    soup = BeautifulSoup(rsp.text, 'html.parser')
    all_a = soup.find_all('a')

    all_urls = [f'{URL}/{a["href"]}' for a in all_a if a['href'].endswith('.log')]

    tasks = []
    for i in range(download_queue_worker_cnt):
        tasks.append(asyncio.create_task(download(download_queue, save_queue)))

    for i in range(save_queue_worker_cnt):
        tasks.append(asyncio.create_task(write(save_queue)))

    for url in all_urls:
        download_queue.put_nowait(url)

    await download_queue.join()
    await save_queue.join()

    for task in tasks:
        task.cancel()

    print(time.perf_counter() - start)


if __name__ == '__main__':
    asyncio.run(main())
