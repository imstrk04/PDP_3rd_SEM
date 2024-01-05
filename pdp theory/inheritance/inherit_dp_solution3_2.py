#MULTIPLE INHERTIANCE AND MULTIPLE ARGUMENTS
class Contact:
 all_contacts = []
 def __init__(self,name, email):
     self.name = name
     self.email = email
     Contact.all_contacts.append(self)
 def __repr__(self):
     return (f"{self.name}, {self.email}")

class AddressHolder:
    def __init__(self,street, city, state, code):
        
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):
    def __init__(self,name, email, phone, street, city, state, code):
        super().__init__(phone, email)
        self.phone = phone
        Contact.__init__(self,name,email)
        AddressHolder.__init__(self,street, city, state, code)

c1 = Contact("Dusty", "dusty@example.com")
c2 = Contact("Steve", "steve@itmaybeahack.com")
f1=Friend("John", "john@gmail.com","123456789","street1", "city1", "state1", "12345")

print(Contact.all_contacts)
print(f1.street)


"""
Output:
[Contact('Dusty', 'dusty@example.com'), Contact('Steve', 'steve@itmaybeahack.com'), Friend('John', 'john@gmail.com'), Friend('John', 'john@gmail.com')]
street1"""