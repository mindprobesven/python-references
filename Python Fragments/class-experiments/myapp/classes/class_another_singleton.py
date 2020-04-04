#!/usr/bin/env python3

from common.singleton import singleton

@singleton
class ClassAnotherSingleton:
    def __init__(self, text):
        print("Class ClassAnotherSingleton instantiated once")
        self._data = []
        print(text)

    @classmethod
    def name(cls):
        print(cls.__name__)

    def add_data(self, value):
        self._data.append(value)

    def get_data(self):
        return self._data
