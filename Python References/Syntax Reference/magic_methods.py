#!/usr/bin/env python3

"""
----------------------------------------------------------------------------------------------------------------
Magic Methods

- Magic methods are most frequently used to define overloaded behaviours of predefined operators in Python
----------------------------------------------------------------------------------------------------------------
"""

class Person:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    # Overriding the __str__() method
    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}\nSalary: {self.salary}"

    # Overloading the + operator
    def __add__(self, other_person):
        sum_salary = self.salary + other_person.salary
        return sum_salary

if __name__ == "__main__":
    sven = Person(first_name='Sven', last_name='Kohn', salary=100000)
    barbara = Person(first_name='Barbara', last_name='Massari', salary=80000)

    # ------------------------------------------------------------------------------------------------------
    # Overriding the __str__() method in the Person class can return a string representation of its object. Pure magic!
    print(sven)
    print(barbara)
    # Magic methods can also be called directly. This is not recommended though.
    print(Person.__str__(barbara))

    # ------------------------------------------------------------------------------------------------------
    # Overloading the + operator to add the salary values of two Person class instances. Again, magic!
    total_salary = sven + barbara
    # Magic methods can also be called directly. This is not recommended though.
    total_salary = sven.__add__(barbara)
    print(f"Total salary: {total_salary}")

    # ------------------------------------------------------------------------------------------------------
    # Lists all magic methods inherited by a class
    print(dir(sven))
    # Magic methods can also be called directly. This is not recommended though.
    print(sven.__dir__())
