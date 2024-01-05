class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_string(cls, name_string):
        first_name, last_name = name_string.split()
        return cls(first_name, last_name)

# Demonstrate object creation
# Using class function
employee1 = Employee.from_string("John Doe")

# Using instance creation
employee2 = Employee("Alice", "Smith")
