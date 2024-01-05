from accountmodule import account

class savings_account(account):

    def __init__(self,acc_no,balance,acc_holder,**kwargs):
        super().__init__(acc_no,balance)
        self.acc_holder=acc_holder

    def display(self):
        super().display()
        print(f'{self.acc_holder}')
        

