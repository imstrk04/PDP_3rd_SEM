class Departments: 

    def __init__(self):
        self.departments = {}

    def add_course(self, dept_name, dept_id):
        self.departments[dept_name] = dept_id