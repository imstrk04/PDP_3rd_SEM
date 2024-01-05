class Shape:
    def calculate_area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius
rectangle = Rectangle(5, 8)
circle = Circle(4)

rectangle_area = rectangle.calculate_area()
circle_area = circle.calculate_area()

print("Area of the rectangle:", rectangle_area)
print("Area of the circle:", circle_area)
