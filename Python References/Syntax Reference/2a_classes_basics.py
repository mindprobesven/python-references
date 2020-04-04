#!/usr/bin/env python3

"""
----------------------------------------------------------------------------------------------------------------
Classes - Basics

- Creating a class
- Class constructor, class attributes, instance attributes, class methods
----------------------------------------------------------------------------------------------------------------
"""

# Class
class Dog:
    # Class attributes. Shared in all instances of the class. Similar to a global.
    class_id = 0

    # Class constructor
    def __init__(self, name, age):  # Class parameters
        # Incrementing a class attribute (class_id) when a class instance is created
        Dog.class_id += 1

        # Setting instance attributes values
        self.name = name
        self.age = age

    # Class method
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

# ------------------------------------------------------------------------------------------------------
# Class attributes can be accessed and modified without having to instantiate the class
print(Dog.class_id)                     # OUTPUT: 0
print("-----" * 10)

# ------------------------------------------------------------------------------------------------------
# Instantiating a class with parameters
LEIKA = Dog('Leika', 3)
print(f"Class ID: {LEIKA.class_id}")    # OUTPUT: Class ID: 1
SANDY = Dog('Sandy', 8)
print(f"Class ID: {SANDY.class_id}")    # OUTPUT: Class ID: 2
print("-----" * 10)

# ------------------------------------------------------------------------------------------------------
# Using get and set methods
print(LEIKA.get_name())                 # OUTPUT: Leika
LEIKA.set_name("Super Leika")
print(LEIKA.get_name())                 # OUTPUT: Super Leika
print("-----" * 10)
