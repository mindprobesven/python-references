#!/usr/bin/env python3

import asyncio

async def hello(name: str) -> str:
    print("Hello, ")
    await asyncio.sleep(1)
    print(name)
    return "Done"

res = asyncio.run(hello("Sven"))
print(res)
res = asyncio.run(hello("Barbara"))
print(res)
