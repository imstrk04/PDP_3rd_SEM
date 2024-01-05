from inventory_management_system.products.base_product import Product
from inventory_management_system.products.electronics import Electronics
from inventory_management_system.products.clothing import Clothing

class Diwali(Electronics, Clothing):
    
    def __init__(self, name, price, category):
        super().__init__(name, price, category)
    
    def display_info(self):
        #display = f"Its Diwali Time, You get {self.name} for Rs. {self.price}"
        #return display 
        return super().display_info()

