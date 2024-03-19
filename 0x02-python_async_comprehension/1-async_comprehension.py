#!/usr/bin/env python3
"""async comprehension"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async comprehension"""
    return [i async for i in async_generator()]


if __name__ == "__main__":
    async def main():
        print(await async_comprehension())

    asyncio.run(main())
