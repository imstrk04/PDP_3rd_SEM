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


class DoorDelivery:

    def __init__(self):
        self.observers=[]
        self.orders={}
        self.order_no=0

    def add_observer(self,observer):
        self.observers.append(observer)

    def remove_observer(self,observer):
        self.observers.remove(observer)

    def notify_observer(self,message):
        for observer in self.observers:
            observer.update(message)

    def place_order(self,vegetable_list):
        self.order_no+=1
        if self.order_no not in self.orders:
            self.orders[self.order_no]={'Vegetables' : vegetable_list}
            self.notify_observer(f' order placed for the veggielist {vegetable_list} it will arive in 30 min')
            print(f'your order no is {self.order_no}')

    def pay_bill(self,order_no):
        if order_no in self.orders:
            sum_price=0
            for item in self.orders[order_no]['Vegetables']:
                sum_price+=item['price']
            if sum_price > 100:
                self.notify_observer(f' bill payed for the order_no : {order_no} bill amount : {sum_price}')
  
            
#observers 
class customer:
    def __init__(self,name):
        self.name=name

    def update(self,message):
        print(f'{self.name} received a notification : {message}')

class Vendor:

    def update(self,message):
        print(f'Vendor received a notification : {message}')

c1=customer('srihari')
vendor=Vendor()
Doordelv=DoorDelivery()
Doordelv.add_observer(c1)
Doordelv.add_observer(vendor)
Doordelv.place_order([{'name':'carrot','qty':5,'price':80}])
Doordelv.place_order([{'name':'beetroot','qty':5,'price':80},{'name':'carrot','qty':5,'price':80}])
Doordelv.pay_bill(2)
