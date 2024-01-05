from abc import ABC, abstractmethod

class Sportsman(ABC):
    @abstractmethod
    def GetSportsDetails(self):
        pass

    @abstractmethod
    def DisplaySportsDetails(self):
        pass

class Student(ABC):
    def __init__(self, student_name, contact, age):
        self.student_name = student_name
        self.contact = contact
        self.age = age

    @abstractmethod
    def GetStudentDetails(self):
        pass

    @abstractmethod
    def DisplayStudentDetails(self):
        pass

class SportsStudent(Sportsman, Student):
    def __init__(self, student_name, contact, age, teamname, captain, coachname):
        super().__init__(student_name, contact, age)  
        self.teamname = teamname
        self.captain = captain
        self.coachname = coachname

    def GetStudentDetails(self):
        return f"{self.student_name}, {self.contact}, {self.age}"

    def GetSportsDetails(self):
        return f"{self.teamname}, {self.captain}, {self.coachname}"

    def DisplaySportsDetails(self):
        print("Sports Details:")
        print(self.GetSportsDetails())

    def DisplayStudentDetails(self):
        print("Student Details:")
        print(self.GetStudentDetails())

    def GetData(self):
        student = self.GetStudentDetails() 
        sports = self.GetSportsDetails()  
        print(f"Student detail: {student}, Sports detail: {sports}")




s = SportsStudent('Srihari', '988****', 17, 'ABC', 'XYZ', 'Dhoni')
print(s.GetData())


student_list = [
    SportsStudent('Srihari', '988****', 17, 'ABC', 'XYZ', 'Dhoni'),
    SportsStudent('Srihari', '988****', 17, 'ABC', 'XYZ', 'abc')
]

for i in student_list:
    if i.coachname == 'Dhoni':  
        i.GetData() 

