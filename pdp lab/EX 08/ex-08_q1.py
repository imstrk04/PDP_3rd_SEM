# -*- coding: utf-8 -*-
"""
This module provides two classes, PplAsn and PplIterator, and related functions.
It is part of the exercises for the course UIT2312 (Programming and Design Patterns).


The code defines a data structure to store information about people at a college,
along with an iterator to iterate over specific categories. It also provides functions
to add a NewYear bonus to security staff and store the list in an object file using Pickle.

Your comments and suggestions are welcome.
Original Author: T. Sadakopa Ramakrishnan <sadakopa2210221@ssn.edu.in>
"""


import pickle

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

def get_user_input_for_iterator():
    category = input("Enter the category (student/faculty/staff/security): ").lower()
    department = input("Enter the department (optional, press Enter if not applicable): ").lower()
    return category, department if department else None


# Example usage:
people_at_college = []

user_category, user_department = get_user_input_for_iterator()

# Append individuals to the list
people_at_college.append(PplAsn("Sadakopa", "IT", "Student", 25000))
people_at_college.append(PplAsn("Varshini", "CSE", "Faculty", 60000))
people_at_college.append(PplAsn("Vamsi", "Security", "Staff", 30000))
people_at_college.append(PplAsn("Rajeshwari", "ECE", "Faculty", 55000))
people_at_college.append(PplAsn("Karthik", "Civil", "Student", 28000))
people_at_college.append(PplAsn("Malini", "Security", "Staff", 32000))
people_at_college.append(PplAsn("Prasad", "Mechanical", "Faculty", 58000))

# Iterate over a category using iterator
iterator = PplIterator(people_at_college, user_category, department=user_department)
for person in iterator:
    print(person)

# Add NewYear bonus to security staff
add_newyear_bonus(people_at_college)

# Store in an object file using Pickle
store_in_object_file(people_at_college, 'people_at_college_south.pkl')
