#!/usr/bin/env python3
"""
Defines a function `wait_n` which returns the list of all the delays
(float values). The list of the delays should be in ascending order.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """waiting for you ..."""
    tasks = []
    for _ in range(n):
        task = asyncio.ensure_future(wait_random(max_delay))
        tasks.append(task)

    res = await asyncio.gather(*tasks, return_exceptions=True)
    return sorted(res)


if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
