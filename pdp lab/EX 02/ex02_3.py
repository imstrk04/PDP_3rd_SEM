# -*- coding: utf-8 -*-
"""
This module provides code for two classes Regular_Polygon
and Square which is inherited from Regular_Polygon. This is a part
of the exercises given under the course UIT2312 (Programming
and Design Patterns).

In this source code I've executed my own logic and may contain bugs.
The source code has followed good coding practices.

Your comments and suggestions are welcome.

Created on Fri Sept 15 2023

Revised on Wed Sept 21 2023

Original Author: T. Sadakopa Ramakrishnan <sadakopa2210221@ssn.edu.in>
"""


from ex02_1 import Point

class Regular_Polygon(Point):
    def __init__(self):
        super().__init__()
        self.points_array = []
        self.num_sides = 0
    
    def getPolygon(self):
        self.num_sides = int(input("Enter the number of sides: "))
        print("Enter the coordinates of polygon's vertices")
        for i in range(self.num_sides):
            point = Point()
            point.getPoint()
            self.points_array.append(point)
    
    def showPolygonDetails(self):
        print(f"Number of sides: {self.num_sides}")
        print("Coordinates of the polygon's vertices:")
        for i, point in enumerate(self.points_array, start=1):
            print(f"Vertex {i}: ({point.x}, {point.y})")

class Square(Regular_Polygon):
    def __init__(self):
        super().__init__()  # Call the constructor of the base class (Regular_Polygon)
        self.side_length = 0

    def getSquareDetails(self):
        self.getPolygon()  # Reuse the getDetails method from the Regular_Polygon class
        self.side_length = float(input("Enter the side length of the square: "))

    def calcArea(self):
        area = self.side_length ** 2
        return area

    def calcPerimeter(self):
        perimeter = self.side_length * self.num_sides
        return perimeter


if __name__ == "__main__":
    print("Polygon!!!")
    # Create an instance of the Regular_Polygon class
    polygon = Regular_Polygon()

    # Get details of the regular polygon
    polygon.getPolygon()

    # Display the polygon details
    polygon.showPolygonDetails()

    print("_________________________________\n")
    print("SQUARE!!!")
    # Create an instance of the Square class
    square = Square()

    # Get details of the square
    square.getSquareDetails()

    # Display the square details
    square.showPolygonDetails()
    area = square.calcArea()
    perimeter = square.calcPerimeter()
    print(f"Area of the square: {area:.2f}")
    print(f"Perimeter of the square: {perimeter:.2f}")