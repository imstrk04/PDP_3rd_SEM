
class Contact:
    all_contacts= []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
    def __repr__(self):
        return (f"{self.name}, {self.email}")

c_1 = Contact("Dusty", "dusty@example.com")
c_2 = Contact("Steve", "steve@itmaybeahack.com")
print(Contact.all_contacts)

"""output:
[Contact('Dusty', 'dusty@example.com'), Contact('Steve', 'steve@itmaybeahack.com')]"""
'''
'''
class Contact:
    all_contacts = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
    def __repr1__(self):
        return (f"{self.name}, {self.email}")

c_1 = Contact("Dusty", "dusty@example.com")
c_2 = Contact("Steve", "steve@itmaybeahack.com")
print(Contact.all_contacts)

'''
"""OUTPUT:
[<__main__.Contact object at 0x0000021D55C31FF0>, <__main__.Contact object at 0x0000021D55C32050>]"""

"""
class Contact:
 all_contacts = []
 def __init__(self, name, email) -> None:
     self.name = name
     self.email = email
     Contact.all_contacts.append(self)
 def __repr__(self):
     return (f"{self.__class__.__name__}("f"{self.name!s}, {self.email!s})")

c_1 = Contact("Dusty", "dusty@example.com")
c_2 = Contact("Steve", "steve@itmaybeahack.com")
print(Contact.all_contacts)

"""
"""OUTPUT:
[Contact(Dusty, dusty@example.com), Contact(Steve, steve@itmaybeahack.com)]
"""

'''
class Contact:
 all_contacts = []
 def __init__(self, name, email):
     self.name = name
     self.email = email
     self.all_contacts.append(self)
 def __repr__(self):
     return (f"{self.name}, {self.email}")

c_1 = Contact("Dusty", "dusty@example.com")
c_2 = Contact("Steve", "steve@itmaybeahack.com")
print(c_1.name)
print(c_1.email)
print(c_2.name)
print(c_2.email)
print(Contact.all_contacts)


"""
OUTPUT:
Dusty
dusty@example.com
Steve
steve@itmaybeahack.com
[Contact('Dusty', 'dusty@example.com'), Contact('Steve', 'steve@itmaybeahack.com')]
"""
