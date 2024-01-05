import threading
from abc import ABC, abstractmethod
import unittest

class observable:

    def add_observer(self, observer):
        pass

    def remove_observer(self, observer):
        pass

    def notify_observer(self):
        pass

class observer:

    def update(self, msg):
        pass

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

    def notify_observer(self, message):
        for observer in self.observers:
            observer.update(message)

    def place_order(self, vegetables):
        with self.lock:
            order_no = self.order_no + 1
            if not order_no in self.vegetables:
                self.vegetables[order_no] = vegetables
            self.notify_observer(f'Order no : {order_no} Order Placed for : {vegetables}')
            self.order_no = order_no

    def pay_bill(self, order_no):
        with self.lock:
            if order_no in self.vegetables:
                total = 0
                for item in self.vegetables[order_no]:
                    total += item['price']
            self.notify_observer(f'Total : {total} Paid for Order No : {order_no}')

class customer:

    def __init__(self, name):
        self.name= name

    def update(self, msg):
        print(f'{self.name} received a notification : {msg}')

class Vendor:

    def update(self, msg):
        print(f'Vendor received a message : {msg}')

def order_thread(vendorsystem, vegetables):
    vendorsystem.place_order(vegetables)

def bill_thread(vendorsystem, order_no):
    vendorsystem.pay_bill(order_no)

class TestVendorSystem(unittest.TestCase):

    def setUp(self):
        self.c1 = customer('Sada')
        self.vendor = Vendor()
        self.vendorsystem = VendorSystem()
        self.vendorsystem.add_observer(self.c1)
        self.vendorsystem.add_observer(self.vendor)

    def test_place_order_and_pay_bill(self):
        order_thread1 = threading.Thread(target = order_thread, args = (self.vendorsystem, [{'name' : 'carrot', 'qty':5, 'price' : 80}]))
        print()
        order_thread2 = threading.Thread(target = order_thread, args = (self.vendorsystem, [{'name' : 'onion', 'qty' : 10, 'price' : 60}]))

        bill_thread1 = threading.Thread(target = bill_thread, args = (self.vendorsystem, 1))
        bill_thread2 = threading.Thread(target = bill_thread, args = (self.vendorsystem, 2))

        order_thread1.start()
        order_thread2.start()

        order_thread1.join()
        order_thread2.join()

        bill_thread1.start()
        bill_thread2.start()

        bill_thread1.join()
        bill_thread2.join()

        self.assertEqual(self.vendorsystem.order_no, 2)

unittest.main()
