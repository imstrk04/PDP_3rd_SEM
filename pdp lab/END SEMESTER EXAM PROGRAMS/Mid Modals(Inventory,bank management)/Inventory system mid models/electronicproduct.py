from productclass import product

class electronic_product(product):

    def __init__(self,name,brand,**kwargs):
        super().__init__(name,**kwargs)
        self.brand=brand

    def display(self):
        return f'{self.name},{self.brand}'

