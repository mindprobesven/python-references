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

    # Non-deamon threads - the program will wait for the threads to complete before it exits
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    logging.info("Main    : all done")

    time.sleep(3.0)
    print("-" * 50)

    # join - tell one thread to wait for another thread to finish
    logging.info("Main    : before creating thread")
    y = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info("Main    : before running thread")
    y.start()
    logging.info("Main    : wait for the thread to finish")
    y.join()
    logging.info("Main    : all done")

    time.sleep(1.0)
    print("-" * 50)

    # Deamon threads - are just killed wherever they are when the program is exiting
    # This deamon thread does not have enough time to finish before the program exits
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    logging.info("Main    : all done")
