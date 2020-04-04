#!/usr/bin/env python3

"""
----------------------------------------------------------------------------------------------------------------
Classes - Encapsulation

- Public, private and protected attributes
----------------------------------------------------------------------------------------------------------------
"""

class Dog:
    def __init__(self, name, age, dog_type):
        # Public attribute
        self.name = name

        # Protected attribute
        # Prevents it to be accessed, unless it is from within a sub-class.
        self._age = age

        # Private attribute
        # Gives a strong suggestion not to touch it from outside the class
        self.__type = dog_type

SANDY = Dog('Sandy', 5, 'Schlangenhund')

# ------------------------------------------------------------------------------------------------------
# Accessing a public attribute
print(f"Name: {SANDY.name}")            # Can be accessed publicly
print("-----" * 10)

# ------------------------------------------------------------------------------------------------------
# Accessing a protected attribute
print(f"Age: {SANDY._age}")             # pylint warns: Access to a protected member _age of a client class
print("-----" * 10)

# ------------------------------------------------------------------------------------------------------
# Accessing a private attribute
try:
    print(f"Type: {SANDY.__type}")      # Raises AttributeError: AttributeError: 'Dog' object has no attribute '__type'
except Exception as err:
    print(f"Error: {type(err).__name__} : {err}")

"""
NOTE:
Python performs name mangling of private variables.
Every member with double underscore will be changed to _object._class__variable.
If so required, it can still be accessed from outside the class, but the practice should be refrained.
"""
print(f"Type: {SANDY._Dog__type}")      # Like this, the private attribute can still be accessed from outside the class
