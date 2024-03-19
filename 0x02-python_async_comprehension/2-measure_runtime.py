#!/usr/bin/env python3
"""benchmarking"""
import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """benchmark async comprehension"""
    tasks: List[asyncio.Future[float]] = []
    for _ in range(4):
        task: asyncio.Future[float] = asyncio.ensure_future(
            async_comprehension())
        tasks.append(task)

    start: float = time.time()
    await asyncio.gather(*tasks, return_exceptions=True)
    return time.time() - start


if __name__ == "__main__":
    async def main():
        return await (measure_runtime())

    print(
        asyncio.run(main())
    )
