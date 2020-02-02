#!/usr/bin/env python3

import asyncio

async def foo(numbers: list) -> list:
    await asyncio.sleep(1)
    return list(reversed(numbers))

async def main() -> list:
    t1 = asyncio.create_task(foo([1, 2, 3]))
    t2 = asyncio.create_task(foo([5, 6, 7]))
    t = await asyncio.gather(t1, t2)
    print(f't Completed all?: {all((t1.done(), t2.done()))}')
    return t

t = asyncio.run(main())
print(t)
