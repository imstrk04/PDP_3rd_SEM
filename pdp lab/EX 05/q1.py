class ElectronicDevice:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def turn_on(self):
        print(f"{self.brand} {self.model} is turning on.")

    def turn_off(self):
        print(f"{self.brand} {self.model} is turning off.")

class Phone(ElectronicDevice):
    def __init__(self, brand, model, is_smartphone=True):
        super().__init__(brand, model)
        self.is_smartphone = is_smartphone

    def make_call(self):
        print(f"{self.brand} {self.model} is making a call.")

class Laptop(ElectronicDevice):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size

    def open_browser(self):
        print(f"{self.brand} {self.model} is opening a web browser.")

class Smartphone(Phone):
    def __init__(self, brand, model, is_smartphone=True, has_touch_screen=True):
        super().__init__(brand, model, is_smartphone)
        self.has_touch_screen = has_touch_screen

    def send_text(self):
        print(f"{self.brand} {self.model} is sending a text message.")

# MRO for Smartphone class
print(Smartphone.mro())
          