#!/usr/bin/env python3

"""

Experimenting with:

- Global object design pattern
- Singleton design pattern
- @classmethod
- __init__.py setup
- __main__.py setup to run a app as package (e.g. python -m myapp)

"""

from classes.class_classmethods import ClassMethods
from classes.class_instantiate_at_import import class_instantiate_at_import_instance
from classes.class_singleton import ClassSingleton
from classes.class_another_singleton import ClassAnotherSingleton
from classes.class_singleton_subclass import Logger

from some_class import SomeClass

class App:
    def __init__(self):
        print("Started app")

        ClassMethods.add_data(1)
        print(f"ClassMethods: {ClassMethods.get_data()}")
        print('*' * 50)

        # ------------------------------------------------------------------------------------

        class_instantiate_at_import_instance.add_data(1)
        print(f"class_instantiate_at_import_instance: {class_instantiate_at_import_instance.get_data()}")
        print('*' * 50)

        # ------------------------------------------------------------------------------------

        class_singleton_1 = ClassSingleton(111)
        print(class_singleton_1)
        class_singleton_1.name()
        class_singleton_1.add_data(1)
        print(class_singleton_1.get_data())

        class_singleton_2 = ClassSingleton(222)
        print(class_singleton_2)
        class_singleton_2.name()
        class_singleton_2.add_data(2)
        print(class_singleton_2.get_data())

        print('Are they the same object?', class_singleton_1 is class_singleton_2)
        print('*' * 50)

        # ------------------------------------------------------------------------------------

        class_another_singleton_1 = ClassAnotherSingleton(333)
        print(class_another_singleton_1)
        class_another_singleton_1.name()
        class_another_singleton_1.add_data(11)
        print(class_another_singleton_1.get_data())

        class_another_singleton_2 = ClassAnotherSingleton(444)
        print(class_another_singleton_2)
        class_another_singleton_2.name()
        class_another_singleton_2.add_data(22)
        print(class_another_singleton_2.get_data())

        print('Are they the same object?', class_another_singleton_1 is class_another_singleton_2)
        print('*' * 50)

        # ------------------------------------------------------------------------------------

        self.logger = Logger(name='Logger-Thread', daemon=True)
        self.logger2 = Logger(name='Logger-Thread', daemon=True)

        print(self.logger)
        print(self.logger2)

        self.logger2.start_logger()

        # ------------------------------------------------------------------------------------

        SomeClass()

        while True:
            pass

if __name__ == "__main__":
    App()
