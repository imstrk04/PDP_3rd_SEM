from abc import ABC, abstractmethod
import json

'''class Observer:

    @abstractmethod
    def update(self):
        pass

class ConfigurationManager:

    _instance = None
    _observers = []
    _config_strategy = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._config_data = {}
        return cls._instance
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._config_data)
    
    def set_configuration_strategy(self, configuration_strategy):
        self._config_strategy = configuration_strategy()
    
    def load_configuration(self, filename):
        config_data = self._config_strategy.read_conifugaration(filename)
        self._config_data = config_data
        self.notify_observers()

class SomeObserver(Observer):

    def update(self, data):
        print("Received Updates", data)

class Istrategy:

    @abstractmethod
    def read_configuration(self, filename):
        pass

class JSONStrategy(Istrategy):

    def read_configuration(self, filename):
        with open(filename, "r") as file:
            config_data = json.load(file)
            return config_data'''

'''class Observable(ABC):

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class Observer(ABC):        

    @abstractmethod
    def update(self, data):
        pass

class WeatherMonitoringSystem:

    def __init__(self,_temp, pressure):
        self.obs_list = []
        self._temp = _temp
        self.pressure = pressure
    
    def attach(self, observer):
        self.obs_list.append(observer)
    
    def dettach(self, observer):
        self.obs_list.remove(observer)
    
    def notify(self, data):
        for observer in self.obs_list:
            observer.update(data)

    @property
    def temperature(self):
        return self._temp

    @temperature.setter
    def temperature(self, new_temp):
        if new_temp != self._temp:
            self._temp = new_temp
            self.notify(self._temp)
    
class Subscribers(Observer):

    def update(self, data):
        print("Updates Received, Change in temp:", data)

w = WeatherMonitoringSystem(30,40)
s1 = Subscribers()
s2 = Subscribers()
w.attach(s1)
w.attach(s2)
w.temperature = 31
'''

#Component
'''class Flavours:

    def cost(self):
        pass

#concrete component 1
class BlackCurrent(Flavours):

    def cost(self):
        return 100

#concrete component 2
class Strawberry(Flavours):

    def cost(self):
        return 60
    
class Decorator(Flavours):

    def __init__(self, flavour):
        self.flavour = flavour

    def cost(self):
        return self.flavour.cost()

class Chocolate_sauce(Decorator):

    def cost(self):
        return self.flavour.cost() + 10

class Gems(Decorator):

    def cost(self):
        return self.flavour.cost() + 5

class RainbowSprinkles(Decorator):

    def cost(self):
        return self.flavour.cost() + 5

class Chocochips(Decorator):

    def cost(self):
        return self.flavour.cost() + 10

strawberry = Strawberry()
print("Cost of Ice cream is:", strawberry.cost())

cc = Chocochips(strawberry)
print("Cost of ice cream:", cc.cost())

rs = RainbowSprinkles(cc)
print("Cost of ice cream:", rs.cost())'''


'''class TrafficLightsState(ABC):

    @abstractmethod
    def action(self):
        pass

class RedLight(TrafficLightsState):

    def action(self):
        print("STOP DONT MOVE")

class GreenLight(TrafficLightsState):

    def action(self):
        print("YOU CAN MOVE")

class YellowLight(TrafficLightsState):

    def action(self):
        print("Be Ready to Stop")

class TrafficLights:
    def __init__(self):
        self.state = None
    
    def setState(self, state):
        self.state = state
    
    def perform_action(self):
        if self.state:
            self.state.action()
        else:
            print("Invalid Action")

t = TrafficLights()
t.setState(RedLight())
t.perform_action()'''

'''from abc import ABC, abstractmethod

# Context
class VendingMachine:
    def __init__(self):
        # Initialize with NoCoinState
        self._state = NoCoinState()

    def set_state(self, state):
        self._state = state

    def insert_coin(self):
        self._state.insert_coin(self)

    def eject_coin(self):
        self._state.eject_coin(self)

    def dispense(self):
        self._state.dispense(self)

# State Interface
class VendingMachineState(ABC):
    @abstractmethod
    def insert_coin(self, vending_machine):
        pass

    @abstractmethod
    def eject_coin(self, vending_machine):
        pass

    @abstractmethod
    def dispense(self, vending_machine):
        pass

# Concrete States
class NoCoinState(VendingMachineState):
    def insert_coin(self, vending_machine):
        print("Coin inserted.")
        vending_machine.set_state(HasCoinState())

    def eject_coin(self, vending_machine):
        print("No coin to eject.")

    def dispense(self, vending_machine):
        print("Please insert a coin.")

class HasCoinState(VendingMachineState):
    def insert_coin(self, vending_machine):
        print("Coin already inserted.")

    def eject_coin(self, vending_machine):
        print("Coin ejected.")
        vending_machine.set_state(NoCoinState())

    def dispense(self, vending_machine):
        print("Dispensing product.")
        vending_machine.set_state(NoCoinState())

# Client Code
if __name__ == "__main__":
    vending_machine = VendingMachine()

    print("starting")
    vending_machine.insert_coin()
    print()
    vending_machine.eject_coin()
    print()
    vending_machine.dispense()
    print()

    print("Again")
    vending_machine.insert_coin()
    print()
    vending_machine.dispense()
'''

S = [y - x for x in [1, 2, 3] for y in [3, 4, 5] if y > x]
print(S)

L = []
for y in [3, 4, 5]:
    for x in [1, 2, 3]:
        if y > x:
            L += [y -x]
print(L)