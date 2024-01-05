from typing import Iterable, Iterator

# Iterable class
class Iter_cap(Iterable[str]):
    def __init__(self, lst):
        self.lst = lst  # Assign the input list to the instance variable

    def __iter__(self):
        return Spl_iter(self.lst)  # Use the correct class name 'Spl_iter'

# Iterator class
class Spl_iter(Iterator[str]):
    def __init__(self, iter_cap_lst):
        self.iter_lst = [x for x in iter_cap_lst if x.isupper()]
        self.index = 0

    def __next__(self):  # Correct the method name to '__next__'
        if self.index < len(self.iter_lst):
            current = self.iter_lst[self.index]
            self.index += 1
            return current
        else:
            raise StopIteration

# Driver code
x = Iter_cap('SriHari')
for i in x:
    print(i)
