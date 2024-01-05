from abc import ABC, abstractmethod

#Component
class Beverage(ABC):

    @abstractmethod
    def cost(self):
        ...

#Concrete Component 1
class Decaf(Beverage):
    
    def cost(self):
        return 2

#Concrete Component 2
class Espresso(Beverage):

    def cost(self):
        return 1

#Decorator
class AddOnDecorator(Beverage):

    def __init__(self, beverage):
        self.beverage = beverage
    
    def cost(self):
        return self.beverage.cost()

#Concrete Decorator 1
class Caramel(AddOnDecorator):

    def cost(self):
        return self.beverage.cost() + 2

#Concrete Decorator 2
class Soy(AddOnDecorator):

    def cost(self):
        return self.beverage.cost() + 1
    
if __name__ == '__main__':
    decaf = Decaf()
    print("Cost of Decaf: Rs.", decaf.cost())
    caramel_decaf = Caramel(decaf)
    print("Cost of Caramel Decaf: Rs.",caramel_decaf.cost())
    soy_caramel_decaf = Soy(caramel_decaf)
    print("Cost of Soy Caramel Decaf: Rs.", soy_caramel_decaf.cost())
    