'''
Customers module
Author : Dunya Syed Hassan
Date: 22-11-23
'''

class Customer:

    def __init__(self,name,phone_num):
        self._name = name
        self._phone_num = phone_num
        self.accounts=[]

    def __str__(self):
        acc_nums = []
        for acc in self.accounts:
            acc_nums.append(acc._acc_num)
        return f'''
        Name: {self._name}
        Phone Number: {self._phone_num}
        Account Numbers: {acc_nums}'''
    
    def add_account(self,account):
        self.accounts.append(account)
        print('Account added')
    
        