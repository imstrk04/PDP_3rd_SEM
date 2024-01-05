'''
Transactions module
Author : Dunya Syed Hassan
Date: 22-11-23
'''

from datetime import datetime

class Transaction:

    slots = ['acc_num','amount','bank']

    def __str__(self):
        return f'''
        Account Number:{self.acc_num}
        Amount: {self.amount}
        Transaction Type: {self.type}
        Transaction Time: {self.timestamp}
        '''

class Deposit(Transaction):

    def __init__(self,bank,acc_num,amount):
        self.bank = bank
        self.acc_num = acc_num
        self.amount = amount
        self.type = 'Deposit'
        self.timestamp = datetime.now()
        self.deposit()
        self.bank.transactions.append(self)

    def deposit(self):
        for account in self.bank.accounts:
            if account._acc_num == self.acc_num:
                account._balance += self.amount
        self.bank.serialize_data()
        print('Transaction Successful')
    

class Withdrawal(Transaction):

    def __init__(self,bank,acc_num,amount):
        self.bank = bank
        self.acc_num = acc_num
        self.amount = amount
        self.type = 'withdrawal'
        self.timestamp = datetime.now()
        self.withdraw()
        self.bank.transactions.append(self)

    def withdraw(self):
        for account in self.bank.accounts:
            if account._acc_num == self.acc_num:
                account._balance -= self.amount
        self.bank.serialize_data()
        print('Transaction Successful')
