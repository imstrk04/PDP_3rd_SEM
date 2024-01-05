class observer:
    def update(self):
        pass

class observable:
    def add(self):
        pass

    def remove(self):
        pass

    def notify(self):
        pass


class Assignmentqueue:

    def __init__(self):
        self.assignments=[]
        self.observer=[]

    def add_observer(self,observer):
        if observer not in self.observer:
            self.observer.append(observer)

    def remove_observer(self,index):
        del self.observer[index]

    def notify_observer(self,message):
        for observer in self.observer:
            observer.update(message)

    def add_assignment(self, assignment_number, deadline):
        self.assignments.append({"assignment_number": assignment_number, "deadline": deadline})
        self.notify_observer(f"New Assignment: {assignment_number}")

    def submit_assignment(self, register_number, assignment_number, submission_date):
        for assignment in self.assignments:
            if assignment["assignment_number"] == assignment_number and submission_date <= assignment["deadline"]:
                self.notify_observer(f"Submission: {register_number} submitted Assignment {assignment_number} before the deadline")
                return True
        return False

class Student(observer):
    def __init__(self, register_number):
        self.register_number = register_number

    def update(self, message):
        print(f"Student {self.register_number} received a notification: {message}")

class Teacher(observer):
    def __init__(self):
        self.submissions = {}

    def update(self, message):
        print(f"Teacher received a notification: {message}")

#driver code

s1=Student('101')
s2=Student('102')

queue=Assignmentqueue()
queue.add_observer(s1)
queue.add_observer(s2)
teacher = Teacher()

queue.add_observer(teacher)

queue.add_assignment(1, "2023-01-15")
queue.add_assignment(2, "2023-01-20")
queue.submit_assignment("S001", 1, "2023-01-14")  # Submitted before the deadline
queue.submit_assignment("S002", 1, "2023-01-16")  # Submitted after the deadline
queue.submit_assignment("S001", 2, "2023-01-18")  # Submitted before the deadline
queue.submit_assignment("S002", 2, "2023-01-19")  # Submitted before the deadline

