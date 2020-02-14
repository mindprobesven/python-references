#!/usr/bin/env python3

import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)s) %(message)s',)

class MyThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None):
        super().__init__(group=group, target=target, name=name)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug('running with %s and %s', self.args, self.kwargs)

if __name__ == '__main__':
    for i in range(3):
        t = MyThread(args=(i,), kwargs={'a':1, 'b':2})
        t.start()
