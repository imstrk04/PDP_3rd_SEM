from abc import ABC, abstractmethod

class Vehicle(ABC):

    @property
    def vehcolor(self):
        return self._color

    @vehcolor.setter
    def vehcolor(self, color):
        if color in self.vehcolorcatalog:
            self._color=color
        else:
            raise ValueError("The vehicle color is not available")

   
    @abstractmethod
    def vehcolorcatalog(self):
        ...

    @abstractmethod
    def vehtype(self, price):
        ...


class Car(Vehicle):
    @property
    def vehcolorcatalog(self):
        return["white","black"]

    def vehtype(self,price):
        print(f"Car is of color {self._color}")

        if price<100000:
            print("buy")
        else:
            print("dont buy")

class Bus(Vehicle):
    @property
    def vehcolorcatalog(self):
        return["red","blue"]

    
    def vehtype(self,price):
        print(f"Bus is of color {self._color}")
        
        if price<1000000:
            print("buy")
        else:
            print("dont buy")


vehicle1=Car()
vehicle1.vehcolor="white"
vehicle1.vehtype(1000)

vehicle2=Bus()
vehicle2.vehcolor="blue"
vehicle2.vehtype(10000000)
