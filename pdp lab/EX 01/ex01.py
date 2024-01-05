# -*- coding: utf-8 -*-
"""
This module provides code for two classes. This is a part
of the exercises given under the course UIT2312 (Programming
and Design Patterns).

In this source code I've executed my own logic and may contain bugs.
The source code has followed good coding practices.

Your comments and suggestions are welcome.

Created on Fri Sept 15 2023

Revised on Sat Sept 16 2023

Original Author: T. Sadakopa Ramakrishnan <sadakopa2210221@ssn.edu.in>
"""


class Complex:
    '''Complex Number class which has two data members namely re and im
    and two member functions norm() and display()'''

    def __init__(self, re, im):
        '''
        Constructor to initialise data members
        '''
        self.re = re
        self.im = im
    
    def norm(self):
        '''
        Returns the norm value of a complex number
        '''
        return ((self.re * self. re) + (self.im * self.im)) ** 0.5

    def display(self):
        '''
        Displays the complex number along with its norm value
        '''
        string = "|" + str(self.re) + " + " + str(self.im) +"j |= " + str(self.norm())
        return string

class Rectangle:
    def __init__(self, length,breadth):
        """
        Constructor to initialise data members
        """
        self.length = length
        self.breadth = breadth
    
    def area(self):
        """
        Member function to calculate the area of rectangle
        """
        return self.length * self.breadth
    
    def perimeter(self):
        """
        Member function to calculate the perimeter of rectangle
        """
        return 2 * (self.length + self.breadth)

    def display(self):
        """
        Member function to display the rectangle class
        """
        result = f"The sides of rectangle are ({self.length}, {self.breadth}) and Area is {self.area()}. The perimeter of the rectangle is {self.perimeter()}"
        return result
        
#Test cases for the above code

if __name__ == "__main__":
    #This part of the program will not be executed when the file is imported.

    c = Complex(3,4)
    print(c.display())

    R = Rectangle(5,4)
    print(R.display())