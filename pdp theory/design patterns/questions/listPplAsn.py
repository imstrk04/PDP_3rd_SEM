class Person:

    def __init__(self, name, category, department = None, salary = 0):
        self.name = name
        self.category = category
        self.department = department
        self.salary = salary

class Iterable:

    def create_iterator(self):
        pass

class Iterator:

    def has_next():
        pass

    def next():
        pass

class List(Iterable):

    def __init__(self):
        self.list = []
    
    def create_iterator(self):
        return ListIterator(self)
    
    def attach(self, item):
        self.list.append(item)

class ListIterator(Iterator):

    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0
    
    def has_next(self):
        return self.index < len(self.iterable.list)
    
    def next(self):
        if self.has_next():
            value = self.iterable.list[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration("No more elements")
        
if __name__ == '__main__':
    PplAsn = List()
    n = int(input("Enter number of inputs: "))
    for i in range(n):
        name = input("Enter Name: ")
        category = input("Student/ Faculty: ")
        department = input("Department: ")
        person = Person(name, category, department)
        PplAsn.attach(person)
    
    category_choice = input("Enter category of your choice: ")
    iterator = PplAsn.create_iterator()

    while iterator.has_next():
        person = iterator.next()
        if person.category.lower() == category_choice.lower():
            # Add New Year bonus of Rs 2000 to the salary of security personnel
            if person.department.lower() == category_choice.lower():
                person.salary += 2000
            print(f"{person.name} - {person.category} ({person.department}) - Salary: Rs {person.salary}")
    

    