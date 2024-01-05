from abc import ABC

class Vehicle(ABC):

    def vehtype(self):
        ...

class Car(Vehicle):
    def vehtype(self):
        print("car")

class Bus(Vehicle):
    def vehtype(self):
        print("bus")

b=Bus()
b.vehtype()
c=Car()
c.vehtype()


vehicle=[Car(),Bus()]

for v in vehicle:
    v.vehtype()
                
