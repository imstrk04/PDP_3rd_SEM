from abc import ABC, abstractmethod
import threading
import time
import unittest

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

# Subject (Observable) class
class TableReservationSystem:
    def __init__(self):
        self.observers = []
        self.tables = {'Table 1': {'seats': 4, 'occupied': False},
                       'Table 2': {'seats': 6, 'occupied': False}}  # Sample tables
        self.lock = threading.Lock()
       
    def attach(self, observer):
        self.observers.append(observer)
       
    def detach(self, observer):
        self.observers.remove(observer)
       
    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)
       
    def reserve_table(self, num_seats):
        with self.lock:
            for table, details in self.tables.items():
                if not details['occupied'] and details['seats'] >= num_seats:
                    details['occupied'] = True
                    self.notify_observers(f"Table {table} reserved for {num_seats} people.")
                    return table
            return None

    def free_table(self, table):
        with self.lock:
            if table in self.tables:
                self.tables[table]['occupied'] = False
                self.notify_observers(f"Table {table} is now available.")

# Concrete observer - Client
class Client(Observer):
    def __init__(self, name):
        self.name = name
       
    def update(self, message):
        print(f"Client {self.name} received: {message}")

# Concrete observer - Hotel Manager
class HotelManager(Observer):
    def __init__(self, name):
        self.name = name
       
    def update(self, message):
        print(f"Manager {self.name} received: {message}")

def reserve_table_and_notify(reservation_system, num_seats):
    table_reserved = reservation_system.reserve_table(num_seats)
    if table_reserved:
        print(f"Table {table_reserved} is reserved.")

def free_table_and_notify(reservation_system, table):
    reservation_system.free_table(table)

class TestTableReservationSystem(unittest.TestCase):
    def setUp(self):
        self.reservation_system = TableReservationSystem()
        client1 = Client("Alice")
        client2 = Client("Bob")
        manager = HotelManager("John Doe")
        self.reservation_system.attach(client1)
        self.reservation_system.attach(client2)
        self.reservation_system.attach(manager)

    def test_reserve_table(self):
        reservation_thread = threading.Thread(target=reserve_table_and_notify, args=(self.reservation_system, 5))
        reservation_thread.start()
        reservation_thread.join()  

        # Now, attempt to free the table
        payment_thread = threading.Thread(target=free_table_and_notify, args=(self.reservation_system, "Table 1"))
        payment_thread.start()
        payment_thread.join()  

if __name__ == '__main__':
    unittest.main()