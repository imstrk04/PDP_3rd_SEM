import pickle

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Name: {self.name}, Price: ${self.price}")

class Electronics(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

    def display_info(self):
        super().display_info()
        print(f"Brand: {self.brand}")

class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

class InventoryManager:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)

    def save_inventory(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.inventory, file)

    def load_inventory(self, filename):
        with open(filename, 'rb') as file:
            self.inventory = pickle.load(file)

# Example usage
if __name__ == "__main__":
    # Classes, Inheritance, and Polymorphism
    laptop = Electronics("Laptop", 1200, "Dell")
    shirt = Clothing("Shirt", 30, "Medium")

    laptop.display_info()
    shirt.display_info()

    # Diamond Problem
    d_obj = D()
    d_obj.show()

    # Serialization
    manager = InventoryManager()
    manager.add_product(laptop)
    manager.add_product(shirt)

    manager.save_inventory("inventory_data.pkl")

    new_manager = InventoryManager()
    new_manager.load_inventory("inventory_data.pkl")
    print("Loaded Inventory:")
    for item in new_manager.inventory:
        item.display_info()
