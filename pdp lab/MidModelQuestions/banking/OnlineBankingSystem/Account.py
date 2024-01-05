'''
Accounts module
Author : Dunya Syed Hassan
Date: 22-11-23
'''

from abc import ABC

class Account(ABC):
    
    slots = ['_acc_num','_balance','_acc_holder','bank']

    def displayinfo(self):
        print(f'''
        Bank: {self.bank}
        Account Number: {self._acc_num}
        Account Balance: {self._balance}
        Account Holder: {self._acc_holder._name}'''
        )
    
    def __str__(self):
        return f'''Account Number: {self._acc_num}
        Account Balance: {self._balance}
        Account Holder: {self._acc_holder._name}
        Account Type: {self._acc_type}
        '''
    
    def add_acc_to_customer(self):
        for customer in self.bank.customers:
            if customer == self._acc_holder:
                customer.add_account(self)


class SavingsAccount(Account):

    def __init__(self,bank,acc_num, balance, acc_holder):
        self.bank = bank
        self._acc_num = acc_num
        self._balance = balance
        self._acc_holder = acc_holder
        self._acc_type = 'Savings Account'
        self.add_acc_to_customer()
        self.bank.accounts.append(self)
    
    def displayinfo(self):
        super().displayinfo()
        print('Account Type: Savings Account')


class CheckingAccount(Account):

    def __init__(self,bank,acc_num, balance, acc_holder):
        self.bank=bank
        self._acc_num = acc_num
        self._balance = balance
        self._acc_holder = acc_holder
        self._acc_type = 'Checking Account'
        self.add_acc_to_customer()
        self.bank.accounts.append(self)
    
    def displayinfo():
        super().displayinfo()
        print('Account Type: Checking Account')


