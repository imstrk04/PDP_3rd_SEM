from abc import ABC, abstractmethod

#context
class GateState(ABC):

    @abstractmethod
    def enter(self):
        pass
    
    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def payOK(self):
        pass
    
    @abstractmethod
    def payFAILED(self):
        pass

class OpenGateState(GateState):

    def __init__(self, gate):
        print("You are in OpenGateState")
        self.gate = gate
    

class Gate:
    
    def __init__(self):
        self.status = OpenGateState(self)
