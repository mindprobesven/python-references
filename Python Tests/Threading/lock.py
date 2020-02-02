"""
To prevent race conditions on shared memory (e.g. self.message in the Pipeline class), use Lock .acquire and .release
to control swaping between thread activity.
"""

import logging
import threading
import concurrent.futures
import random

SENTINEL = object()

def producer(pipeline):
    """Pretend we're getting a message from the network."""
    for index in range(10):
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        # 2. The producer gets a burst of 10 messages and sends them to the pipeline ony by one
        pipeline.set_message(message, "Producer")

    pipeline.set_message(SENTINEL, "Producer")

def consumer(pipeline):
    """Pretend we're saving a number in the database."""
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            logging.info("Consumer storing message: %s", message)

class Pipeline:
    """
    Class to allow a single element pipeline between producer and consumer.
    """
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        # 1. The consumer thread is locked first. The consumer needs to wait until the first message is present.
        self.consumer_lock.acquire()

    def get_message(self, name):
        logging.debug("%s:about to acquire getlock", name)
        # 6. The consumer thread is locked again after receiving the first message.
        # 9. The consumer thread is locked again to wait for the next message to be present.
        self.consumer_lock.acquire()
        logging.debug("%s:have getlock", name)
        message = self.message
        logging.debug("%s:about to release setlock", name)
        # 7. The producer thread is released to set the second message
        self.producer_lock.release()
        logging.debug("%s:setlock released", name)
        # 8. The first message is returned and stored
        return message

    def set_message(self, message, name):
        logging.debug("%s:about to acquire setlock", name)
        # 3. The producer thread is locked, then sets self.message the first time.
        # 5. The producer thread gets the second message, but has to wait until the first message is stored by the consumer.
        # 10. The producer thread locks again and sets the second message.
        self.producer_lock.acquire()
        logging.debug("%s:have setlock", name)
        self.message = message
        logging.debug("%s:about to release getlock", name)
        # 4. The consumer thread is released because the first message is ready
        # 11. The consumer thread is released to store the second message
        self.consumer_lock.release()
        logging.debug("%s:getlock released", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)

    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)
