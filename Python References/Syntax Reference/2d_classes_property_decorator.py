#!/usr/bin/env python3

"""
----------------------------------------------------------------------------------------------------------------
Classes - Property Decorator

- Accessing and modifying private instance attributes using the property decorator and function overloading
----------------------------------------------------------------------------------------------------------------
"""

class Person:
    def __init__(self):
        self.__name = ''                # A private instance attribute

    @property                           # This is the getter
    def name(self):
        print("Calling getter...")
        return self.__name

    @name.setter                        # This is the setter
    def name(self, value):
        print("Calling setter...")
        self.__name = value

    @name.deleter                       # This is the deleter
    def name(self):
        print("Calling deleter...")
        del self.__name

if __name__ == "__main__":
    sven = Person()

    # This calls the setter
    sven.name = 'Sven'
    print("-----" * 10)

    # This calls the getter
    print(f"Name: {sven.name}")         # OUTPUT: Name: Sven
    print("-----" * 10)

    # This calls the deleter
    del sven.name
    print("-----" * 10)

    print(f"Name: {sven.name}")         # OUTPUT: AttributeError: 'Person' object has no attribute '_Person__name'
