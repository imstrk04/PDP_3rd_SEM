from abc import ABC, abstractmethod
import random

# Product
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

# Creator
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

# Concrete Creators
class RandomFactory(AnimalFactory):
    def create_animal(self):
        animal_types = [Dog, Cat, Duck]
        random_animal = random.choice(animal_types)
        return random_animal()

class BalancedFactory(AnimalFactory):
    def create_animal(self, animal_type):
        if animal_type == 'Dog':
            return Dog()
        elif animal_type == 'Cat':
            return Cat()
        elif animal_type == 'Duck':
            return Duck()
        else:
            raise ValueError("Invalid animal type")

# Client code
def main():
    random_animal_factory = RandomFactory()
    animal1 = random_animal_factory.create_animal()
    print(f"Random Animal says: {animal1.speak()}")

    balanced_animal_factory = BalancedFactory()
    animal2 = balanced_animal_factory.create_animal('Dog')
    print(f"Balanced Animal says: {animal2.speak()}")

if __name__ == "__main__":
    main()
