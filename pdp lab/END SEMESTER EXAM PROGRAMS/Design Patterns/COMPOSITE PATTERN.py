import math
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

# Leaf 1 (Concrete class)
class Circle(Shape):

    def set_dimension(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

# Leaf 2 (Concrete class)
class Rectangle(Shape):

    def set_dimension(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

# Composite class (Concrete class)
class Composite(Shape):

    def __init__(self, shapes):
        self.shapes = shapes

    def add_shape(self, shape):
        self.shapes.append(shape)

    def remove_shape(self, shape):
        self.shapes.remove(shape)

    def calculate_area(self):
        total_area = 0
        for shape in self.shapes:
            total_area += shape.calculate_area()
        return total_area

    def display(self):
        print(f'Total Area is: {self.calculate_area()}')


# Client code
circle = Circle()
circle.set_dimension(5)

rec = Rectangle()
rec.set_dimension(4)

composite_shapes = Composite([circle, rec])
composite_shapes.display()
