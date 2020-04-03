#!/usr/bin/env python3

import time

def measure_time(func):
    def wrapper(*args):
        t = time.time()
        func(*args)
        print(f"Took {str(time.time() - t)} seconds.")
    return wrapper

@measure_time
def doStuff(n):
    time.sleep(n)

if __name__ == "__main__":
    doStuff(2)
