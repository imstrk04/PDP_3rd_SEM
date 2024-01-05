from abc import ABC, abstractmethod

# Template Class
class Sandwich(ABC):
    def make_sandwich(self):
        self.prepare_bread()
        self.add_protein()
        self.add_vegetables()
        self.add_sauce()
        self.wrap_sandwich()

    @abstractmethod
    def prepare_bread(self):
        pass

    @abstractmethod
    def add_protein(self):
        pass

    @abstractmethod
    def add_vegetables(self):
        pass

    @abstractmethod
    def add_sauce(self):
        pass
    @abstractmethod
    def wrap_sandwich(self):
        pass

# Concrete Class 1
class VegSandwich(Sandwich):
    def prepare_bread(self):
        print("Using whole wheat bread")

    def add_protein(self):
        print("Adding paneer as protein")

    def add_vegetables(self):
        print("Adding lettuce, tomato, and cucumber")

    def add_sauce(self):
        print("Adding mayo and mustard")

    def wrap_sandwich(self):
        print("Wrapping the sandwich")

# Concrete Class 2
class NonVegSandwich(Sandwich):
    def prepare_bread(self):
        print("Using multi-grain bread")

    def add_protein(self):
        print("Adding chicken as protein")

    def add_vegetables(self):
        print("Adding lettuce, tomato, and onion")

    def add_sauce(self):
        print("Adding BBQ sauce")

    def wrap_sandwich(self):
        print("Wrapping the sandwich")

# Client Code
def make_and_serve(sandwich):
    sandwich.make_sandwich()

# Example Usage
veg_sandwich = VegSandwich()
non_veg_sandwich = NonVegSandwich()

print("Making Veg Sandwich:")
make_and_serve(veg_sandwich)

print("\nMaking Non-Veg Sandwich:")
make_and_serve(non_veg_sandwich)
