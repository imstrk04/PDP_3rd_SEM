class Emailable():
    def __init__(self, email):
     self.email = email

class MailSender(Emailable):
    def send_mail(self, message):
        self.message=message
        print(f"Sending mail to {self.email=}")

class Contact:
 all_contacts= []
 def __init__(self, name, email):
     self.name = name
     self.email = email
     Contact.all_contacts.append(self)
 def __repr__(self):
     return (f"{self.name}, {self.email}")

'''c_1 = Contact("Dusty", "dusty@example.com")
c_2 = Contact("Steve", "steve@itmaybeahack.com")'''



class EmailableContact(Contact, MailSender):
    pass

e = EmailableContact("John B", "johnb@sloop.net")
print(Contact.all_contacts)
e.send_mail("Hello, test e-mail here")

"""
OUTPUT:
[EmailableContact('John B', 'johnb@sloop.net')]
Sending mail to self.email='johnb@sloop.net'
"""


