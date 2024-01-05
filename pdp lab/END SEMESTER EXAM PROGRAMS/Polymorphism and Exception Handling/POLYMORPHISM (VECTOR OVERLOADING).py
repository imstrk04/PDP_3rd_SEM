class Vector(list):

    def __init__(self, *args):
        super().__init__(args)

    def append(self, value):
        if not isinstance(value, int):
            raise ValueError('Enter integer values only')
        super().append(value)

    def extend(self, iterable):
        if not all(isinstance(x, int) for x in iterable):
            raise ValueError('Enter integer values only')
        super().extend(iterable)

    def insert(self, index, value):
        if not isinstance(value, int):
            raise ValueError('Enter integer values only')
        super().insert(index, value)

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('Vectors must be of equal length for addition')
        return [a + b for a, b in zip(self, other)]

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Vectors must be of equal length for subtraction')
        return [a - b for a, b in zip(self, other)]

    def merge(self, other):
        return sorted(set(self + other))

    def difference(self, other):
        return [x for x in self if x not in other]

# Example usage:
v1 = Vector(2, 3, 4)
v2 = Vector(1, 2,5)

try:
    result_merge = v1.__add__(v2)
    result_diff = v1.__sub__(v2)

    print("Merged Vector (V1 + V2):", result_merge)
    print("Difference Vector (V1 - V2):", result_diff)
except ValueError as e:
    print(f"Error: {e}")
