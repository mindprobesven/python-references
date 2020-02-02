import concurrent.futures
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    # ----------- Starting a group of threads the hard way
    threads = list()
    for index in range(3):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)

    time.sleep(2.0)
    print("-" * 50)

    # ----------- Starting a group of threads the easier way with ThreadPoolExecutor
    # The end of the with block causes the ThreadPoolExecutor to do a .join() on each of the threads in the pool automatically
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        # using map iterable
        executor.map(thread_function, range(3))

        # using submit
        executor.submit(thread_function, 3)
        executor.submit(thread_function, 4)
        executor.submit(thread_function, 5)
