#!/usr/bin/env python3
"""oooooooooouu"""
import asyncio
import random
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    """coroutineeeeeee"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10


if __name__ == "__main__":
    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())
