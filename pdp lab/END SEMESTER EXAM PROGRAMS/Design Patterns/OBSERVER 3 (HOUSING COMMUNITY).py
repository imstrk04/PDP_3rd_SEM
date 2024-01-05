#observer pattern hosuing community
from abc import ABC,abstractmethod
#abstract classes
class observable(ABC):

    @abstractmethod
    def add_observer(self):
        pass
    @abstractmethod
    def remove_observer(self):
        pass
    @abstractmethod
    def notify_observer(self):
        pass
    
class observer(ABC):

    @abstractmethod
    def update(self):
        pass


class HousingCommunity:

    def __init__(self):
        self.observers=[]
        self.occupied_flats={}

    def add_observer(self,observer):
        self.observers.append(observer)

    def remove_observer(self,observer):
        self.observers.remove(observer)

    def notify_observer(self,message):
        for i in self.observers:
            i.update(message)

    def occupy_flat(self,flat_no,bhk):
        if flat_no not in self.occupied_flats:
            self.occupied_flats[flat_no]={'bhk':bhk,'occupied':True}
            self.notify_observer(f'{flat_no} with {bhk} bhk occupied !')
            
    def vacate_flat(self, flat_no):
        if flat_no in self.occupied_flats:
            bhk = self.occupied_flats.pop(flat_no)['bhk']
            self.notify_observer(f'{flat_no} vacated')
            self.occupied_flats[flat_no] = {'bhk': bhk, 'occupied': False}


    def get_occupied_flats(self):
        occupied=[flat_no for flat_no,details in self.occupied_flats.items() if details['occupied']]
        return occupied 
                  
            

class resident:

    def __init__(self,name):
        self.name=name

    def update(self,message):
        print(f'{self.name} received a notification : {message}')

r1=resident('srihari')
HC=HousingCommunity()
HC.add_observer(r1)
HC.occupy_flat(101,3)
HC.vacate_flat(101)
print(HC.get_occupied_flats())
