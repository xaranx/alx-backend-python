#!/usr/bin/env python3
"""
Defines a function `wait_n` which returns the list of all the delays
(float values). The list of the delays should be in ascending order.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """waiting for you ..."""
    tasks = []
    for _ in range(n):
        task = asyncio.ensure_future(task_wait_random(max_delay))
        tasks.append(task)

    res = await asyncio.gather(*tasks, return_exceptions=True)
    return sorted(res)


if __name__ == "__main__":
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
