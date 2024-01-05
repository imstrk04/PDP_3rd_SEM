from productclass import product

class clothing_product(product):

    def __init__(self,name,size,**kwargs):
        super().__init__(name,**kwargs)
        self.size=size

    def display(self):
        return f'{self.name},{self.size}'

