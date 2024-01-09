import threading
from abc import ABC, abstractmethod
import unittest
import time


# observable interface
class observable:
    def add_observer(self):
        pass

    def remove_observer(self):
        pass

    def notify_customer(self):
        pass

# observer interface
class observer:
    def update(self):
        pass

# concrete observable
class VendorSystem:
    def __init__(self):
        self.observers = []
        self.vegetables = {}
        self.order_no = 0
        self.lock = threading.Lock()

    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

    def place_order(self, vegetables):
        with self.lock:
            order_no = self.order_no + 1
            if not order_no in self.vegetables:
                self.vegetables[order_no] = vegetables
            self.notify_observers(f'order no : {order_no} order placed for : {vegetables}')
            self.order_no = order_no

    def pay_bill(self, order_no):
        with self.lock:
            if order_no in self.vegetables:
                total = 0
                for item in self.vegetables[order_no]:
                    total += item['price']

                self.notify_observers(f'total: {total} paid for order_no: {order_no}')

# concrete observer
class customer:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f' {self.name} received a notification : {message}')

class Vendor:
    def update(self, message):
        print(f'vendor received a message : {message}')

# functions for threading
def order_thread(vendorsystem, vegetables):
    vendorsystem.place_order(vegetables)

def bill_thread(vendorsystem, order_no):
    vendorsystem.pay_bill(order_no)

class TestVendorSystem(unittest.TestCase):
    def setUp(self):
        self.c1 = customer('srihari')
        self.vendor = Vendor()
        self.vendorsystem = VendorSystem()
        self.vendorsystem.add_observer(self.c1)
        self.vendorsystem.add_observer(self.vendor)

    def test_place_order_and_pay_bill(self):
        order_thread1 = threading.Thread(target=order_thread, args=(self.vendorsystem, [{'name': 'carrot', 'qty': 5, 'price': 80}]))
        order_thread2 = threading.Thread(target=order_thread, args=(self.vendorsystem, [{'name': 'beetroot', 'qty': 6, 'price': 70}]))

        bill_thread1 = threading.Thread(target=bill_thread, args=(self.vendorsystem, 1))
        bill_thread2 = threading.Thread(target=bill_thread, args=(self.vendorsystem, 2))

        print("order thread")
        time.sleep(1)
        order_thread1.start()
        time.sleep(1)
        order_thread2.start()

        order_thread1.join()
        order_thread2.join()

        print("Bill thread")
        time.sleep(1)
        bill_thread1.start()
        time.sleep(1)
        bill_thread2.start()

        time.sleep(1)
        bill_thread1.join()
        time.sleep(1)
        bill_thread2.join()

        # Add assertions here to check if the order and bill operations were successful
        # For example, check if the order number has been incremented correctly

        # Example assertion:
        self.assertEqual(self.vendorsystem.order_no, 2)

if __name__ == '__main__':
    unittest.main()
