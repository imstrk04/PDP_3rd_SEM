from abc import ABC, abstractmethod
import random

#Receiver
class System:

    def __init__(self):
        self.ticket = []

    def add_ticket(self, ticket):
        self.ticket.append(ticket)

    def remove_ticket(self, ticket):
        self.ticket.pop()

#Icommand Interface
class Icommand(ABC):

    @abstractmethod
    def execute(self):
        pass

#Command1
class Request(Icommand):

    def __init__(self, system, ticket_type, req_no):
        self.system = system
        self.ticket_type = ticket_type
        self.req_no = req_no
    
    def execute(self):
        print(f"Your Request is accepted. Your Request Number is {self.req_no}")
        self.system.add_ticket((self.ticket_type, self.req_no))

#Command2
class Complaint(Icommand):

    def __init__(self, system,ticket_type, comp_no):
        self.system = system
        self.ticket_type = ticket_type
        self.comp_no = comp_no
    
    def execute(self):
        print("Your Complaint is Raised. Your Complaint Number is {self.comp_no}")
        self.system.add_ticket((self.ticket_type, self.comp_no))


#Invoker
class Service_Engineer:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_command(self):
        if self.command:
            self.command.execute()
        else:
            print("No Command Set")


#Driver code
if __name__ == '__main__':
    print("----------------SSNCE HELPDESK-----------------")
    print()
    system = System()
    invoker = Service_Engineer()

    #Request1
    while True:
        check = input("Do you want to exit(y/n): ")
        if check.lower() == 'y':
            print("Thank you for using SSNCE Helpdesk")
            if len(system.ticket) > 0:
                print("Our Service Engineer will look into your Queries")
            break
        else:
            name = input("Do you have a request or complaint: ")
            service = input("What is it about? ")
            tick_num = random.randint(1,1000000)
            print()
            if name.lower() == 'request':
                req = Request(system, service, tick_num)
                print("Initial Tickets:", system.ticket)
                print()
                invoker.set_command(req)
                invoker.execute_command()
                print("After Command:", system.ticket)
                print()
            elif name.lower() == 'complaint':
                comp = Complaint(system, service, tick_num)
                print("Initial Tickets:", system.ticket)
                print()
                invoker.set_command(comp)
                invoker.execute_command()
                print("After Command:", system.ticket)
                print()
            else:
                print("Invalid operation")
                break
            print()
            
    
        
    
