#!/usr/bin/env python3

import asyncio
import sys
import logging
import random

logging.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)
logger = logging.getLogger()
logging.getLogger("chardet.charsetprober").disabled = True

async def produce(number, queue):
    await queue.put(number)
    logger.info("Producer added %s to queue. Queue size = %i +", number, queue.qsize())
    print(queue)

async def consume(name, queue):
    while True:
        await asyncio.sleep(3)
        number = await queue.get()
        logger.info("Consumer %s got %s from queue. Queue size = %i", name, number, queue.qsize())
        queue.task_done()

async def main():
    counter = 0
    queue = asyncio.Queue(maxsize=10)

    consumers = [asyncio.create_task(consume(n, queue)) for n in range(3)]
    asyncio.gather(*consumers)

    while True:
        producers = [asyncio.create_task(produce(random.randint(0, 10), queue)) for _ in range(4)]
        asyncio.gather(*producers)

        print(counter)
        await asyncio.sleep(1)
        counter += 1

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit('\nInterrupted by user')
