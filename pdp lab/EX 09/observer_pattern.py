#Subject interface
from abc import ABC, abstractmethod

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
            # Disable further order appending after payment
            self._orders = None
        else:
            print("Orders should be placed for more than Rs. 100")

    def place_order(self, order):
        if self._orders is not None:
            self._orders.append(order)
            print(f"Order placed. Order number: {len(self._orders)}")
        else:
            print("Order placement is disabled after payment.")

    def notify_order_ready(self, delivery_time):
        for observer in self._observers:
            observer.notify_order_ready(delivery_time)

#Concrete Observer
class CustomerObserver(VegetableObserver):
    def update_vegetable_availability(self, vegetables):
        print(f"Available Vegetables: {vegetables}")

    def confirm_payment(self, order_amount):
        print(f"Payment confirmed. Amount: Rs. {order_amount}")

    def notify_order_ready(self, delivery_time):
        print(f"Your order is ready. It will be delivered at {delivery_time}")

class VendorObserver(VegetableObserver):
    def update_vegetable_availability(self, vegetables):
        print(f"Updated Vegetable Availability for Vendor: {vegetables}")

    def confirm_payment(self, order_amount):
        print(f"Payment received from customer. Amount: Rs. {order_amount}")

    def notify_order_ready(self, delivery_time):
        print(f"Order ready for delivery at {delivery_time}. Notify customer.")

#Example:
# Example usage of the Vegetable Vendor System
vendor_system = VegetableVendorSystem()

# Create observers (customer and vendor)
customer_observer = CustomerObserver()
vendor_observer = VendorObserver()

# Register observers with the subject (Vegetable Vendor System)
vendor_system.register_observer(customer_observer)
vendor_system.register_observer(vendor_observer)

# Update vegetable availability
vendor_system.update_vegetable_availability({"Tomato": 10, "Carrot": 15, "Spinach": 20})

# Place an order
vendor_system.place_order({"Tomato": 2, "Carrot": 3, "Spinach": 1})

# Confirm payment
vendor_system.confirm_payment(120)

# Notify order readiness
vendor_system.notify_order_ready("4:00 PM")
