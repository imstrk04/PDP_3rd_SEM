#INVENTORY MANAGEMENT SYSTEM
'''from abc import ABC, abstractmethod
import pickle
import re

class Product(ABC):

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category 

    def display_info(self):
        display = f"Name of the product is {self.name} and its price is Rs. {self.price}"
        return display
    
class Electronics(Product):

    def __init__(self, name, price, category):
        super().__init__(name, price, category)

    def display_info(self):
        display = f"Name of the Electronics is {self.name} and its price is Rs. {self.price}"
        return display

class Clothing(Product):

    def __init__(self, name, price, category):
        super().__init__(name, price, category)
    
    def display_info(self):
        display = f"Name of the Cloth is {self.name} and its price is Rs. {self.price}"
        return display

class Diwali(Electronics, Clothing):
    
    def __init__(self, name, price, category):
        super().__init__(name, price, category)
    
    def display_info(self):
        #display = f"Its Diwali Time, You get {self.name} for Rs. {self.price}"
        #return display 
        return super().display_info()

def serialize_data(data):
    with open("data.pickle", 'wb') as file:
        pickle.dump(data, file)

def deserialize_data():
    f1 = open("data.pickle", "rb")

    try:
        while (1):
            d = pickle.load(f1)
            print(d)
    except EOFError:
        print("Reached EOF")
    print("All datas printed\n")
    f1.close()

def perform_string_operations(data):
    print("String Operations and Regular Expressions:\n")

    search_term = "Speakers"
    matching_products = [product for product in data if product['name'].startswith(search_term)]
    print(f"Products starting with 'Speakers': {matching_products}\n")

    category_filter1 = "Electronics"
    electronics_product = [product for product in data if category_filter1 in product['category']]
    print("Electronic Products:", electronics_product,"\n")

    category_filter2 = "Clothing"
    clothing_product = [product for product in data if category_filter2 in product['category']]
    print("Clothing Products:", clothing_product,"\n")

    pattern = re.compile(r'T-Shirt', re.IGNORECASE)
    matching_products = [product for product in data if re.search(pattern, product['name'])]
    print("Matching Products:", matching_products)

if __name__ == '__main__':
    print("Product Class")
    p = Product("Household", 2500, "Electronics")
    print(p.display_info() + "\n")

    print("Electronics Class")
    e = Electronics("JBL", 1000,"Electronics")
    print(e.display_info() + '\n')

    print("Clothing Class")
    c = Clothing("Jeans", 1500, "Clothing")
    print(c.display_info() + "\n")

    print("Diamond Problem")
    d = Diwali("Alexa", 1200,"Electronics")
    print(d.display_info())
    print("MRO of Diwali class", end = " ")
    print(Diwali.__mro__)

    print("Searialisation:")
    data = []
    p1 = {'name' : "Speakers", 'price' : 2000, "category" : "Electronics"}
    p2 = {'name' : "Keyboard", 'price' : 1500, "category" : "Electronics"}
    p3 = {'name' : "T-Shirt", 'price' : 600,"category" : "Clothing"}
    p4 = {'name' : "Track Pants", 'price' : 600, "category" : "Clothing"}
    p5 = {'name' : "Mouse", 'price' : 700, "category" : "Electronics"}

    data.append(p1)
    data.append(p2)
    data.append(p3)
    data.append(p4)
    data.append(p5)

    serialize_data(data)
    
    deserialize_data()

    perform_string_operations(data)'''

#BANKING SYSTEM
'''from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance
    
    def display_info(self):
        display = f"Your Account Number is {self.acc_no} and Your Remaining Balance is Rs. {self.balance}\n"
        return display
    
class SavingsAccount(Account):

    def __init__(self, acc_no, balance):
        super().__init__(acc_no, balance)
    
    def display_info(self):
        display = f"You are accessing Savings Account {self.acc_no}\nRemaining Balance is Rs. {self.balance}\n"
        return display

class CheckingAccount(Account):

    def __init__(self, acc_no, balance):
        super().__init__(acc_no, balance)
    
    def display_info(self):
        display = f"You are accessing Checking Account {self.acc_no}\nRemaining Balance is Rs. {self.balance}\n"
        return display
    
class Transactions:

    def __init__(self, trans_type, amount, timestamp):
        self.trans_type = trans_type
        self.amount = amount
        self.timestamp = timestamp
    
    def display_info(self):
        display = f"You are currently {self.trans_type}ing Rs. {self.amount} at {self.timestamp}\n"
        return display

class Deposit(Transactions):

    def __init__(self, trans_type, amount, timestamp,deposit_method):
        super().__init__(trans_type, amount, timestamp)
        self.deposit_method = deposit_method
    
    def display_info(self):
        display = f"Deposited {self.amount} at {self.timestamp} via {self.deposit_method}\n"
        return display

class Withdrawl(Transactions):

    def __init__(self, trans_type, amount, timestamp, withdrawl_method):
        super().__init__(trans_type, amount, timestamp)
        self.withdrawl_method = withdrawl_method
    
    def display_info(self):
        display = f"Withdrawn {self.amount} at {self.timestamp} via {self.withdrawl_method}\n"
        return display
    
class BankingSystem:

    def __init__(self):
        self.amount = {}
        self.transaction = []

    def operation(self,type, account, transaction, amount):
        if isinstance(account, Account) and isinstance(transaction, Transactions):
            if type.lower() == 'deposit':
                account.balance += amount
            elif type.lower() == 'withdraw':
                if account.balance - amount > 0:
                    account.balance -= amount
                else:
                    print("INSUFFICIENT FUNDS")
                    return
            '''
class A:
    def __init__(self, a_value):
        self.a_value = a_value

    def display(self):
        print(f"A: {self.a_value}")

class B(A):
    def __init__(self, a_value, b_value):
        super().__init__(a_value)
        self.b_value = b_value

    def display(self):
        super().display()
        print(f"B: {self.b_value}")

class C(A):
    def __init__(self, a_value, c_value):
        super().__init__(a_value)
        self.c_value = c_value

    def display(self):
        super().display()
        print(f"C: {self.c_value}")

class D(B, C):
    def __init__(self, a_value, b_value, c_value, d_value):
        # Using **kwargs to handle potential conflicts
        super().__init__(a_value=a_value, b_value=b_value, c_value=c_value)
        self.d_value = d_value

    def display(self):
        super().display()
        print(f"D: {self.d_value}")

# Example usage
d_object = D(a_value=1, b_value=2, c_value=3, d_value=4)
d_object.display()
