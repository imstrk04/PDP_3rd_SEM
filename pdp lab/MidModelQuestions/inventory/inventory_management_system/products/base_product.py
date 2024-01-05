from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display_info(self):
        display = f"Name of the product is {self.name} and its price is Rs. {self.price}"
        return display