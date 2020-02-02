class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name)
        print(self.age)

    def get_dog_info(self):
        print(self.name)
        print(self.age)

class Breed:
    def __init__(self, breed):
        self.breed = breed

    def get_breed(self):
        print(self.breed)

class SpecialDog(Dog):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = Breed(breed)

    # Overwrites parent method with same name
    def sit(self):
        print(self.name)
        print(self.age)
        self.breed.get_breed()

MY_DOG = Dog('Leika', 3)
MY_DOG.sit()
print("-------")
MY_SPECIAL_DOG = SpecialDog('Sandy', '9', 'Schlangenhund')
MY_SPECIAL_DOG.get_dog_info()
print("-------")
MY_SPECIAL_DOG.breed.get_breed()
print("-------")
MY_SPECIAL_DOG.sit()
