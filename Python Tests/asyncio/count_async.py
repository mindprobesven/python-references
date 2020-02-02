import asyncio

async def count():
    print("One")
    await asyncio.sleep(5)
    print("Two")

async def timer(ct):
    counter = 0

    while True:
        print(counter)

        """ for a in asyncio.Task.all_tasks():
            print(str(a).split(None, 3)[1:3]) """

        if ct.done():
            print("Done!")
            break

        await asyncio.sleep(1)
        counter += 1

async def main():
    counter_task = asyncio.create_task(count())
    timer_task = asyncio.create_task(timer(counter_task))
    t = await asyncio.gather(counter_task, timer_task)
    print(f't Completed all?: {all((counter_task.done(), timer_task.done()))}')

if __name__ == "__main__":
    import time

    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
