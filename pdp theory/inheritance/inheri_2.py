#BASIC INHERITANCE 

class Contact:
    all_contacts= []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
    def __repr__(self):
        return (f"{self.name}, {self.email})")

class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send "f"'{order}' order to '{self.name}' and mail @ '{self.email}'")
 
c_1 = Contact("Dusty", "dusty@example.com")
c_2 = Contact("Steve", "steve@itmaybeahack.com")
s_1 = Supplier("Bob", "bob@supplies.com")
print(Contact.all_contacts)

"""
OUTPUT:
[Contact('Dusty', 'dusty@example.com'), Contact('Steve', 'steve@itmaybeahack.com'), Supplier('Bob', 'bob@supplies.com')]
"""

'''c_1.order("100 apples")'''

"""
OUTPUT:
[Contact('Dusty', 'dusty@example.com'), Contact('Steve', 'steve@itmaybeahack.com'), Supplier('Bob', 'bob@supplies.com')]
Traceback (most recent call last):
  File "C:/Users/SSN/AppData/Local/Programs/Python/Python310/inheri_2.py", line 25, in <module>
    c_1.order("100 apples")
AttributeError: 'Contact' object has no attribute 'order'
"""

#s_1.order("100 apples")

"""
OUTPUT:

[Contact('Dusty', 'dusty@example.com'), Contact('Steve', 'steve@itmaybeahack.com'), Supplier('Bob', 'bob@supplies.com')]
If this were a real system we would send '100 apples' order to 'Bob' and mail @ 'bob@supplies.com'

"""


