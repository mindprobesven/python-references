#!/usr/bin/env python3

# Class instantiates itself and the class instanace class_instantiate_at_import_instance can be imported from any module

class ClassInstantiateAtImport:
    def __init__(self):
        print("Class ClassInstantiateAtImport instantiated")
        self._data = []

    def add_data(self, value):
        self._data.append(value)

    def get_data(self):
        return self._data

class_instantiate_at_import_instance = ClassInstantiateAtImport()
