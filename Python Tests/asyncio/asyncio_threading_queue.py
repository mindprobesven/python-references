#!/usr/bin/env python3

import sys
import os
import time
import asyncio
import threading
from threading import Thread

def start_loop(loop):
    asyncio.set_event_loop(loop)
    print("Event loop started")
    loop.run_forever()

    print("Event loop stopped")
    loop.close()
    print("Thread finished! Exit thread.")

def create_consumers(number):
    for n in range(1, number + 1):
        print(f"Creating consumer {n}")
        asyncio.run_coroutine_threadsafe(consumer(n), new_loop)

async def consumer(consumer_id):
    while True:
        await asyncio.sleep(0.01)
        if not queue.empty():
            data = await queue.get()
            print(f"Consumer {consumer_id} got {data} from queue. Queue size: {queue.qsize()}")
            queue.task_done()

            if data != "cancel":
                await write_data(data)
            elif data == "cancel" and queue.qsize() >= 1:
                break
            elif data == "cancel" and queue.qsize() == 0:
                new_loop.stop()
                break

async def producer(message):
    await queue.put(message)
    print(f"Producer added {message} to queue. Queue size: {queue.qsize()}")

def add_message(message):
    asyncio.run_coroutine_threadsafe(producer(message), new_loop)

async def write_data(data):
    async with consumer_lock:
        global consumed_data
        consumed_data.append(data)

def forced_kill():
    global new_loop_running
    new_loop_running = False

    asyncio.gather(*asyncio.all_tasks(new_loop)).cancel()
    new_loop.stop()

    queue._queue.clear()
    queue._finished.set()
    queue._unfinished_tasks = 0

def safe_kill():
    global new_loop_running
    new_loop_running = False

    for _ in range(max_consumers):
        add_message("cancel")

if __name__ == "__main__":
    counter = 0
    new_loop_running = True
    max_consumers = 2
    consumed_data = list()

    try:
        new_loop = asyncio.new_event_loop()
        queue = asyncio.Queue(maxsize=10, loop=new_loop)
        consumer_lock = asyncio.Lock(loop=new_loop)

        t = Thread(name="MessagesThread", target=start_loop, args=(new_loop,), daemon=True)
        t.start()

        create_consumers(max_consumers)

        while True:
            if counter == 90:
                # forced_kill()
                safe_kill()

            if new_loop.is_running() and new_loop_running:
                for n in range(1, 11):
                    add_message("Sven")

            os.system('clear')
            print(f"{'-' * 80} {counter}")
            for thread in threading.enumerate():
                print(thread)
            print(f"Running tasks in daemon thread: {len(asyncio.all_tasks(new_loop))}")
            # task_list = enumerate(asyncio.all_tasks(new_loop))
            """ for task in asyncio.all_tasks(new_loop):
                print(task) """
            print(queue)
            print(f"Comsumed data: {consumed_data}")
            print(f"{'-' * 80} {counter}")

            counter += 1
            time.sleep(0.001)

    except KeyboardInterrupt:
        sys.exit('\nInterrupted by user')
