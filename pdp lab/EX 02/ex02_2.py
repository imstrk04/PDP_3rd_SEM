# -*- coding: utf-8 -*-
"""
This module provides code for two classes Circle and Cone 
which is inherited from Circle. This is a part
of the exercises given under the course UIT2312 (Programming
and Design Patterns).

In this source code I've executed my own logic and may contain bugs.
The source code has followed good coding practices.

Your comments and suggestions are welcome.

Created on Fri Sept 15 2023

Revised on Wed Sept 21 2023

Original Author: T. Sadakopa Ramakrishnan <sadakopa2210221@ssn.edu.in>
"""


class Circle:
    def __init__(self):
        self.radius = 0.0

    def getCircle(self):
        print("Enter the coordinates of Centre")
        x1 = int(input("Enter x coordinate of center: "))
        y1 = int(input("Enter y coordinate of center: "))

        print("Enter the coordinates of any point on circumference")
        x2 = int(input("Enter x coordinate of point: "))
        y2 = int(input("Enter y coordinate of point: "))

        self.calcRad(x1,y1,x2,y2)
        self.calcArea()
    
    def calcRad(self, x1, y1, x2, y2):
        self.radius = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
    
    def calcArea(self):
        area = 3.14 * (self.radius ** 2)
        print(f"The radius of the circle is {self.radius}")
        print(f"Area of circle is {area}")

class Cone(Circle):
    def __init__(self):
        super().__init__()
        self.apex = None

    def getCone(self):
        self.getCircle()
        print("Enter the coordinates of apex")
        x = int(input("Enter the x coordinates of apex: "))
        y = int(input("Enter the y coordinate of apex: "))
        self.apex = (x, y)
    
    def calcVolume(self):
        height = ((self.radius ** 2) + (self.apex[1]**2)) ** 0.5
        volume = (1/3) * 3.14 * (self.radius**2) * (height)
        print(f"Apex Coordinates: {self.apex}")
        print(f"Height of the cone: {height}")
        print(f"Volume of the cone: {volume}")


if __name__ == "__main__":
    print("CIRCLE!!!")
    #Creating a circle object
    circle = Circle()

    #Printing details
    circle.getCircle() 

    print("_________________________________")
    print("CONE!!!")
    #Creating a Cone object
    cone = Cone()
    
    #Printing details
    cone.getCone()
    cone.calcVolume()
