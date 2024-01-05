'''from abc import ABC, abstractmethod
#Command Pattern
# Invoker -> Icommand -> Commands -> Receiver

#Invoker
class RemoteControl:

    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command
    
    def press_button(self):
        self.command.execute()

#Icommand
class Icommand(ABC):
    
    @abstractmethod
    def execute(self):
        pass

#Command1
class LightOnCommand(Icommand):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

#Command2
class LightOffCommand(Icommand):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

#Receiver
class Light:

    def turn_on(self):
        print("Light is On")

    def turn_off(self):
        print("Light is OFF")

if __name__ == '__main__':

    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    remote = RemoteControl()

    remote.set_command(light_on)
    remote.press_button()
    remote.set_command(light_off)
    remote.press_button()'''


'''from abc import ABC, abstractmethod

# Invoker
class Cart:

    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def process_commands(self):
        for command in self.commands:
            command.execute()


# ICommand
class ICommand(ABC):

    @abstractmethod
    def execute(self):
        pass


# Command1: Adding
class Adding(ICommand):

    def __init__(self, item, inventory):
        self.item = item
        self.inventory = inventory

    def execute(self):
        self.item.add()
        self.inventory.update_inventory(self.item.name, 1)


# Command2: Removing
class Removing(ICommand):

    def __init__(self, item, inventory):
        self.item = item
        self.inventory = inventory

    def execute(self):
        self.item.remove()
        self.inventory.update_inventory(self.item.name, -1)


# Receiver
class Item:

    def __init__(self, name):
        self.name = name

    def add(self):
        print(f"{self.name} is Added")

    def remove(self):
        print(f"{self.name} is Removed")


# Observer
class Inventory:

    def __init__(self):
        self.inventory = {}

    def update_inventory(self, item_name, quantity_change):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity_change
        else:
            self.inventory[item_name] = quantity_change

        print(f"Inventory updated: {item_name} - {self.inventory[item_name]} items")


if __name__ == '__main__':
    inventory_manager = Inventory()

    item1 = Item("Item1")
    add_item1 = Adding(item1, inventory_manager)
    remove_item1 = Removing(item1, inventory_manager)

    cart = Cart()

    cart.add_command(add_item1)
    cart.add_command(remove_item1)

    cart.process_commands()'''

'''#Adaptee
class Bus:

    def __init__(self, name):
        self.name = name

    def increase(self):
        print("Speed increased to 50kmph")

#Adaptee
class Car:

    def __init__(self, name):
        self.name = name

    def accelerate(self):
        print("Speed increased to 70kmph")

#Adaptee
class Bike:

    def __init__(self, name):
        self.name = name

    def speedo(self):
        print("Speed increased to 100kmph")

#Adapter
class AdapterBike:

    def __init__(self, bike):
        self.bike = bike
        self.name = bike.name

    def accelerate(self):
        self.bike.speedo()

#Adapter
class AdapterBus:

    def __init__(self, bus):
        self.bus = bus
        self.name = bus.name

    def accelerate(self):
        self.bus.increase()

#Target
class VehicleDetail:

    def __init__(self):
        pass

    def get_details(self, vehicle):
        print(vehicle.name)
        vehicle.accelerate()

b = Bus('volvo')
c = Car('Lambo')
bi = Bike('yamaha')
l = [c, AdapterBike(bi), AdapterBus(b)]
v = VehicleDetail()
for i in l:
    v.get_details(i)'''

'''#Adaptee
class API1:

    def __init__(self, name):
        self.name = name

    def connect(self):
        print("API1 is Connected Successfully")

#Adaptee
class API2:

    def __init__(self, name):
        self.name = name

    def establish_connection(self):
        print("API2 connection established")

#Target Interface
class Target:

    def request(self):
        pass

#Adapter
class Adapter(Target):

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        if isinstance(self.adaptee, API1):
            self.adaptee.connect()
        elif isinstance(self.adaptee, API2):
            self.adaptee.establish_connection()

def client_code(target):
    target.request()

if __name__ == "__main__":
    api1_instance = API1("API1")
    api2_instance = API2("API2")

    adapter1 = Adapter(api1_instance)
    adapter2 = Adapter(api2_instance)

    print("Client Code using API1: ")
    client_code(adapter1)'''

class AudioPlayer:
    
    def play_audio(self):
        print("Audio is Playing")

class VideoPlayer:

    def play_video(self):
        print("Video is Playing")

class Projector:

    def display(self):
        print("Displayig on Projector")

class MultimediaFacade:

    def __init__(self):
        self.audio_player = AudioPlayer()
        self.video_player = VideoPlayer()
        self.projector = Projector()

    def play_movie(self):
        print("------ Playing Movie ------")
        self.audio_player.play_audio()
        self.video_player.play_video()
        self.projector.display()
        print("------ Movie Finished ------")

multimedia_facade = MultimediaFacade()
multimedia_facade.play_movie()



























