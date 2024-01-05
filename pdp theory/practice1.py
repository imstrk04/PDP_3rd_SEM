#Iterator Pattern
print("Iterator Pattern")
class Iterable:

    def create_iterator(self):
        pass

class Iterator:

    def has_next(self):
        pass

    def next(self):
        pass

class ConcreteIterable(Iterable):

    def __init__(self):
        self.data = [1,2,3,4,5]

    def create_iterator(self):
        return ConcreteIterator(self)

class ConcreteIterator(Iterator):

    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def has_next(self):
        return self.index < len(self.iterable.data)

    def next(self):
        if self.has_next():
            value = self.iterable.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration("No more elements")

iterable = ConcreteIterable()
iterator = iterable.create_iterator()

while iterator.has_next():
    value = iterator.next()
    print(value)

print()
#Observer Pattern
print("Observer Pattern")
class WeatherStation:

    def __init__(self, place, _temp):
        self.obs_list = []
        self.place = place
        self._temp = _temp

    def __str__(self):
        return f"Temp at {self.place} is {self._temp} degree Celcius"

    def attach(self, obs):
        self.obs_list.append(obs)

    def dettach(self, obs):
        self.obs_list.remove(obs)

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, new_temp):
        if new_temp != self._temp:
            self._temp = new_temp
            self.notify()

    def notify(self):
        for obs in self.obs_list:
            obs.update(self)

class PhoneDisplay:

    def __init__(self):
        pass

    def update(self, temp):
        print("Phone Display:", temp)

class WindowDisplay:

    def __init__(self):
        pass

    def update(self, temp):
        print("Window Display:", temp)

w = WeatherStation('Chennai', 27)
observer1 = PhoneDisplay()
observer2 = WindowDisplay()

w.attach(observer1)
w.attach(observer2)
w.temp = 26

print()
print("Weather Monitoring System")
from abc import ABC, abstractmethod

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, weather_data):
        pass

# Subject class (Weather Monitoring System)
class WeatherMonitoringSystem:
    def __init__(self, place):
        self.place = place
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, weather_data):
        for observer in self.observers:
            observer.update(weather_data)

    def set_conditions(self, conditions):
        # Simulate weather data change
        weather_data = {'place': self.place, 'conditions': conditions}
        self.notify_observers(weather_data)

# Concrete Observer classes
class EmailNotifier(Observer):
    def __init__(self, user_email, conditions):
        self.user_email = user_email
        self.conditions = conditions

    def update(self, weather_data):
        if all(weather_data['conditions'][key] >= value for key, value in self.conditions.items()):
            print(f"Sending email to {self.user_email}: Weather conditions met - {weather_data}")

class SMSNotifier(Observer):
    def __init__(self, user_phone, conditions):
        self.user_phone = user_phone
        self.conditions = conditions

    def update(self, weather_data):
        if all(weather_data['conditions'][key] >= value for key, value in self.conditions.items()):
            print(f"Sending SMS to {self.user_phone}: Weather conditions met - {weather_data}")

class PushNotifier(Observer):
    def __init__(self, user_device, conditions):
        self.user_device = user_device
        self.conditions = conditions

    def update(self, weather_data):
        if all(weather_data['conditions'][key] >= value for key, value in self.conditions.items()):
            print(f"Sending push notification to {self.user_device}: Weather conditions met - {weather_data}")

# Example usage
weather_system = WeatherMonitoringSystem('Chennai')

# Users register for alerts with specific conditions
email_user = EmailNotifier('user@example.com', {'temperature': 30, 'humidity': 50})
sms_user = SMSNotifier('1234567890', {'temperature': 25})
push_user = PushNotifier('MobileDevice123', {'humidity': 60})

weather_system.add_observer(email_user)
weather_system.add_observer(sms_user)
weather_system.add_observer(push_user)

# Simulate changes in weather conditions
weather_system.set_conditions({'temperature': 28, 'humidity': 55})
print()

#State Pattern
print("State Pattern")
class IState:
    def read(self, reader):
        pass

    def write(self, writer):
        pass

class ReaderState(IState):

    def read(self, reader):
        print(f"{reader.name} is Reading.")

class WriterState(IState):

    def write(self, writer):
        print(f"{writer.name} is writing.")

class Resource:

    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def perform_read(self, reader):
        self.state.read(reader)

    def perform_write(self, writer):
        self.state.write(writer)

class Reader:
    def __init__(self, resource, name):
        self.resource = resource
        self.name = name

    def read(self):
        self.resource.perform_read(self)

class Writer:
    def __init__(self, resource, name):
        self.resource = resource
        self.name = name

    def write(self):
        self.resource.perform_write(self)

resource = Resource()
resource.set_state(ReaderState())
reader1 = Reader(resource, "Rajesh")
reader2 = Reader(resource, "Ananya")
writer1 = Writer(resource, "Arjun")

reader1.read()
reader2.read()
resource.set_state(WriterState())
writer1.write()

print()
print("Singleton Pattern")

class S_class:
    S_instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.S_instance:
            cls.S_instance = super().__new__(cls, *args, **kwargs)
        return cls.S_instance
x = S_class()
y = S_class()
print(x)
print(y)
print()
print("Question")
from abc import ABC, abstractmethod
import threading
import time

#IObserver
class ReservationObserver(ABC):

    @abstractmethod
    def update_reservation_status(self, table_number, status):
        pass

#IObservable
class ReservationSubject(ABC):

    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self, observer):
        pass

#Concrete Observable
class TableReservationSystem(ReservationSubject):

    def __init__(self, num_tables, seats_per_table):
        self._observers = []
        self._num_tables = num_tables
        self._seats_per_table = seats_per_table
        self._table_status = {i+1: {'status':'available', 'seats':seats_per_table} for i in range(num_tables)}
        self._lock = threading.Lock()

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        sefl._observers.remove(observer)

    def notify_observers(self, table_number, status):
        for observer in self._observers:
            observer.update_reservation_status(table_number, status)

    def reserve_table(self, num_seats):
        with self._lock:
            for table_number, table_info in self._table_status.items():
                if table_info['status'] == 'available' and table_info['seats'] >= num_seats:
                    self._table_status[table_number]['status'] = 'occupied'
                    self.notify_observers(table_number, 'occupied')
                    return table_number
            return None

    def release_table(self, table_number):
        with self._lock:
            if table_number in self._table_status and self._table_status[table_number]['status'] == 'occupied':
                self._table_status[table_number]['status'] = 'available'
                self.notify_observers(table_number, 'available')

class ReservationClient(ReservationObserver):
    def __init__(self, client_name):
        self._client_name = client_name

    def update_reservation_status(self, table_number, status):
        print(f"Client {self._client_name}: Table {table_number} is now {status}")

def reservation_worker(system, client, num_seats):
    table_number = system.reserve_table(num_seats)
    if table_number is not None:
        print(f"Client {client._client_name}: Table {table_number} reserved")
        time.sleep(3)  # Simulating some work before releasing the table
        system.release_table(table_number)
        print(f"Client {client._client_name}: Table {table_number} released")

'''import unittest

class TestTableReservationSystem(unittest.TestCase):

    def test_reservation_system(self):
        num_tables = 5
        seats_per_table = 4

        reservation_system = TableReservationSystem(num_tables, seats_per_table)

        # Registering clients as observers
        client1 = ReservationClient("Alice")
        client2 = ReservationClient("Bob")
        reservation_system.register_observer(client1)
        reservation_system.register_observer(client2)

        self.assertEqual(len(reservation_system._observers), 2)

        table_number = reservation_system.reserve_table(2)
        self.assertIsNotNone(table_number)
        self.assertEqual(reservation_system._table_status[table_number]['status'], 'occupied')

        reservation_system.release_table(table_number)
        self.assertEqual(reservation_system._table_status[table_number]['status'], 'available')    

def main():
    num_tables = 5
    seats_per_table = 4

    reservation_system = TableReservationSystem(num_tables, seats_per_table)

    # Registering clients as observers
    client1 = ReservationClient("Alice")
    client2 = ReservationClient("Bob")
    reservation_system.register_observer(client1)
    reservation_system.register_observer(client2)

    # Simulating multiple threads for reservation and bill payment work
    thread1 = threading.Thread(target=reservation_worker, args=(reservation_system, client1, 2))
    thread2 = threading.Thread(target=reservation_worker, args=(reservation_system, client2, 3))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
'''

print()
print("GENERATORS")

def sq_num(nums):
    for i in nums:
        yield (i*i)
my_nums = sq_num([1,2,3,4,5])
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))

my_nums = (x * x for x in [1,2,3,4,5])
print(list(my_nums))

print()
print("Comprehension")
dict1 = {i : i + 10 for i in range(4)}
print(dict1)


print()
print("Command Pattern")

class System:

    def __init__(self):
        self.ticket = []

    def add_ticket(self, ticket):
        self.ticket.append(ticket)

    def remove_ticket(self, ticket):
        self.ticket.remove(ticket)

class ICommand(ABC):

    @abstractmethod
    def execute(self):
        pass

class Request(ICommand):

    def __init__(self, department, service_type):
        self.department = department
        self.service_type = service_type

    def execute(self):
        print(f"Executing Request of {self.service_type} in {self.department}")

class Complaint(ICommand):

    def __init__(self, department, service_type):
        self.department = department
        self.service_type = service_type
        
    def execute(self):
        print(f"Executing Complaint of {self.service_type} in {self.department}")

class Service_Engineer:

    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def perform(self):
        self.command.execute()

sys = System()
req1 = Request("IT", "Software")
comp1 = Complaint("Mech", "Hardware")
sys.add_ticket(req1)
sys.add_ticket(comp1)
ser_eng = Service_Engineer()
ser_eng.set_command(req1)
ser_eng.perform()

print()
print("Adapter pattern")
class flatarray:

    def __init__(self, size):
        self.size = size
        self.array = [0] * self.size

    def set_value(self, index, value):
        self.array[index] = value

    def get_value(self, index):
        return self.array[index]

class multiarray:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.array = [[0] * columns for _ in range(rows)]

    def set_value(self, row, column, value):
        self.array[row][column] = value

    def get_value(self, row, column):
        return self.array[row][column]

class arrayadapter(flatarray):

    def __init__(self, multi_array):
        size = multi_array.rows * multi_array.columns
        super().__init__(size)
        self.multi_array = multi_array

    def set_values(self, index, value):
        row = index // self.multi_array.columns
        col = index % self.multi_array.columns
        self.multi_array.set_value(row, col, value)

    def get_values(self, index):
        row = index // self.multi_array.columns
        col = index % self.multi_array.columns
        return self.multi_array.get_values(row, col)

multi_array = multiarray(rows = 3, columns = 3)
adapter = arrayadapter(multi_array)

adapter.set_values(5, 100)
print(adapter.get_value(5))

#Decorator
print()
print("Decorator Pattern")
class Text:
    def __init__(self, msg):
        self.msg = msg

    def show(self):
        return self.msg

class Bold(Text):

    def __init__(self, msg):
        self.boldmsg = msg

    def show(self):
        return f"<b>{self.boldmsg.show()}</b>"

class Underline(Text):

    def __init__(self, msg):
        self.underlinemsg = msg

    def show(self):
        return f"<u>{self.underlinemsg.show()}</u>"

class Italic(Text):

    def __init__(self, msg):
        self.italicmsg = msg

    def show(self):
        return f"<i>{self.italicmsg.show()}</i>"

t = Text('sada')
msg = Underline(Italic(Bold(t)))
print(msg.show())
print()
print("multiple design patterns")
print("Temperature Station")
import random

class temperatureobserver:

    def update(self):
        pass

class temperaturestrategy:

    def measure_temp(self):
        pass

class randomtempstrategy(temperaturestrategy):

    def measure_temp(self):
        return random.randint(-10,30)

class fixedtempstrategy(temperaturestrategy):

    def __init__(self, temp):
        self.temp = temp

    def measure_temp(self):
        return self.temp

class WeatherStation:

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(WeatherStation, cls).__new__(cls)
            cls._instance.measurement_strategy = None
            cls._instance.observers = []
        return cls._instance

    def set_measurement_strategy(self, measurement_strategy):
        self.measurement_strategy = measurement_strategy

    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def measure_temp(self):
        temperature = self.measurement_strategy.measure_temp()
        self.notify_observers(temperature)

    def notify_observers(self, temp):
        for observer in self.observers:
            observer.update(temp)

class Tempdisplay(temperatureobserver):

    def __init__(self, device_name):
        self.device_name = device_name

    def update(self, message):
        print(f"{self.device_name} received a notification ! Current Temperature is {message}")

rand_strategy = randomtempstrategy()
fixed_strat = fixedtempstrategy('42 degreee')

w = WeatherStation()
w.set_measurement_strategy(rand_strategy)
display = Tempdisplay('Iphone 14')
w.add_observer(display)
w.measure_temp()
w.set_measurement_strategy(fixed_strat)
w.measure_temp()
'''
print()
print("Unittesting and Multithreading")
print("Staring here\n")

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
            self.notify_observer(f'Order no : {order_no}\nOrder Placed for : {vegetables}')
            self.order_no = order_no

    def pay_bill(self, order_no):
        with self.lock:
            if order_no in self.vegetables:
                total = 0
                for item in self.vegetables[order_no]:
                    total += item['price']
            self.notify_observer(f'Total : {total}\nPaid for Order No : {order_no}')

class customer:

    def __init__(self, name):
        self.name= name

    def update(self, msg):
        print(f'{self.name} received a notification : {msg}')

class vendor:

    def update(self, msg):
        print(f'Vendor received a message : {message}')

def order_thread(vendorsystem, vegetables):
    vendorsystem.place_order(vegetables)

def bill_thread(vendorsystem, order_no):
    vendorsystem.pay_bill(order_no)

class TestVendorSystem(unittest.TestCase):

    def setUp(self):
        self.c1 = customer('Sada')
        self.vendor = vendor()
        self.vendorsystem = VendorSystem()
        self.vendorsystem.add_observer(self.c1)
        self.vendorsystem.add_observer(self.vendor)

    def test_place_order_and_pay_bill(self):
        order_thread1 = threading.Thread(target = order_thread, args = (self.vendorsystem, [{'name' : 'carrot', 'qty':5, 'price' : 80}]))
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
'''





























    
