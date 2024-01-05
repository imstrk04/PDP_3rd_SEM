# Iterator Pattern
from typing import Iterable, Iterator

class Student:

    def __init__(self, name, age, club):
        self.name = name
        self.age = age
        self.club = club

    def display(self):
        print(f'NAME : {self.name} AGE : {self.age} CLUB : {self.club}')

# Creating Student Iterable
class StudentIterable(Iterable[Student]):

    def __init__(self, *args):
        self.students = [*args]

    def add_student(self, student):
        self.students.append(student)

    def __iter__(self):
        return StudentIterator(self.students)

class StudentIterator(Iterator[Student]):

    def __init__(self, lst):
        self.student_list = [x for x in lst if x.club == 'NSO']
        self.index = 0

    def __next__(self):
        if self.index < len(self.student_list):
            current = self.student_list[self.index]
            self.index += 1
            return current
        else:
            raise StopIteration

s1 = Student('srihari', 18, 'NSO')
s2 = Student('venkat', 19, 'NSO')
s3 = Student('abc', 20, 'NSS')

iterable = StudentIterable(s1, s2, s3)

# Now, let's iterate over the students and display their information
for student in iterable:
    student.display()
