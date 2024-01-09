'''Design a temperature monitoring system using design patterns.
Implement the Singleton pattern to ensure there is only one instance of the weather station.
Use the Observer pattern to allow temperature displays to receive updates when the temperature changes.
Implement two concrete temperature measurement strategies: 
random temperature measurement and fixed temperature measurement.
Provide a client code that demonstrates the usage of the system with 
comments explaining each part of the design.
Make sure to import the necessary modules and include meaningful 
comments in your implementation.
'''
import random

#abstract class for observer
class temperatureobserver:

    def update(self):
        pass

#abstract class for strategy
class temperaturestrategy:
    def measure_temp(self):
        pass


#concrete class strategy
class randomtempstrategy(temperaturestrategy):
    def measure_temp(self):
        return random.randint(-10,30)

class fixedtempstrategy(temperaturestrategy):
    def __init__(self,temp):
        self.temp=temp

    def measure_temp(self):
        return self.temp


#observable class using singleton to create a single instance
class WeatherStation:
    
    _instance=None

    def __new__(cls):
        if not cls._instance:
            cls._instance=super(WeatherStation,cls).__new__(cls)
            cls._instance.measurement_strategy=None
            cls._instance.observers=[]
        return cls._instance

    def set_measurement_strategy(self,measurement_strategy):
        self.measurement_strategy=measurement_strategy

    def add_observer(self,observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self,observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def measure_temp(self):
        temperature=self.measurement_strategy.measure_temp()
        self.notify_observers(temperature)

    def notify_observers(self,temp):
        for observer in self.observers:
            observer.update(temp)

#concrete class for observer
class Tempdisplay(temperatureobserver):
    def __init__(self,device_name):
        self.device_name=device_name

    def update(self,message):
        print(f'{self.device_name} received a notification ! current temperature : {message}')

#Driver code
rand_strat=randomtempstrategy()
fixed_strat=fixedtempstrategy('42 degree')

Weatherstation=WeatherStation()
Weatherstation.set_measurement_strategy(fixed_strat)

displaydevice1=Tempdisplay('TV')
displaydevice2=Tempdisplay('Smartphone')

Weatherstation.add_observer(displaydevice1)
Weatherstation.add_observer(displaydevice2)

Weatherstation.measure_temp()