#!/usr/bin/env python3

import sys
import time
import asyncio
import threading
from threading import Thread

def start_loop(loop):
    # 3. Set and run the event loop inside the thread
    asyncio.set_event_loop(loop)
    print("Event loop started")
    loop.run_forever()

    # 9. This executes after the event loop is stopped
    print("Event loop stopped")
    print(f"Loop: {loop}") # loop running = false, closed = false

    # 10. Close the event loop
    loop.close()
    print("Closed event loop")
    print(f"Loop: {loop}") # loop running = false, closed = true

    # 11. Since the event loop is finished, the thread will also finish and exit
    print("Thread finished! Exit thread.")

def regular_function(x):
    print(f"Regular - Start work {x}")
    time.sleep(x)
    print(f"Regular - Finished work {x}")

async def coroutine_function(x):
    print(f"Coroutine - Start work {x}")
    await asyncio.sleep(x)
    print(f"Coroutine - Finished work {x}")

def add_message(loop):
    print("Add workers")
    # 6. Regular functions can be called and execute in order like a task queue, but they can block the event loop thread
    # loop.call_soon_threadsafe(regular_function, 0.25)
    # loop.call_soon_threadsafe(regular_function, 0.25)

    # 7. Coroutine functions can be called and executed in parallel. These execute after the regular funcions above finish
    asyncio.run_coroutine_threadsafe(coroutine_function(1), loop)
    asyncio.run_coroutine_threadsafe(coroutine_function(3), loop)

if __name__ == "__main__":
    new_loop_running = True
    counter = 0

    try:
        # 1. Create a new event loop
        new_loop = asyncio.new_event_loop()

        # 2. Create a new daemon thread and pass to it the new event loop
        t = Thread(name="MessagesThread", target=start_loop, args=(new_loop,), daemon=True)
        t.start()

        # 4. The main thread is running a non-blocking while loop which can control the event loop running in the daemon thread
        while True:
            if counter == 6:
                # 8. To stop the event loop and thread running it, we first cancel all coroutine tasks running in the event loop and then stop it
                """
                task_list = enumerate(asyncio.all_tasks(new_loop))
                for task in task_list:
                    print(task)
                    print(str(task[1]).split(None, 3)[1:3])
                    task[1].cancel()
                """
                new_loop_running = False
                asyncio.gather(*asyncio.all_tasks(new_loop)).cancel()
                print("Cancelled coroutine tasks")
                new_loop.stop()

            # 5. Tasks can be added to the event loop daemon thread interactively
            if new_loop.is_running() and new_loop_running:
                add_message(new_loop)

            print(f"{'-' * 80} {counter}")
            for thread in threading.enumerate():
                print(thread)
            print(f"Running tasks in daemon thread: {len(asyncio.all_tasks(new_loop))}")
            print(f"{'-' * 80} {counter}")

            counter += 1
            time.sleep(1.0)

    except KeyboardInterrupt:
        sys.exit('\nInterrupted by user')
