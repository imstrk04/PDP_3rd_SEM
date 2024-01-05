'''
SADAKOPA RAMAKRISHNAN T
ex 5 pdp lab qn 2
Create a class ‘Employee’. The constructor must assign the first name and last name of an employee. 
Define a function called from_string() which gets a single string from the user, splits and assigns to the 
first and last name. For example, if the string is ‘Seetha Raman’, the function should assign first name 
as Seetha and second name as Raman and the function returns the object. Can you design from_string()
as a class or instance function? Justify your response'''


class Employee:
    """Stores the details of an employee"""

    def __init__(self, fname=None, lname=None):
        """Constructor of the Employee class"""
        self.fname = fname
        self.lname = lname

    @classmethod
    def from_string(cls, name):
        """Create an Employee object from a full name string."""
        fname, lname = name.split()
        return cls(fname, lname)

    def __str__(self):
        """Return a string representation"""
        return "\nfirst name: {}\nlast name: {}\n".format(self.fname, self.lname)

if __name__ == "__main__":
    # Create Employee objects
    emp1 = Employee.from_string(input("\nEnter employee 1 full name: "))
    emp2 = Employee()
    emp2.from_string(input("\nEnter employee 2 full name: "))
    fname = input("\nEnter employee 3 first name: ")
    lname = input("Enter employee 3 last name: ")
    emp3 = Employee(fname, lname)

    # Display the employee details
    print("\nEmployee details:")
    print(emp1)
    print(emp2)
    print(emp3)
