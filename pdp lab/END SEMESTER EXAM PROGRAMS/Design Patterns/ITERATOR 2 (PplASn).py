from typing import Iterable, Iterator

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class student(person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

class faculty(person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

class staff(person):
    def __init__(self, name, age, sal):
        super().__init__(name, age)
        self.sal = sal

class PplAsn_iterable(Iterable[str]):

    def __init__(self, *args):
        self.people_list = [*args]

    def add_people(self, person):
        self.people_list.append(person)

    def add_new_year_bonus(self,category):
        for i in self.people_list:
            if isinstance(i,category):
                i.sal+=2000
                print(f'new year bonus added to {i.name}')
                
    def get_faculty_set(self):
        # Using set comprehension to create a unique set of faculty (desired list by user)
        faculty_set = {person for person in self.people_list if isinstance(person, faculty)}
        return faculty_set

    def get_faculty_by_department(self, department):
        # Using list comprehension to create a list of faculty in different departments
        faculty_list = [person for person in self.people_list if isinstance(person, faculty) and person.department != department]
        return faculty_list
                
    def __iter__(self, class_category, department):
        return PplAsn_iterator(self.people_list, class_category, department)

class PplAsn_iterator(Iterator[str]):
    def __init__(self, lst, category, dept):
        self.peoplelist = [x for x in lst if isinstance(x, category) and x.department==dept]
        self.index = 0

    def __next__(self):
        if self.index < len(self.peoplelist):
            current = self.peoplelist[self.index]
            self.index += 1
            return current
        else:
            raise StopIteration

# Driver Code
a = student("John", 19, "IT")
b = faculty("Dr. Smith", 18, "CSE")
c = staff("Security1", 25, 30000)
d = staff("Security2", 32, 30000)

people_list = PplAsn_iterable(a, b, c, d)

# Iterate over students in IT department
print("Students in IT department:")
for person_obj in people_list.__iter__(student,'IT'):
    print(person_obj.name)

#adding new year bonus
people_list.add_new_year_bonus(staff)
