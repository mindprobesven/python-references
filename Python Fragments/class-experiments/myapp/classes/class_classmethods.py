#!/usr/bin/env python3

# Using a class directly without instantiating it

class ClassMethods:
    _class_data = []

    @classmethod
    def add_data(cls, value):
        cls._class_data.append(value)

    @classmethod
    def get_data(cls):
        return cls._class_data
