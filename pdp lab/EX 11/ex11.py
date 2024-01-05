import threading
import time

class VegetableVendor:
    def __init__(self):
        self.vegetables = {'Tomato': 20, 'Potato': 15, 'Onion': 10}
        self.orders = {}
        self.order_counter = 1
        self.lock = threading.Lock()

    def display_available_vegetables(self):
        print("Available Vegetables:")
        for veg, quantity in self.vegetables.items():
            print(f"{veg}: {quantity} kg")

    def place_order(self, customer_name, order_items):
        with self.lock:
            order_total = 0
            order_details = {}
            for veg, quantity in order_items.items():
                if veg in self.vegetables and self.vegetables[veg] >= quantity:
                    order_details[veg] = quantity
                    order_total += quantity * 10  # Assuming Rs. 10 per kg
                    self.vegetables[veg] -= quantity

            if order_total >= 100:
                order_number = self.order_counter
                self.orders[order_number] = {'customer': customer_name, 'items': order_details, 'total': order_total}
                self.order_counter += 1
                print(f"Order placed successfully. Order Number: {order_number}")
                self.notify_customer_payment(customer_name, order_number)
                self.notify_vendor(order_number)
                return order_number
            else:
                print("Order total should be more than Rs. 100. Please add more items.")
                return None

    def notify_customer_payment(self, customer_name, order_number):
        print(f"Payment confirmation sent to {customer_name} for Order Number {order_number}")

    def notify_vendor(self, order_number):
        print(f"Order Number {order_number} notified to the vendor.")

    def prepare_order(self, order_number):
        time.sleep(5)  # Simulate order preparation time
        print(f"Order Number {order_number} is ready for delivery.")
        self.notify_customer_delivery(order_number)

    def notify_customer_delivery(self, order_number):
        print(f"Notification sent to customer for Order Number {order_number}: Your order will be delivered soon.")

def customer_thread(vegetable_vendor, customer_name, order_items):
    vegetable_vendor.display_available_vegetables()
    order_number = vegetable_vendor.place_order(customer_name, order_items)
    if order_number:
        vegetable_vendor.prepare_order(order_number)

def vendor_thread(vegetable_vendor):
    while True:
        time.sleep(10)  # Check for new orders every 10 seconds
        with vegetable_vendor.lock:
            print("Vendor checking for new orders...")
            if vegetable_vendor.orders:
                order_number, order_details = vegetable_vendor.orders.popitem()
                print(f"Vendor processing Order Number {order_number}...")
                vegetable_vendor.notify_vendor_delivery(order_number)

if __name__ == "__main__":
    vendor = VegetableVendor()

    # Customer 1 placing an order
    customer1_order = {'Tomato': 2, 'Potato': 3}
    customer1_thread = threading.Thread(target=customer_thread, args=(vendor, 'Customer1', customer1_order))

    # Customer 2 placing an order
    customer2_order = {'Onion': 5}
    customer2_thread = threading.Thread(target=customer_thread, args=(vendor, 'Customer2', customer2_order))

    # Vendor processing orders
    vendor_thread = threading.Thread(target=vendor_thread, args=(vendor,))

    # Start threads
    customer1_thread.start()
    customer2_thread.start()
    vendor_thread.start()

    # Join threads
    customer1_thread.join()
    customer2_thread.join()
    vendor_thread.join()
