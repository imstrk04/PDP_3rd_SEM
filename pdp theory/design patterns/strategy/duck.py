#strategy pattern

from abc import ABC, abstractmethod

class IFlyBehavior(ABC):

    @abstractmethod
    def fly(self):
        ...

class IQuackBehavior(ABC):

    @abstractmethod
    def quack(self):
        ...

class IDisplayBehavior(ABC):

    @abstractmethod
    def display(self):
        ...

class SimpleFlying(IFlyBehavior):

    def fly(self):
        return "I fly Simply"

class NoFlying(IFlyBehavior):

    def fly(self):
        return "I cant Fly"

class JetFlying(IFlyBehavior):

    def fly(self):
        return "I fly like a Jet"
    
class SimpleQuacking(IQuackBehavior):

    def quack(self):
        return "I quack Simply"

class NoQuacking(IQuackBehavior):

    def quack(self):
        return "I dont Quack"

class Duck:

    def __init__(self, duck_type, fly_type, quack_type):
        self.duck_type = duck_type
        self.fly = fly_type()
        self.quack = quack_type()
    
    def show(self):
        print(f'''DUCK DETAILS:
                TYPE: {self.duck_type}
                FLY: {self.fly.fly()}
                QUACK: {self.quack.quack()}''')

d1 = Duck('wild duck', SimpleFlying, SimpleQuacking)
d1.show()
print()

d2 = Duck('city duck', JetFlying, SimpleQuacking)
d2.show()
print()

d3 = Duck('rubber duck', NoFlying, NoQuacking)
d3.show()
print()