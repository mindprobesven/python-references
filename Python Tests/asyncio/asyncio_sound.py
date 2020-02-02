import asyncio
import threading
import time
from playsound import playsound

def play(kill_main_event):
    print("Before playing sound")
    playsound('/Users/svenkohn/Desktop/Python/Python%20Tests/asyncio/clearly.mp3')
    print("After playing sound")
    kill_main_event.set()

async def play_sound(kill_main_event):
    print("Before thread start")
    x = threading.Thread(target=play, args=(kill_main_event,), daemon=True)
    x.start()
    print("After thread start")

async def timer(kill_main_event):
    counter = 0

    while True:
        if kill_main_event.is_set():
            print("Killed main task")
            break

        print(counter)
        await asyncio.sleep(1)
        counter += 1

async def main():
    kill_main_event = asyncio.Event()

    player_task = asyncio.create_task(play_sound(kill_main_event))
    timer_task = asyncio.create_task(timer(kill_main_event))
    t = await asyncio.gather(player_task, timer_task)
    print(f't Completed all?: {all((player_task.done(), timer_task.done()))}')

if __name__ == "__main__":
    import time
    import sys

    s = time.perf_counter()

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit('\nInterrupted by user')

    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
