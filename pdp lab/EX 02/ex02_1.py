# -*- coding: utf-8 -*-
"""
This module provides code for Point class. This is a part
of the exercises given under the course UIT2312 (Programming
and Design Patterns).

In this source code I've executed my own logic and may contain bugs.
The source code has followed good coding practices.

Your comments and suggestions are welcome.

Created on Fri Sept 15 2023

Revised on Wed Sept 21 2023

Original Author: T. Sadakopa Ramakrishnan <sadakopa2210221@ssn.edu.in>
"""


class Point:
    def __init__(self, xcod = 0, ycod = 0):
        self.x = xcod
        self.y = ycod
    
    def getPoint(self):
        self.x = int(input("Enter x coordinate: "))
        self.y = int(input("Enter y coordinate: "))
    
    def showPoint(self):
        result = f"({self.x}, {self.y})"
        return result

if __name__ == "__main__":
    #Creating a Point Object
    P = Point()

    #Getting x and y coordinates
    P.getPoint()

    #Displaying x and y coordinates
    print(P.showPoint())