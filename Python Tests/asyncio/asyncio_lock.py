#!/usr/bin/env python3

import asyncio

async def worker(lock):
    async with lock:
        print("Successfully acquired the lock")
        await asyncio.sleep(3)
        print("Releasing lock")

async def main():
    lock = asyncio.Lock()
    tasks = [worker(lock) for _ in range(12)]
    await asyncio.gather(*(tasks))
    print("Main Coroutine")

asyncio.run(main())
