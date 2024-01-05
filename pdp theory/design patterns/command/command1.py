from abc import ABC, abstractmethod

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

# ICommand interface
class ICommand(ABC):
    @abstractmethod
    def execute(self):
        pass

# Command
class LightOnCommand(ICommand):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

# Another Command
class LightOffCommand(ICommand):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# Receiver
class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")



# Client
if __name__ == "__main__":
    # Creating instances
    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    remote = RemoteControl()

    # Associating the command with the invoker
    remote.set_command(light_on)

    # Pressing the button
    remote.press_button()

    # Changing the command
    remote.set_command(light_off)
    remote.press_button()
