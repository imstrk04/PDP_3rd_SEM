from abc import ABC, abstractmethod
import unittest
import threading
#Subject interface
class VegetableVendorSubject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

#Observer Interface
class VegetableObserver(ABC):
    @abstractmethod
    def update_vegetable_availability(self, vegetables):
        pass

    @abstractmethod
    def confirm_payment(self, order_amount):
        pass

    @abstractmethod
    def notify_order_ready(self, delivery_time):
        pass

#Concrete Subject
class VegetableVendorSystem(VegetableVendorSubject):
    def __init__(self):
        self._observers = []
        self._vegetable_availability = {}
        self._orders = []
        self._total_sales = 0

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update_vegetable_availability(self._vegetable_availability)
    
    def update_vegetable_availability(self, vegetables):
        self._vegetable_availability.update(vegetables)
        self.notify_observers()

    def confirm_payment(self, order_amount):
        if order_amount > 100:
            self._total_sales += order_amount
            for observer in self._observers:
                observer.confirm_payment(order_amount)
            self._orders = None
        else:
            raise ValueError("Orders should be placed for more than Rs. 100")


    def place_order(self, order):
        if self._orders is not None:
            self._orders.append(order)
            print(f"Order placed. Order number: {len(self._orders)}")
            for key, val in order.items():
                self._vegetable_availability[key.title()] -= val
            print("Remaining vegetables:", self._vegetable_availability)
        else:
            raise ValueError("Order placement is disabled after payment.")

    def notify_order_ready(self, delivery_time):
        for observer in self._observers:
            observer.notify_order_ready(delivery_time)
    
    def place_order_async(self, order):
        # Perform ordering asynchronously using threads
        order_thread = threading.Thread(target=self.place_order, args=(order,))
        order_thread.start()

    def notify_order_ready_async(self, delivery_time):
        # Perform delivery notification asynchronously using threads
        delivery_thread = threading.Thread(target=self.notify_order_ready, args=(delivery_time,))
        delivery_thread.start()

#Concrete Observer
class CustomerObserver(VegetableObserver):
    def __init__(self):
        self._delivery_time = None

    def update_vegetable_availability(self, vegetables):
        print(f"Available Vegetables: {vegetables}")

    def confirm_payment(self, order_amount):
        print(f"Payment confirmed. Amount: Rs. {order_amount}")

    def notify_order_ready(self, delivery_time):
        print(f"Your order is ready. It will be delivered at {delivery_time}")
        self._delivery_time = delivery_time


class VendorObserver(VegetableObserver):
    def __init__(self):
        self._delivery_time = None

    def update_vegetable_availability(self, vegetables):
        pass

    def confirm_payment(self, order_amount):
        print(f"Payment received from customer. Amount: Rs. {order_amount}")

    def notify_order_ready(self, delivery_time):
        print(f"Order ready for delivery at {delivery_time}. Notify customer.")
        self._delivery_time = delivery_time


#Iterator Pattern
class Iterable:
    
    def create_iterator(self):
        pass

    def append(self, item):
        pass

class Iterator:
    
    def has_next(self):
        pass
    def next(self):
        pass

class ObserversList(Iterable):
    def __init__(self):
        self._observers = []
    
    def create_iterator(self):
        return ObserversListIterator(self)

    def append(self, obs):
        self._observers.append(obs)

class ObserversListIterator(Iterator):

    def __init__(self, iterable):
        self._iterable = iterable
        self._index = 0
    
    def has_next(self):
        return self._index < len(self._iterable._observers)

    def next(self):
        if self.has_next():
            value = self._iterable._observers[self._index]
            self._index += 1
        else:
            raise StopIteration("No more Elements")

class TestVegetableVendorSystem(unittest.TestCase):

    def setUp(self):
        self.vendor_system = VegetableVendorSystem()
        self.stock = {"Tomato": 50, "Carrot": 50, "Spinach": 50, "Onion": 50, "Garlic": 50}
        self.customer_observer = CustomerObserver()
        self.vendor_observer = VendorObserver()
        self.vendor_system.register_observer(self.customer_observer)
        self.vendor_system.register_observer(self.vendor_observer)
        self.vendor_system.update_vegetable_availability(self.stock)

    def test_place_order(self):
        place_order = {"Tomato": 5, "Carrot": 3, "Spinach": 2}
        self.vendor_system.place_order(place_order)
        # Assuming the order is placed successfully, check if the stock is updated
        for vegetable, qty in place_order.items():
            self.assertEqual(self.stock[vegetable] - qty, self.vendor_system._vegetable_availability[vegetable])

    def test_confirm_payment(self):
        # Confirm payment with an amount less than 100
        order_amount = 80
        with self.assertRaisesRegex(Exception, "Orders should be placed for more than Rs. 100"):
            self.vendor_system.confirm_payment(order_amount)

    def test_place_order_after_payment_disabled(self):
        # Confirm payment
        self.vendor_system.confirm_payment(120)

        # Try placing an order after payment (should be disabled)
        place_order = {"Tomato": 5, "Carrot": 3, "Spinach": 2}
        with self.assertRaisesRegex(Exception, "Order placement is disabled after payment"):
            self.vendor_system.place_order(place_order)


    def test_notify_order_ready(self):
        delivery_time = "2:00 PM"
        self.vendor_system.notify_order_ready(delivery_time)

        # Check if both customer and vendor are notified
        self.assertEqual(self.customer_observer._delivery_time, delivery_time)
        self.assertEqual(self.vendor_observer._delivery_time, delivery_time)

if __name__ == '__main__':
    vendor_system = VegetableVendorSystem()
    stock = {"Tomato": 50, "Carrot": 50, "Spinach": 50, "Onion": 50, "Garlic": 50}     

    customer_observer = CustomerObserver()
    vendor_observer = VendorObserver()

    vendor_system.register_observer(customer_observer)
    vendor_system.register_observer(vendor_observer)

    vendor_system.update_vegetable_availability(stock)

    placeOrder = {}
    for name in stock.keys():
        placeOrder[name] = 0

    process = True

    n = int(input("Enter how many vegetables you are going to purchase: "))
    for i in range(n):
        name = input(f"Enter vegetable{i+1} name: ")
        qty = int(input(f"Enter the quantity: "))
        if stock[name.title()] > qty:
            placeOrder[name.title()] += qty
        else:
            print(f"Sorry, we ran out of {name}")

    print(f'Your Current Order is:', placeOrder)

    # Assuming delivery_time is provided by some means (e.g., input)
    delivery_time = input("Enter tentative time of delivery (e.g., 2:00 PM): ")

    # Perform ordering and delivery tasks concurrently using threads
    order_thread = threading.Thread(target=vendor_system.place_order_async, args=(placeOrder,))
    delivery_thread = threading.Thread(target=vendor_system.notify_order_ready_async, args=(delivery_time,))

    order_thread.start()
    delivery_thread.start()

    # Wait for both threads to complete before proceeding
    order_thread.join()
    delivery_thread.join()

    # Run unit tests
    unittest.main()