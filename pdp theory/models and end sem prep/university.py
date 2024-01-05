import json
import re
from abc import ABC, abstractmethod
from typing import List
import pickle
import threading
 

# Observer Pattern
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

class ThreadedObserver(Observer):
    def __init__(self,name):
        self.name = name

    def update(self, subject):
        print(f"Threaded Observer {self.name}: Received update from {subject.__class__.__name__}")
        # Simulate some time-consuming task
        threading.Thread(target=self.process_update, args=(subject,)).start()

    def process_update(self, subject):
        print(f"Threaded Observer {self.name}: Processing update from {subject.__class__.__name__}")
        # Perform the actual processing here


class Observable(ABC):
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

# Strategy Pattern
class DisplayStrategy(ABC):
    @abstractmethod
    def display_info(self, obj):
        pass

class SimpleDisplay(DisplayStrategy):
    def display_info(self, obj):
        print(f"Name: {obj.name}, Age: {obj.age}")

class DetailedDisplay(DisplayStrategy):
    def display_info(self, obj):
        obj.display_info()

    def update(self,subject):
        print(f"DetailedDisplay: Updated by {subject.__class__.__name__}")
        
# State Pattern
class State(ABC):
    @abstractmethod
    def handle(self, ums):
        pass

class DisplayAllState(State):
    def handle(self, ums):
        ums.display_all()

class SearchState(State):
    def handle(self, ums):
        search_results = ums.search_students("John")
        print("\nSearch Results:")
        for result in search_results:
            result.display_info()

# Singleton Pattern
class Singleton(ABC):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
    
class Person:
    def __init__(self, name, age,**kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id,**kwargs):
        super().__init__(name,age,**kwargs)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")

class Professor(Person):
    def __init__(self, name, age, employee_id,**kwargs):
        super().__init__(name, age,**kwargs)
        self.employee_id = employee_id

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")

class TeachingAssistant(Student, Professor):
    def __init__(self,name,age,employee_id,student_id,**kwargs):
        super().__init__(name=name, age=age,employee_id=employee_id, student_id=student_id,**kwargs)

    def display_info(self):
        super().display_info()
        
class Person:
    def __init__(self, name, age,**kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id,**kwargs):
        super().__init__(name,age,**kwargs)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")

class Professor(Person):
    def __init__(self, name, age, employee_id,**kwargs):
        super().__init__(name, age,**kwargs)
        self.employee_id = employee_id

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")

class TeachingAssistant(Student, Professor):
    def __init__(self,name,age,employee_id,student_id,**kwargs):
        super().__init__(name=name, age=age,employee_id=employee_id, student_id=student_id,**kwargs)

    def display_info(self):
        super().display_info()
        
# Template Pattern
class UniversityManagementSystem(Observable,Singleton):
    def __init__(self):
        super().__init__()
        self.students = []
        self.professors = []
        self.display_strategy = SimpleDisplay()  # Strategy Pattern
        self.state = DisplayAllState()  # State Pattern

    def add_student(self, student):
        self.students.append(student)
        self.notify_observers()
        self.serializeStudents()

    def add_professor(self, professor):
        self.professors.append(professor)
        self.notify_observers()
        self.serializeProfessor()

    def serializeStudents(self):
        serialized_student =[]
        for student in self.students:
            serialized_student.append({
                "name": student.name,
                "age": student.age,
                "student_id": student.student_id
            })

        with open('student.json', 'a') as file:
            json.dump(serialized_student, file)


    def serializeProfessor(self):
        with open('Professor.pkl', 'ab') as file:
            pickle.dump(self.professors,file)


    def display_all(self):
        print("\nStudents:")
        for student in self.students:
            self.display_strategy.display_info(student)
        print("\nProfessors:")
        for professor in self.professors:
            self.display_strategy.display_info(professor)

    def search_students(self, keyword):
        result = []
        for student in self.students:
            if re.search(keyword, student.name, re.IGNORECASE):
                result.append(student)
        return result

    def set_display_strategy(self, display_strategy):
        self.display_strategy = display_strategy

    def set_state(self, state):
        self.state = state

    def perform_action(self):
        self.state.handle(self)

    def load_students_from_json(self, filename='student.json'):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.students = [Student(name=item['name'], age=item['age'], student_id=item['student_id']) for item in data]



# Iterator and Comprehension
def get_students_above_age(students: List[Student], age_threshold: int):
    return [student for student in students if student.age > age_threshold]

# Generator and Coroutine
def generate_student_info():
    while True:
        name = yield
        age = yield
        student_id = yield
        print(f"Received student info: {name}, {age}, {student_id}")

# Async I/O (asyncio)
import asyncio

async def fetch_student_info(name):
    print(f"Fetching info for {name}")
    await asyncio.sleep(1)
    print(f"Info fetched for {name}")

# Unit Testing and Pytest
def test_student_creation():
    student = Student(name="Test Student", age=25, student_id="TS001")
    assert student.name == "Test Student"
    assert student.age == 25
    assert student.student_id == "TS001"

# Example usage
if __name__ == "__main__":
    ums = UniversityManagementSystem()

    # Observer Pattern
    threaded_observer1 = ThreadedObserver("1")
    ums.add_observer(threaded_observer1)
    ums.add_observer(DetailedDisplay())
     # Attach an observer

    student1 = Student(name="John Doe", age=20, student_id="S123")
    professor1 = Professor(name="Dr. Smith", age=40, employee_id="P456")
    ta1 = TeachingAssistant(name="Jane Doe", age=25, student_id="S789", employee_id="P101")

    ums.add_student(student1)
    ums.add_professor(professor1)
    

    # Strategy Pattern
    ums.display_all()

    # State Pattern
    ums.set_state(SearchState())
    ums.perform_action()

    # Template Pattern
    ums.set_display_strategy(DetailedDisplay())
    ums.display_all()

    # Iterator and Comprehension
    students_above_21 = get_students_above_age(ums.students, 21)
    print("\nStudents above 21:")
    for student in students_above_21:
        print(f"Name: {student.name}, Age: {student.age}")

    # Generator and Coroutine
    student_info_generator = generate_student_info()
    next(student_info_generator)  # Start the generator
    student_info_generator.send("Alice")
    student_info_generator.send(22)
    student_info_generator.send("A123")

    # Async I/O (asyncio)
    loop = asyncio.get_event_loop()
    tasks = [fetch_student_info(student.name) for student in ums.students]
    loop.run_until_complete(asyncio.gather(*tasks))



    # Unit Testing and Pytest
    test_student_creation()
    print("Unit test passed.")