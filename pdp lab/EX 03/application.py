# -*- coding: utf-8 -*-
"""
This module provides code for Modules and Packages. This is a part
of the exercises given under the course UIT2312 (Programming
and Design Patterns).

In this source code I've executed my own logic and may contain bugs.
The source code has followed good coding practices.

Your comments and suggestions are welcome.

Created on Thur Sept 21 2023

Revised on Wed Sept 26 2023

Original Author: T. Sadakopa Ramakrishnan <sadakopa2210221@ssn.edu.in>
"""


from Date.validity import Valid
from Date.difference import Difference

class StudentCompetition:

    def __init__(self,name,dob,registration_date):
        self.name = name
        self.dob = dob
        self.registration_date = registration_date

    def is_registration_valid(self):
        if not Valid().IsValidDate(self.dob):
            return "Invalid date of birth"
        age_in_years = Difference().difference_with_current(self.dob)
        if age_in_years is None or age_in_years>(17*365):
            return "Invalid age"
        registration_age = Difference().difference_with_current(self.registration_date)
        if registration_age is None or registration_age>(0.5*365):
            return "Registration expired"
        else:
            return "Registration is valid"
    
if __name__ == "__main__":
    student = StudentCompetition(input("Enter student name:"), input("Enter date of birth:"), input("Enter registration date:"))
    print(f"Student Details:\nName: {student.name}\nDate of Birth: {student.dob}\nRegistration Date: {student.registration_date}")
    print("Registration Status:", student.is_registration_valid())
        