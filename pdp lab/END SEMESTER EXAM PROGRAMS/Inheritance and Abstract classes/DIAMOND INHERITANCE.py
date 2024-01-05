class Person:

    def __init__(self, name, **kwargs):
        self.name = name

    def display(self):
        print(f'The name of the person is {self.name}')

class Student(Person):

    def __init__(self, name, rollno, **kwargs):
        super().__init__(name, **kwargs)
        self.rollno = rollno

    def display(self):
        super().display()
        print(f'Roll no is {self.rollno}')

class Teacher(Person):

    def __init__(self, name, teacher_id, **kwargs):
        super().__init__(name, **kwargs)
        self.teacher_id = teacher_id

    def display(self):
        super().display()
        print(f'The teacher id is {self.teacher_id}')

class Scholar(Student, Teacher):

    def __init__(self, name, rollno, teacher_id, stipend, **kwargs):
        super().__init__(name=name, rollno=rollno, teacher_id=teacher_id, **kwargs)
        self.stipend = stipend

    def display(self):
        super().display()
        print(f'The annual stipend is {self.stipend}')

s1 = Scholar('Srihari', 134, 206, 100000)
s1.display()
print(Scholar.__mro__)