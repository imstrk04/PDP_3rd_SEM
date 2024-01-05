'''
Sadakopa Ramakrishnan T
ex 5 pdp lab qn 1
Define a vector inheriting from standard list. Let the vector is restricted to having only integer 
number in the list. Overload appropriate function and operator so that when any other type of element 
is inserted the program raises an error.
'''


class Vector(list):
    def __init__(self, sequence=None):
        super().__init__()
        if sequence is not None:
            try:
                for item in sequence:
                    self.append(item)
            except TypeError:
                self.append(sequence)

    def append(self, item):
        if isinstance(item, int):
            super().append(item)
        else:
            raise TypeError('Only integers can be appended')

    def __add__(self, other):
        return sorted(Vector(set(self) | set(other)))

    def __sub__(self, other):
        union = set(self) | set(other)
        intersection = set(self) & set(other)
        return sorted(Vector(union - intersection))

    def get_ratios(self, other):
        if isinstance(other, Vector):
            if len(self) == len(other):
                result = Vector()
                for i in range(len(self)):
                    try:
                        result.append(self[i] // other[i])
                    except ZeroDivisionError:
                        result.append(0)
                return result
            else:
                raise IndexError("Vectors have different dimensions")
        else:
            raise TypeError(f"{other} is not a Vector object")


if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    v2 = Vector([3, 4, 5, 7])
    identity = Vector([1] * 4)

    v1.append(4)
    print("v1:", v1)
    print("v2:", v2)
    print("v1 + v2:", v1 + v2)
    print("v1 - v2:", v1 - v2)
    print("v1 / identity ratios:", v1.get_ratios(identity))

    try:
        v1.get_ratios(Vector([1, 0, 3, 2]))
    except ZeroDivisionError:
        print("Division by zero!")

    try:
        v1.get_ratios(Vector([1, 0, 3]))
    except IndexError as e:
        print(e)
