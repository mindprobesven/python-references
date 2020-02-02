import sys
import asyncio
import threading
from playsound import playsound

def play(play_completed_event):
    print("Before playing sound")
    playsound('/Users/svenkohn/Desktop/Python/Python%20Tests/asyncio/clearly.mp3')
    print("After playing sound")
    play_completed_event.set()

async def play_sound(play_completed_event):
    print("Before thread start")
    x = threading.Thread(target=play, args=(play_completed_event,), daemon=True)
    x.start()
    print("After thread start")

async def main():
    counter = 0
    play_completed_event = asyncio.Event()

    player_task = asyncio.create_task(play_sound(play_completed_event))

    while True:
        if play_completed_event.is_set():
            print("Before create play sound task")
            play_completed_event.clear()
            player_task = asyncio.create_task(play_sound(play_completed_event))
            print("After create play sound task")

        print(counter)
        await asyncio.sleep(1)
        counter += 1

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit('\nInterrupted by user')
