#!/usr/bin/env python3

from classes.class_classmethods import ClassMethods
from classes.class_instantiate_at_import import class_instantiate_at_import_instance
from classes.class_singleton import ClassSingleton
from classes.class_another_singleton import ClassAnotherSingleton

class SomeClass:
    def __init__(self):
        print("Started SomeClass")

        ClassMethods.add_data(2)
        print(f"ClassMethods: {ClassMethods.get_data()}")
        print('*' * 50)

        # ------------------------------------------------------------------------------------

        class_instantiate_at_import_instance.add_data(2)
        print(f"class_instantiate_at_import_instance: {class_instantiate_at_import_instance.get_data()}")
        print('*' * 50)

        class_singleton_1 = ClassSingleton(333)
        print(class_singleton_1)
        class_singleton_1.name()
        class_singleton_1.add_data(3)
        print(class_singleton_1.get_data())

        class_singleton_2 = ClassSingleton(444)
        print(class_singleton_2)
        class_singleton_2.name()
        class_singleton_2.add_data(4)
        print(class_singleton_2.get_data())

        print('Are they the same object?', class_singleton_1 is class_singleton_2)
        print('*' * 50)

        # ------------------------------------------------------------------------------------

        class_another_singleton_1 = ClassAnotherSingleton(555)
        print(class_another_singleton_1)
        class_another_singleton_1.name()
        class_another_singleton_1.add_data(33)
        print(class_another_singleton_1.get_data())

        class_another_singleton_2 = ClassAnotherSingleton(666)
        print(class_another_singleton_2)
        class_another_singleton_2.name()
        class_another_singleton_2.add_data(44)
        print(class_another_singleton_2.get_data())

        print('Are they the same object?', class_another_singleton_1 is class_another_singleton_2)
        print('*' * 50)

        # ------------------------------------------------------------------------------------

        """ Logger.addStuff(2)
        Logger.printStuff()
        Logger.start_stats_monitor() """

        """ print(Logger)
        Logger.addInstanceStuff(5)
        print(Logger.instance_data)

        AnotherClass() """
