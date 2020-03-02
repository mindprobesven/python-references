#!/usr/bin/env python3

import datetime
import asyncio
from threading import Thread

from common.singleton import singleton

class Error(Exception):
    pass

class LoggerError(Error):
    pass

@singleton
class Logger(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        print("Class Logger instantiated once")
        self.stats = {
            'daemon_name': None,
            'thread_name': None,
            'tasks_running': 0,
            'tasks': []
        }

        self.loop = asyncio.new_event_loop()
        self._queue = asyncio.Queue(maxsize=10, loop=self.loop)
        self._max_consumers = 2

        self.start()

    def run(self):
        print("Started thread and event loop")

        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

        self.loop.close()
        print("Logger: Logger thread finished! Exit thread.")

    async def _stats_monitor(self):
        print("Started stats monitor")

        self.stats['daemon_name'] = self.__class__.__name__
        self.stats['thread_name'] = self.name

        while True:
            tasks = []
            tasks_list = asyncio.all_tasks(self.loop)
            for task in tasks_list:
                coro = str(task._coro).split(None, 3)[2].split('_', 1)[1]
                tasks.append(coro)

            self.stats['tasks_running'] = len(tasks)
            self.stats['tasks'] = tasks

            print(self.stats)
            await asyncio.sleep(1.0)

    def _start_stats_monitor(self):
        asyncio.run_coroutine_threadsafe(self._stats_monitor(), self.loop)

    async def _consumer(self, consumer_id: int):
        while True:
            await asyncio.sleep(0.01)
            if not self._queue.empty():
                message, log_type = await self._queue.get()
                time_now = datetime.datetime.now().strftime('%x - %X')
                print(f"Consumer {consumer_id} got {time_now} {message} : {log_type} from queue. Queue size: {self._queue.qsize()}")

                self._queue.task_done()

    def _create_consumers(self):
        for n in range(1, self._max_consumers + 1):
            asyncio.run_coroutine_threadsafe(self._consumer(consumer_id=n), self.loop)

    def start_logger(self):
        try:
            self._create_consumers()
            self._start_stats_monitor()
        except Exception as err:
            print(f"Logger: {err}")
            raise LoggerError("The logger daemon failed to start!")

logger_instance = Logger(name='Logger-Thread', daemon=True)
