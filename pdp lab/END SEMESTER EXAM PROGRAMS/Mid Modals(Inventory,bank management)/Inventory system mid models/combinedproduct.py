from electronicproduct import electronic_product
from clothingproduct import clothing_product

class combined_product(electronic_product,clothing_product):

    def __init__(self,name,brand,size,qty,**kwargs):
        super().__init__(name,brand=brand,size=size,**kwargs)
        self.qty=qty

    def display(self):
        return f'{self.name},{self.brand},{self.size},{self.qty}'



        
