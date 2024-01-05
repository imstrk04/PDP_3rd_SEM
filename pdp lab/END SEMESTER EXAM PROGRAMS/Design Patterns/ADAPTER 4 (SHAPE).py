# Target Interface
class shape:
    def __init__(self, dimension):
        self.dimension = dimension

    def compute_area(self):
        pass

# Adaptee
class square:
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

# Adapter class
class shapeadapter(shape):
    def __init__(self, dimension):
        super().__init__(dimension)
        self.square = square(dimension)

    def compute_area(self):
        return self.square.calculate_area()

# Example usage
square_area = square(2)
adapter = shapeadapter(square_area.side)
area = adapter.compute_area()
print(f'The area is {area}')
