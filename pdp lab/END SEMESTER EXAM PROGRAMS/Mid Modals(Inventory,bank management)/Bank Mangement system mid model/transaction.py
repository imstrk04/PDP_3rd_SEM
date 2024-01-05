from accountmodule import account

class Transaction(account):

    def __init__(self,acc_no,balance,transaction_id,**kwargs):
        super().__init__(acc_no,balance,**kwargs)
        self.transaction_id=transaction_id

    def deposit(self,amount):
        self.balance+=amount
        print(f' reamaining balance :{self.balance}')

    def withdraw(self,amount):
        self.balance-=amount
        print(f' reamaining balance :{self.balance}')

    def display(self):
        return f"{self.acc_no},{self.balance},{self.transaction_id}"

        
        
