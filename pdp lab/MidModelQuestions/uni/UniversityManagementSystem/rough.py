import pickle
import re
from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, age):
        if not re.match("^[A-Za-z ]+$", name):
            raise ValueError("Invalid Name Format. Please use alphabets")
        self.name = name
        if not re.match("^[0-9]+$"):
            raise ValueError("Invalid Age Format. Please use Numerics.")
        self.age = age
    
    @abstractmethod
    def display_info(self):
        pass

class Student(Person):

    def __init__(self, name, age, courses, dept_name):
        super().__init__(name, age)
        self.details = {}
        self.courses = Courses()
        self.courses.add_course(*courses.items())
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
        Student.__init__(self,name, age)
        Professor.__init__(self,name, age)
    
    def display_info(self):
        return super().display_info()
    
class Courses: 

    def __init__(self):
        self.courses = {}

    def add_course(self, course_name, course_id):
        self.courses[course_name] = course_id

class Departments: 

    def __init__(self):
        self.departments = {}

    def add_course(self, dept_name, dept_id):
        self.departments[dept_name] = dept_id

    
class UniversityManagementSystem:

    def __init__(self):
        self.student = []
        self.professor = []

    def add(self):
        user_type = input("Do you want to enter details of student or professor? ")
        n = int(input(f"How many {user_type} do you want to enter: "))
        for i in range(n):
            name = input(f"Enter {user_type }name{i+1}: ")
            age = input("Enter the age: ")
            course_n = int(input("How many courses are you enrolling: "))
            courses = {}
            for j in range(course_n):
                course_name = input(f"Course {j+1} name ")
                course_id = input(f"Course {j+1} ID: ")
                courses[course_name] = course_id
            dept_name = input("Enter department name: ")
            if user_type.lower() == 'student':
                s = Student(name, age, courses,dept_name)
                self.student.append(s.details)
            elif user_type.lower() == 'professor':
                p = Professor(name, age, courses, dept_name)
                self.professor.append(p.details)
            print()
    
    def serialisation(self):
        person = input("Enter student or professor: ")
        if person.lower() == "student":
            with open("data1.pickle", 'ab') as file:
                pickle.dump(self.student, file)
        elif person.lower() == "professor":
            with open("data2.pickle", 'ab') as file:
                pickle.dump(self.professor, file)
    
    def deserialisation(self):
        person = input("Enter student or professor: ")
        if person.lower() == "student":
            f = open("data1.pickle", 'rb')
            try:
                while (1):
                    d = pickle.load(f)
                    for entry in d:
                        for name, details in entry.items():
                            print(f'Name: {name}')
                            print(f'Age: {details[0]}')
                            for course_name, course_details in details[1].items():
                                print(f'Course Name: {course_name}')
                                print(f'Course ID: {course_details} ')
                            print(f'Department ID: {details[2]}')
                            print()
            except EOFError:
                print("REACHED EOF")
            print("All datas printed\n")
            f.close()
        elif person.lower() == "professor":
            f = open("data2.pickle", 'rb')
            try:
                while (1):
                    d = pickle.load(f)
                    for entry in d:
                        for name, details in entry.items():
                            print(f'Name: {name}')
                            print(f'Age: {details[0]}')
                            for course_name, course_details in details[1].items():
                                print(f'Course Name: {course_name}')
                                print(f'Course ID: {course_details} ')
                            print(f'Department ID: {details[2]}')
                            print()
            except EOFError:
                print("REACHED EOF")
            print("All datas printed\n")
            print(d)
            f.close()
    
    def search_by_name(self):
        user_type = input("Enter student or professor: ")
        if user_type.lower() == 'student':
            stud_name = input("Enter the name to search: ")
            f = open("data1.pickle", 'rb')
            try:
                while (1):
                    d = pickle.load(f)
                    for entry in d:
                        for name, details in entry.items():
                            if name.lower() == stud_name.lower():
                                print(f'Name: {name}')
                                print(f'Age: {details[0]}')
                                for course_name, course_details in details[1].items():
                                    print(f'Course Name: {course_name}')
                                    print(f'Course ID: {course_details} ')
                                print(f'Department ID: {details[2]}')
                                print()
            except EOFError:
                print()
            f.close()
        elif user_type.lower() == 'professor':
            prof_name = input("Enter the name to search: ")
            f = open("data2.pickle", 'rb')
            try:
                while (1):
                    d = pickle.load(f)
                    for entry in d:
                        for name, details in entry.items():
                            if name.lower() == prof_name.lower():
                                print(f'Name: {name}')
                                print(f'Age: {details[0]}')
                                for course_name, course_details in details[1].items():
                                    print(f'Course Name: {course_name}')
                                    print(f'Course ID: {course_details} ')
                                print(f'Department ID: {details[2]}')
                                print()
            except EOFError:
                print()
            f.close()



if __name__ == '__main__':
    u = UniversityManagementSystem()
    u.add()
    print()

    check1 = input("Do you want to store the datas(y/n)? ")
    if check1.lower() == 'y':
        u.serialisation()
    elif check1.lower() == 'n':
        print()
    check2 = input("Do you want to see your details(y/n)? ")
    if check2 == 'y':
        u.deserialisation()
    elif check2 == 'n':
        print()
    u.search_by_name()
    print("THANK YOU FOR USING UNIVERSITY MANAGEMENT SYSTEM")
