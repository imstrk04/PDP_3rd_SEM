# Cost attribute of a coffee is enhanced. 
# Wrappee
# Component interface
class Coffee:
    def cost(self):
        pass

# Wrapper
# Concrete component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5

# Represents aggregate relationship between wrapper and wrappee
# Decorator interface
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost()

# Concrete decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 2

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 2

# Client code
simple_coffee = SimpleCoffee()
print("Cost of Simple Coffee:", simple_coffee.cost())

milk_coffee = MilkDecorator(simple_coffee)
print("Cost of Milk Coffee:", milk_coffee.cost())

sugar_milk_coffee = SugarDecorator(milk_coffee)
print("Cost of Sugar Milk Coffee:", sugar_milk_coffee.cost())
