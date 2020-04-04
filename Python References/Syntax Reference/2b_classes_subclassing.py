#!/usr/bin/env python3

"""
----------------------------------------------------------------------------------------------------------------
Classes - Subclassing

- Creating a subclass
- Overwriting class methods
----------------------------------------------------------------------------------------------------------------
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self) -> tuple:
        return self.name, self.age

class Breed:
    def __init__(self, breed):
        self.breed = breed

    def get_breed(self) -> str:
        return self.breed

class SpecialDog(Dog):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        # Instantiating the class (Breed) inside a class and calling the method [get_breed()] of that class
        self.breed = Breed(breed).get_breed()

    # Overwrites parent class (Dog) method (get_info) because it has the same method name
    def get_info(self) -> tuple:
        return self.name, self.age, self.breed

# ------------------------------------------------------------------------------------------------------
# Instantiating a class object (Dog)
LEIKA = Dog('Leika', 3)
print(f"Dog name: {LEIKA.get_info()[0]}")           # OUTPUT: Dog name: Leika
print(f"Dog age: {LEIKA.get_info()[1]}")            # OUTPUT: Dog age: 3
print("-----" * 10)

# ------------------------------------------------------------------------------------------------------
# Instantiating a class object (SpecialDog) which subclasses (Dog)
SANDY = SpecialDog('Sandy', 5, 'Schlangenhund')
print(f"Dog name: {SANDY.get_info()[0]}")           # OUTPUT: Dog name: Sandy
print(f"Dog age: {SANDY.get_info()[1]}")            # OUTPUT: Dog age: 5
print(f"Dog type: {SANDY.get_info()[2]}")           # OUTPUT: Dog type: Schlangenhund
print("-----" * 10)
