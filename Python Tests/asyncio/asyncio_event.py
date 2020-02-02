import asyncio

async def count(kill_timer_event):
    print("One")
    await asyncio.sleep(4)
    kill_timer_event.set()
    print("Two")

async def timer(kill_timer_event):
    counter = 0

    while True:
        if kill_timer_event.is_set():
            break

        print(counter)
        await asyncio.sleep(1)
        counter += 1

async def main():
    kill_timer_event = asyncio.Event()

    counter_task = asyncio.create_task(count(kill_timer_event))
    timer_task = asyncio.create_task(timer(kill_timer_event))
    t = await asyncio.gather(counter_task, timer_task)
    print(f'Completed all tasks?: {all((counter_task.done(), timer_task.done()))}')

if __name__ == "__main__":
    import time

    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
