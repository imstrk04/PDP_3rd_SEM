import re
from UniversityManagementSystem.courses import Courses
from UniversityManagementSystem.departments import Departments
from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, age):
        if not re.match("^[A-Za-z ]+$", name):
            raise ValueError("Invalid Name Format. Please use alphabets")
        self.name = name
        if not re.match("^[0-9]+$", age):
            raise ValueError("Invalid Age Format. Please use Numerics.")
        self.age = age
    
    @abstractmethod
    def display_info(self):
        pass

class Student(Person):

    def __init__(self, name, age, courses, dept_name):
        super().__init__(name, age)
        self.details = {}
        self.details[self.name] = [age,courses,dept_name]


    def display_info(self):
        print(f'''
                Student Details 
                Name : {self.name}
                Age : {self.age}''')

class Professor(Person):

    def __init__(self, name, age, courses, dept_name):
        super().__init__(name, age)
        self.details = {}
        self.details[self.name.title()] = [age, courses,dept_name]
    
    def display_info(self):
        print(f'''
                Professor Details 
                Name : {self.name}
                Age : {self.age}''')

class TeachingAssistant(Student, Professor):

    def __init__(self, name, age):
        super().__init__(name,age)
    
    def display_info(self):
        return super().display_info()
    