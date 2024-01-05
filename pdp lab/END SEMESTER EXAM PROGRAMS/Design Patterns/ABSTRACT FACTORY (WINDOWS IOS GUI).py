from abc import ABC, abstractmethod

# Abstract product A
class Button(ABC):

    @abstractmethod
    def click(self):
        pass

# Concrete products
class WindowsButton(Button):

    def click(self):
        print('Windows button clicked!')

class iOSButton(Button):

    def click(self):
        print('iOS button clicked!')

# Abstract product B
class Textfield(ABC):

    @abstractmethod
    def text(self):
        pass

# Concrete products
class Windowsfield(Textfield):

    def text(self):
        print('Windows text field sent!')

class iOSfield(Textfield):

    def text(self):
        print('iOS text field sent!')

# Abstract Factory
class UIfactory(ABC):

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_textfield(self):
        pass

# Concrete Factories
class WindowsUIfactory(UIfactory):

    def create_button(self):
        return WindowsButton()

    def create_textfield(self):
        return Windowsfield()

class iOSUIfactory(UIfactory):

    def create_button(self):
        return iOSButton()

    def create_textfield(self):
        return iOSfield()

# Client
class GUI:
    def __init__(self, factory):
        self.button = factory.create_button()
        self.textfield = factory.create_textfield()

# Driver code
windows_factory = WindowsUIfactory()
iOS_factory = iOSUIfactory()

windows_gui = GUI(windows_factory)
ios_gui = GUI(iOS_factory)

windows_gui.button.click()
windows_gui.textfield.text()

ios_gui.button.click()
ios_gui.textfield.text()




