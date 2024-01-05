from abc import ABC, abstractmethod

class account(ABC):
    __slots__ = ['acc_no', 'bal']

    def __init__(self, accno, bal):
        self.acc_no = accno
        self.bal = bal

    def __str__(self):
        return str(self.acc_no)
    
    @property
    @abstractmethod
    def rate(self)-> str:
        ...

    @abstractmethod
    def calc_interest(self):
        ...

class sav_acc(account):

    rate = 7

    def calc_interest(self, prd):
        amount = (self.rate*self.bal*prd)/100
        return amount 
    
if __name__ == "__main__":
    a1 = sav_acc(123,300)
    print(a1)
    print(isinstance(a1, object))
    print(a1.calc_interest(12))
    l1 = [23, 'x']
    print(isinstance(l1,list))