from abc import ABC, abstractmethod
import random
#command pattern
'''class ICommand(ABC):

    def execute(self):
        pass

class Request(ICommand):

    def __init__(self, system, ticket_type,ticket_no, observers):
        self.system = system
        self.ticket_type = ticket_type
        self.ticket_no = ticket_no
        self.observers = observers

    def execute(self):
        print(f"Request for ticket no. {self.ticket_no} is registered for {self.ticket_type} type")
        self.system.add_ticket((self.ticket_type, self.ticket_no))
        self.notify_observers()
        
    def notify_observers(self):
        for observer in self.observers:
            observer.update(f"Ticket {self.ticket_no} ({self.ticket_type})")
            
        
class Complaint(ICommand):

    def __init__(self, system, ticket_type, ticket_no, obserrvers):
        self.system = system
        self.ticket_type = ticket_type
        self.ticket_no = ticket_no
        self.observers = observers

    def execute(self):
        print(f"Complaint for ticket no. {self.ticket_no} is registered for {self.ticket_type} type")
        self.system.add_ticket((self.ticket_type, self.ticket_no))
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(f"Ticket {self.ticket_no} ({self.ticket_type})")

class Observer(ABC):

    @abstractmethod
    def update(self, ticket):
        pass

class TicketObserver(Observer):

    def __init__(self, name):
        self.name = name

    def update(self, ticket):
        print(f"{self.name} received a new ticket: {ticket}")
        
class ServiceEngineer(TicketObserver):

    def __init__(self, name):
        super().__init__(name)
        self.command = None

    def set_command(self, command):
        self.command = command

    def process_command(self):
        if self.command:
            self.command.execute()
        else:
            print("No Command Set")
    

class System:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(System, cls).__new__(cls)
        cls.tickets = []
        cls.observers = []
        return cls._instance

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def remove_ticket(self, ticket):
        self.ticket.pop()

    def add_observers(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observer(self, ticket):
        for observer in self.observers:
            observer.update(ticket)


print("---------------SSN HELPDESK--------------")
print()

system = System()
invoker = ServiceEngineer("Sada")
system.add_observers(invoker)

command_type = input("Request or Complaint? :")
service_type = input("What it is about? ")
ticket_num = random.randint(1,100000)
if command_type.lower() == 'request':
    req = Request(system, service_type, ticket_num, system.observers)
    invoker.set_command(req)
    invoker.process_command()
    print(system.tickets)

#Two wheeler service
class Service(ABC):

    @abstractmethod
    def execute(self):
        pass

class Observer(ABC):

    @abstractmethod
    def update(self):
        pass

class TicketObservers(Observer):

    def __init__(self, name):
        self.name = name

    def update(self, ticket):
        print(f"{self.name} has received ticket number {ticket}")


class  QuickService(Service):

    def __init__(self, system, service_type, ticket_num, observers):
        self.system = system
        self.service_type = service_type
        self.ticket_num = ticket_num
        self.observers = observers

    def execute(self):
        self.system.add_tickets((self.ticket_num, self.service_type))
        print(f"{self.service_type} type has been alloted to {self.ticket_num}")
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(f"Ticket {self.ticket_num} {self.service_type}")

class LongService(Service):

    def __init__(self, system, service_type, ticket_num, observers):
        self.system = system
        self.service_type = service_type
        self.ticket_num = ticket_num
        self.observers = observers

    def execute(self):
        self.system.add_tickets((self.ticket_num, self.service_type))
        print(f"{self.service_type} type has been alloted to {self.ticket_num}")
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(f"Ticket {self.ticket_num} {self.service_type}")


class Mechanic(TicketObserver):

    def __init__(self, name):
        super().__init__(name)
        self.service = None

    def set_service(self, service):
        self.service = service

    def process_service(self):
        if self.service:
            self.service.execute()
        else:
            print("No Service is Set")

class ServiceCentre:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ServiceCentre, cls).__new__(cls)
        cls.tickets = []
        cls.observers = []
        return cls._instance

    def add_tickets(self, ticket):
        self.tickets.append(ticket)

    def add_observers(self, observer):
        self.observers.append(observer)

    def notify_observer(self, ticket):
        for observer in self.observers:
            observer.update(tickt)

print("--------------------------------Welcome to TTF PIT SHOP--------------------------------")
print()

system = ServiceCentre()
invoker = Mechanic("Vasan")
system.add_observers(invoker)
name = input("Enter service type (Quick or Long): ")
if name.lower() == 'q' or name.lower() == 'quick':
    ticket_num = random.randint(1,100000)
    quick = QuickService(system, 'quick', ticket_num, system.observers)
    system.add_tickets(quick)
    invoker.set_service(quick)
    invoker.process_service()
    print("TICKETS: ", system.tickets) '''

'''
from abc import ABC,abstractmethod

class State(ABC):
    @abstractmethod
    def process(self):
        pass

class WaitingState(State):
    def process(self):
        print(f'STATE:the package is to be accepted')

class ProcessingState(State):
    def process(self):
        print(f'STATE:the package is being processed')

class ProcessedState(State):
    def process(self):
        print(f'STATE:the package is processed and set for delivery')

class Strategy(ABC):
    @abstractmethod
    def execute_order(self):
        pass

class ExpressDelivery(Strategy):
    def execute_order(self):
        print('STRATEGY:the package is set in express delivery')

class NormalDelivery(Strategy):
    def execute_order(self):
        print('STRETEGY:the package is set in normal delivery')

class observer(ABC):
    @abstractmethod
    def update(self):
        pass

class Owner(observer):
    def __init__(self,name):
        self.name = name

    def update(self,message):
        print(f"Owner {self.name} received a notification: {message}")

class Mechanic(observer):
    def __init__(self,name):
        self.name = name

    def update(self,message):
        print(f"the mechanic {self.name} recived a notifcation:{message}")


class Job:
    def __init__(self,id):
        self.id = id

    def __str__(self):
        print(f'{self.id}')

class ServiceSystem:
    instance = None
    def __new__(cls):
        if not cls.instance:
            cls.instance = super(ServiceSystem,cls).__new__(cls)
            cls.instance.observers = []
            cls.instance.job = {}
            cls.instance.state = WaitingState()
            cls.instance.strategy = ExpressDelivery()
            cls.instance.order_no = 0
        return cls.instance

    def set_state(self,state):
        self.state = state

    def set_strategy(self,strategy):
        self.strategy = strategy

    def add_observer(self,observer):
        if observer not in self.observers:
            self.observers.append(observer)
    
    def remove_observer(self,observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observer(self,message,observertype=None):
        for observer in self.observers:
            if observertype is None or isinstance(observer,observertype):
                observer.update(message)

    def add_job(self,order_no,name,date):
        if order_no not in self.job:
            self.job[order_no] = {'name':name,'date':date}
        self.notify_observer(f'a new job has been assigned {name}',Mechanic)

    def execute_order(self,order_no):
        if order_no in self.job:
            self.job.pop(order_no)
        else:
            print('specified job not in list')
        self.state.process()
        print(f'current delivery strategy')
        self.strategy.execute_order()
        self.set_state(ProcessingState())
        self.state.process()
        self.set_state(ProcessedState())
        self.state.process()
        self.notify_observer('the job is done with')


owner1 = Owner('tanushee')
owner2 = Owner('mohit')

mech = Mechanic('pichamani')
vs = ServiceSystem()
vs.add_observer(owner1)
vs.add_observer(owner2)
vs.add_observer(mech)    
    
vs.add_job(1,'job1',"2023-01-12")
vs.add_job(2,'job2',"2023-01-10")
vs.add_job(3,'job3',"2023-01-9")

vs.execute_order(2)
vs.set_strategy(NormalDelivery())
vs.execute_order(3)
print(vs.job)'''

class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self._push_left_children(root)

    def _push_left_children(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def has_next(self):
        return bool(self.stack)

    def next(self):
        if not self.has_next():
            raise StopIteration("No more elements in BST")

        current_node = self.stack.pop()
        self._push_left_children(current_node.right)

        return current_node.value

def build_bst():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    return root

if __name__ == "__main__":

    bst_root = build_bst()

    bst_iterator = BSTIterator(bst_root)

    expected_result = [2,3,4,5,6,7,8,9]

    result = []
    while bst_iterator.has_next():
        result.append(bst_iterator.next())
    print(result)















































    
        
