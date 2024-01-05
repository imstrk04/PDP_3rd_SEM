from inventory_management_system.products.base_product import Product

class Electronics(Product):

    def __init__(self, name, price, category):
        super().__init__(name, price, category)

    def display_info(self):
        display = f"Name of the Electronics is {self.name} and its price is Rs. {self.price}"
        return display