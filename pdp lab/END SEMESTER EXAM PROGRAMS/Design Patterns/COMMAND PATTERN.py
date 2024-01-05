# Command Interface
class Command:
    def execute(self):
        pass

# Concrete Command
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()
        # Statement: Execute the turn_on method of the Light receiver

# Receiver
class Light:
    def turn_on(self):
        print("Light is ON")
        # Statement: Print "Light is ON" indicating that the light is turned on

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command
        # Statement: Set the command for the invoker

    def press_button(self):
        self.command.execute()
        # Statement: Execute the command when the button is pressed

# Client
light = Light()
light_on = LightOnCommand(light)
# Statement: Create a Light object and a LightOnCommand object with the Light object as the receiver

remote = RemoteControl()
remote.set_command(light_on)
# Statement: Set the LightOnCommand as the command for the RemoteControl

remote.press_button()
# Statement: Press the button on the remote, which triggers the execution of the LightOnCommand
