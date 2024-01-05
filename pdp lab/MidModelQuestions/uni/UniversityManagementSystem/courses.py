class Courses: 

    def __init__(self):
        self.courses = {}

    def add_course(self, course_name, course_id):
        self.courses[course_name] = course_id
