from abc import ABC, abstractmethod

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, job_details):
        pass

# Observable interface
class Observable(ABC):
    def add_observer(self, observer, job_type):
        pass

    def remove_observer(self, observer, job_type):
        pass

    def notify_observers(self, job_type, job_details):
        pass

# Concrete Observable
class Printer(Observable):
    def __init__(self):
        self.observers = {}

    def add_observer(self, observer, job_type):
        if job_type not in self.observers:
            self.observers[job_type] = []
        self.observers[job_type].append(observer)
        

    def remove_observer(self, observer, job_type):
        if job_type in self.observers and observer in self.observers[job_type]:
            self.observers[job_type].remove(observer)
            

    def notify_observers(self, job_type, job_details):
        if job_type in self.observers:
            for observer in self.observers[job_type]:
                observer.update(job_details)

# Concrete Observer
class Employee(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, job_details):
        print(f"Employee {self.name} received a job: {job_details}")

# Concrete Observer
class System(Observer):
    def __init__(self, system_name):
        self.system_name = system_name

    def update(self, job_details):
        print(f"System {self.system_name} received a job: {job_details}")

# Example Usage
printer = Printer()

employee1 = Employee("EmployeeX")
employee2 = Employee("EmployeeY")
system1 = System("SystemA")

printer.add_observer(employee1, "EmployeeJob")
printer.add_observer(employee2, "EmployeeJob")
printer.add_observer(system1, "SystemJob")

printer.notify_observers("EmployeeJob", "PrintJob(EmployeeX, 123)")
printer.notify_observers("SystemJob", "PrintJob(SystemA, 456)")

printer.remove_observer(employee1, "EmployeeJob")

printer.notify_observers("EmployeeJob", "PrintJob(EmployeeY, 123)")

