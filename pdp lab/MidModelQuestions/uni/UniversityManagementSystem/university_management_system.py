from UniversityManagementSystem.person import Student, Professor
import pickle

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