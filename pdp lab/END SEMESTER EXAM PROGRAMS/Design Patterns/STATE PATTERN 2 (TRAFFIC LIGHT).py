#Traffic light system using state pattern
from abc import ABC,abstractmethod

#abstract state
class state(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def transition(self):
        pass
    
#concrete states
class redstate(state):

    def go(self):
        print('dont go on red')

    def stop(self):
        print('stop on red')

    def transition(self):
        print('switching state')
        return greenstate()
    
class greenstate(state):

    def go(self):
        print('you can go')

    def stop(self):
        print(' no need to stop on green')

    def transition(self):
        print('switching to state')
        return yellowstate()


    
class yellowstate(state):
    
    def go(self):
        print("Cannot go on yellow light.")

    def stop(self):
        print("Must stop on yellow light.")

    def transition(self):
        print("Changing from yellow to red.")
        return redstate()

#client
class trafficsystem:
    def __init__(self):
        self.state=redstate()

    def go(self):
        self.state.go()

    def stop(self):
        self.state.stop()

    def transition(self):
        self.state = self.state.transition()

#driver code
light=trafficsystem()
light.go()
light.transition()
light.go()


        

    

