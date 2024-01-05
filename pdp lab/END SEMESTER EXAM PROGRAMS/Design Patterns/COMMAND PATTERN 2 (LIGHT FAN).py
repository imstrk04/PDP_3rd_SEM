from abc import ABC, abstractmethod

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete commands
class LightOnCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

class FanOnCommand(Command):

    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.turn_on()

class FanOffCommand(Command):

    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.turn_off()

class ThermostatIncreaseCommand(Command):

    def __init__(self, thermostat):
        self.thermostat = thermostat

    def execute(self):
        self.thermostat.increase_temperature()

class ThermostatDecreaseCommand(Command):

    def __init__(self, thermostat):
        self.thermostat = thermostat

    def execute(self):
        self.thermostat.decrease_temperature()

# Receiver classes
class Light:

    def turn_on(self):
        print('LIGHT ON')

    def turn_off(self):
        print('LIGHT OFF')

class Fan:

    def turn_on(self):
        print('FAN ON')

    def turn_off(self):
        print('FAN OFF')

class Thermostat:

    def increase_temperature(self):
        print('Thermostat: Temperature Increased')

    def decrease_temperature(self):
        print('Thermostat: Temperature Decreased')

# Invoker class (here remote is used to invoke the devices)
class Remote:

    def __init__(self, command):
        self.command = command

    def set_command(self, command):
        self.command = command
        print(f'Command set to {command}')

    def press_button(self):
        self.command.execute()

# Client code
light = Light()
fan = Fan()
thermostat = Thermostat()

light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

fan_on = FanOnCommand(fan)
fan_off = FanOffCommand(fan)

thermostat_increase = ThermostatIncreaseCommand(thermostat)
thermostat_decrease = ThermostatDecreaseCommand(thermostat)

# Creating remotes for each device
light_remote = Remote(light_on)# set it to off or on here 
fan_remote = Remote(fan_on)
thermostat_remote = Remote(thermostat_increase)

# Pressing buttons to test
light_remote.press_button()  # Turns on the light
fan_remote.press_button()    # Turns on the fan
thermostat_remote.press_button()  # Increases the thermostat temperature
