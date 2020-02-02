#!/usr/bin/env python3

import asyncio

async def worker(my_semaphore):
    async with my_semaphore:
        # await my_semaphore.acquire()
        print("Successfully acquired the semaphore")
        await asyncio.sleep(3)
        print("Releasing Semaphore")
        # my_semaphore.release()

async def main():
    my_semaphore = asyncio.Semaphore(value=2)
    tasks = [worker(my_semaphore) for _ in range(12)]
    await asyncio.gather(*(tasks))
    print("Main Coroutine")

asyncio.run(main())
