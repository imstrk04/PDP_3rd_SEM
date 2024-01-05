from threading import Lock, Thread

# State pattern
class State:
    def read(self, reader):
        pass

    def write(self, writer):
        pass

class ReaderState(State):
    def read(self, reader):
        print(f"{reader.name} is reading.")

class WriterState(State):
    def write(self, writer):
        print(f"{writer.name} is writing.")

class Resource:
    def __init__(self):
        self.state = ReaderState()

    def set_state(self, state):
        self.state = state

    def perform_read(self, reader):
        self.state.read(reader)

    def perform_write(self, writer):
        self.state.write(writer)

class Reader:
    def __init__(self, resource, name):
        self.resource = resource
        self.name = name

    def read(self):
        self.resource.perform_read(self)

class Writer:
    def __init__(self, resource, name):
        self.resource = resource
        self.name = name

    def write(self):
        self.resource.perform_write(self)

# Adapter List for NDimensional Arrays
class NDimensionalArrayAdapter:
    def __init__(self, array):
        self.array = array

    def get_value_at_index(self, indices):
        # Implement logic to get value at specified indices
        pass

    def sort(self):
        # Implement sorting logic for NDimensionalArray
        pass

# Strategy Pattern for calculating entity price
class PricingStrategy:
    def calculate_price(self, entity):
        pass

class BasicPricingStrategy(PricingStrategy):
    def calculate_price(self, entity):
        # Basic pricing logic
        pass

class PremiumPricingStrategy(PricingStrategy):
    def calculate_price(self, entity):
        # Premium pricing logic
        pass

class Entity:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy

    def calculate_price(self):
        return self.strategy.calculate_price(self)

# Facade Pattern for student registration
class PersonalDetails:
    pass

class Hobby:
    pass

class ProfessionalBody:
    pass

class StudentFacade:
    def __init__(self):
        self.personal_details = PersonalDetails()
        self.hobby = Hobby()
        self.professional_body = ProfessionalBody()

    def register_student(self, name, age, hobby_details, body_membership):
        # Registration logic
        self.personal_details.name = name
        self.personal_details.age = age
        self.hobby.details = hobby_details
        self.professional_body.membership = body_membership

    def display_details(self):
        # Display student details
        print(f"Name: {self.personal_details.name}")
        print(f"Age: {self.personal_details.age}")
        print(f"Hobby: {self.hobby.details}")
        print(f"Professional Body Membership: {self.professional_body.membership}")


resource = Resource()
reader1 = Reader(resource, "Rajesh")
reader2 = Reader(resource, "Ananya")
writer1 = Writer(resource, "Arjun")

reader1.read()
reader2.read()

writer1.write()

nd_array = NDimensionalArrayAdapter([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
value = nd_array.get_value_at_index((1, 2))
nd_array.sort()

basic_strategy = BasicPricingStrategy()
premium_strategy = PremiumPricingStrategy()
entity1 = Entity("Saree", basic_strategy)
entity2 = Entity("Dance Class", premium_strategy)
price1 = entity1.calculate_price()
price2 = entity2.calculate_price()

student_facade = StudentFacade()
student_facade.register_student("Krishna", 22, "Classical Dance", "Bharatanatyam Academy")
student_facade.display_details()
