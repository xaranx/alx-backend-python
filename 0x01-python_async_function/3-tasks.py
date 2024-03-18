#!/usr/bin/env python3
"""waiting for youuu ..."""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """waiting for youuu"""
    task = asyncio.ensure_future(wait_random(max_delay))
    return task


if __name__ == "__main__":
    async def test(max_delay: int):
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
