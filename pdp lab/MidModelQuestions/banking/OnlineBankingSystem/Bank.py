'''
Bank module
Author : Dunya Syed Hassan
Date: 22-11-23
'''
import pickle

class Bank:

    def __init__(self,name,address):
        self._name = name
        self._address = address
        self.accounts=[]
        self.customers = []
        self.transactions = []
    
    def add_customer(self,customer):
        self.customers.append(customer)
    
    
    def serialize_data(self):

        customer_data=''
        for customer in self.customers:
            customer_data = customer_data+ '\n' + customer.__str__()
        with open('customer.pickle','wb') as file:
            pickle.dump(customer_data,file)
        
        acc_data=''
        for account in self.accounts:
            acc_data = acc_data+ '\n' + account.__str__()
        with open('accounts.pickle','wb') as file:
            pickle.dump(acc_data,file)

        transaction_data=''
        for transaction in self.transactions:
            transaction_data = transaction_data + '\n' + transaction.__str__()
        with open('transactions.pickle','wb') as file:
            pickle.dump(transaction_data,file)
    
    def displaydata(self):

        with open('customer.pickle','rb') as file:
            customer_data = pickle.load(file)
        print('Customer data:\n',customer_data)

        with open('accounts.pickle','rb') as file:
            acc_data = pickle.load(file)
        print('Account data:\n',acc_data)

        with open('transactions.pickle','rb') as file:
            transaction_data = pickle.load(file)
        print('Transaction data:\n',transaction_data)
