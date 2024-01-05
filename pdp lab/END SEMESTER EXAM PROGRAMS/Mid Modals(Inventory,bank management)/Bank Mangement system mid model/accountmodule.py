class account:

    def __init__(self,acc_no,balance,**kwargs):
        self.acc_no=acc_no
        self.balance=balance

    def display(self):
        print(f'{self.acc_no},{self.balance}')


        
