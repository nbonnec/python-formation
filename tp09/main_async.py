#!/usr/bin/env python

import asyncio


async def add(a: int, b: int) -> int:
    await asyncio.sleep(0.5)
    return a + b


async def main():
    # print('Hello ...')
    # await asyncio.sleep(1)
    # print('... World!')
    # r = add(1, 2)
    all_r = [add(1, 2), add(1, 2), add(1, 2)]
    r = await asyncio.gather(*all_r)
    print(r)


if __name__ == '__main__':
    asyncio.run(main())
