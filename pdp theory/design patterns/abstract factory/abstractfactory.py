from abc import ABC, abstractmethod

# Abstract Product: Pizza
class Pizza(ABC):
    def prepare(self):
        pass

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass

# Concrete Product: Cheese Pizza
class CheesePizza(Pizza):
    def prepare(self):
        print("Preparing Cheese Pizza")

    def bake(self):
        print("Baking Cheese Pizza")

    def cut(self):
        print("Cutting Cheese Pizza")

    def box(self):
        print("Boxing Cheese Pizza")

# Abstract Factory
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

# Concrete Factory: NY Pizza Ingredient Factory
class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return "Thin Crust Dough"

    def create_sauce(self):
        return "Marinara Sauce"

# Concrete Creator
class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        ingredient_factory = NYPizzaIngredientFactory()

        if pizza_type == "cheese":
            return CheesePizza(ingredient_factory)
        # You can add more pizza types here

# Modified Concrete Product: Cheese Pizza
class CheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory
        self.dough = None
        self.sauce = None

    def prepare(self):
        print("Preparing Cheese Pizza")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        print(f"  Dough: {self.dough}")
        print(f"  Sauce: {self.sauce}")

# Updated Client Code
if __name__ == "__main__":
    ny_pizza_store = NYPizzaStore()

    cheese_pizza = ny_pizza_store.order_pizza("cheese")
