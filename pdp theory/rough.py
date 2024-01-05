'''def my_generator(n):
    value = 0

    while value < n:

        yield value
        value += 1

for value in my_generator(3):
    print(value)

#------------------------------------

squares_generator = (i*i for i in range(5))

for i in squares_generator:
    print(i)'''

'''def fib(limit):
    a = 0
    b = 1
    while a < limit:
        yield a
        a = b
        b = a + b

x = fib(5)

print(next(x))
print(next(x))
print(next(x))
print(next(x))

print("\nUsing for Loop:")
for i in fib(5):
    print(i)'''

'''my_list = [4, 7, 0, 3]

my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())
print(my_iter.__next__())

next(my_iter)'''

'''my_list = [4, 7, 0, 3]
my_iter = iter(my_list)

while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break'''
'''
#Defining Iterable Interface
class Iterable:
    def create_iterator(self):
        pass


#Defining an Iterator Interface
class Iterator:
    def has_next(self):
        pass

    def next(self):
        pass

# Concrete implementation of an iterable
class ConcreteIterable(Iterable):
    def __init__(self):
        self._data = [1, 2, 3, 4, 5]
    
    def create_iterator(self):
        return ConcreteIterator(self)

# Concrete Implementation of an iterator
class ConcreteIterator(Iterator):
    def __init__(self, iterable):
        self._iterable = iterable
        self._index = 0
    
    def has_next(self):
        return self._index < len(self._iterable._data)

    def next(self):
        if self.has_next():
            value = self._iterable._data[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration("No more elements")

#Driver Code
iterable = ConcreteIterable()
iterator = iterable.create_iterator()

while iterator.has_next():
    value = iterator.next()
    print(value)'''

'''from typing import Iterable, Iterator

class Student:

    def __init__(self, name, mark, club):
        self.name = name
        self.mark = mark
        self.club = club
    
    def __str__(self):
        result = self.name + '\n' + str(self.mark) +'\n' + self.club
        return result

class iterable_student(Iterable):

    def __init__(self, *args):
        self.student_list = [*args]
    
    def append(self, obj):
        self.student_list.append(obj)
    
    def __iter__(self):
        return iterator_student(self.student_list)

class iterator_student(Iterator[str]):

    def __init__(self, iterable_list):
        self.iterator_list = [x for x in iterable_list if x.club == 'nss']
        self.index = 0
    
    def __next__(self):
        if self.index < len(self.iterator_list):
            x = self.iterator_list[self.index]
            self.index += 1
            return x
        else:
            raise StopIteration("No More Elements")

a = Student('xyz1', 10,'nss')
b = Student('xyz2',20,'nso')
c = Student('xyz3',30,'yrc')
d = Student('xyz4',40,'nss')
e = Student('xyz5',50,'nso')

iterable_student_list=iterable_student(a,b,c,d)
iterable_student_list.append(e)

for i in iterable_student_list:
    print(i)'''

'''import pickle

class PplAsn:
    def __init__(self, name, department, role, salary):
        self.name = name
        self.department = department
        self.role = role
        self.salary = salary

class PplIterator:
    def __init__(self, ppl_list, category, department=None):
        self.ppl_list = ppl_list
        self.category = category.lower()
        self.department = department.lower() if department else None
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.ppl_list):
            person = self.ppl_list[self.index]
            self.index += 1

            if (self.category == 'student' and person.role.lower() == 'student') or \
               (self.category == 'faculty' and person.role.lower() == 'faculty') or \
               (self.category == 'staff' and person.role.lower() == 'staff') or \
               (self.category == 'security' and person.role.lower() == 'security'):
                if self.department and person.department.lower() != self.department:
                    continue
                return person.name

        raise StopIteration

def add_newyear_bonus(ppl_list):
    for person in ppl_list:
        if person.role.lower() == 'security':
            person.salary += 2000

def store_in_object_file(ppl_list, filename):
    with open(filename, 'wb') as file:
        pickle.dump(ppl_list, file)

# Example usage:
people_at_college = []

# Append individuals to the list
people_at_college.append(PplAsn("John Doe", "IT", "Student", 25000))
people_at_college.append(PplAsn("Jane Smith", "CSE", "Faculty", 60000))
people_at_college.append(PplAsn("Bob Johnson", "Security", "Staff", 30000))

# Iterate over a category using iterator
iterator = PplIterator(people_at_college, 'student')
for person in iterator:
    print(person)

# Add NewYear bonus to security staff
add_newyear_bonus(people_at_college)

# Store in an object file using Pickle
store_in_object_file(people_at_college, 'people_at_college.pkl')
'''

'''import re
import json

def check_gmail(gmail):
    pattern = r"^[a-zA-Z0-9]+(@*)[a-zA-z0-9]+(.*)[a-zA-Z0-9]$"
    if re.match(pattern, gmail):
        return True
    else:
        return MailError("Invalid Gmail")

check_gmail("sadakopa2210221@ssn.edu.in")


def check_password(password):
    if (len(password) < 8):
        return "Invalid Format!"
    
    elif not re.search(r"[a-z]", password):
        return "Invalid Format!"
    
    elif not re.search(r"[A-Z]", password):
        return "Invalid Format!"
    
    elif not re.search(r"[0-9]", password):
        return "Invalid Format!"
    
    elif not re.search(r"[_!@#$%^&]", password):
        return "Invalid Format!"
    
    elif re.search(r"\s", password):
        return "Invalid Format!"
    
    else:
        return True

def store_login(data):
    with open("user_login_details.json", "w") as file:
        json.dump(user_login_details, file)

def load_login():
    with open("user_login_details.json", "r") as file:
        data = json.load(file)
    return data



class MailError(Exception):
    pass

class PassError(Exception):
    pass

user_login_details = {}

gmail = input("Enter your gmail: ")
if check_gmail(gmail):
    password = input("Enter your password: ")
    if check_password(password):
        user_login_details = load_login()
        user_login_details[gmail] = password
        store_login(user_login_details)

print(user_login_details)'''
'''
string = "The quick brown\nfox jumps* over the lazy dog."
pattern = r'\n(*)'
string.replace(r'\n'," ")
print(string)'''

'''import asyncio

async def main():
    task = asyncio.create_task(other_function())
    print("A")
    print("B")
    await task

async def other_function():
    print("1")
    await asyncio.sleep(2)
    print("2")

asyncio.run(main())'''

print("version1")