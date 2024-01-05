'''
Main module
Author : Dunya Syed Hassan
Date: 22-11-23
'''
import re
from OnlineBankingSystem.Account import SavingsAccount, CheckingAccount
from OnlineBankingSystem.Customers import Customer
from OnlineBankingSystem.Transactions import Deposit,Withdrawal
from OnlineBankingSystem.Bank import Bank

def main():
    dunya = Customer('Dunya',9789067751)
    valli = Customer('Valli', 9940677636)

    kvb = Bank('Karur Vysya Bank','X street, Chennai')
    print('Bank Details:\n')
    kvb.displaydata()

    kvb.add_customer(dunya)
    kvb.add_customer(valli)

    acc1 = SavingsAccount(kvb,1,5000,valli)
    acc2 = CheckingAccount(kvb,6,9000,dunya)
    acc3 = SavingsAccount(kvb,2,6000,dunya)

    kvb.serialize_data()
    print('Bank Details:\n')
    kvb.displaydata()

    dep1 = Deposit(kvb,1,2000)
    with1 = Withdrawal(kvb,6,1000)
    dep2 = Deposit(kvb,2,4000)
    with2 = Withdrawal(kvb,6,100)

    print('Bank Details:\n')
    kvb.displaydata()

    print(' Deposit transactions only')
    for transaction in kvb.transactions:
        if bool(re.findall('\Dep',transaction.type)):
                print(transaction)

main()
