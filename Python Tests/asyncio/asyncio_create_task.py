#!/usr/bin/env python3

import asyncio

async def foo(numbers: list) -> list:
    await asyncio.sleep(1)
    return list(reversed(numbers))

async def main() -> list:
    t = asyncio.create_task(foo([1, 2, 3]))
    await t
    print(f't: type {type(t)}')
    print(f't done: {t.done()}')
    return t

t = asyncio.run(main())
print(t.result())
