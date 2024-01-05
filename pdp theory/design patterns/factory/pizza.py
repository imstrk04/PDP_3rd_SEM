# Product
class Pizza:
    def prepare(self):
        pass

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass

# Concrete Product
class CheesePizza(Pizza):
    def prepare(self):
        print("Preparing Cheese Pizza")

    def bake(self):
        print("Baking Cheese Pizza")

    def cut(self):
        print("Cutting Cheese Pizza")

    def box(self):
        print("Boxing Cheese Pizza")

# Creator
class PizzaStore:
    def create_pizza(self, pizza_type):
        raise NotImplementedError

    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

# Concrete Creator
class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return CheesePizza()
        # You can add more pizza types here

# Client code
if __name__ == "__main__":
    ny_pizza_store = NYPizzaStore()

    cheese_pizza = ny_pizza_store.order_pizza("cheese")
    # You can order more pizza types here
