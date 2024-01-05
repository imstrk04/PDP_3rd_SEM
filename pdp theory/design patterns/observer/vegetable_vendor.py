from abc import ABC, abstractmethod

class VegetableSubject(ABC):

    @abstractmethod
    def attach(self, obs):
        pass

    @abstractmethod
    def detach(self, obs):
        pass

    @abstractmethod
    def notify(self, obs):
        pass

class VegetableObserver(ABC):

    @abstractmethod
    def update_availability(self, vegetables):
        pass

    @abstractmethod
    def confirm_payment(self, order_amt):
        pass

    @abstractmethod
    def notify_order_ready(self, delivery_time):
        pass


class Vegetable_System(VegetableSubject):
    
    def __init__(self):
        self.obs_list = []
        self.vegetables_availability = {}
        self.orders = []
        self.total_sales = 0
        

'''
class Veg_Info:

    def __init__(self):
        pass

    def update(self, veg):
        print(veg)
'''

dayStock = {}
n = int(input("Enter number of vegetables: "))
for i in range(n):
    name = input("Enter name of the vegetable: ")
    qty = int(input(f"Enter {name} quantity: "))
    price = int(input(f"Enter {name} price: "))
    dayStock[name] = [qty, price]

veg_shop = Vegetable_Shop(dayStock)
observer = Veg_Info()
veg_shop.attach(observer)
print(veg_shop)