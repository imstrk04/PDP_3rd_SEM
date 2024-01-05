# Define an iterable interface
class Iterable:
    def create_iterator(self):
        pass

# Define an iterator interface
class Iterator:
    def has_next(self):
        pass

    def next(self):
        pass

# Concrete implementation of an iterable
class ConcreteIterable(Iterable):
    def __init__(self):
        self._data = [1, 2, 3, 4, 5]

    def create_iterator(self):
        return ConcreteIterator(self)

# Concrete implementation of an iterator
class ConcreteIterator(Iterator):
    def __init__(self, iterable):
        self._iterable = iterable
        self._index = 0

    def has_next(self):
        return self._index < len(self._iterable._data)

    def next(self):
        if self.has_next():
            value = self._iterable._data[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration("No more elements")

# Client code
iterable = ConcreteIterable()
iterator = iterable.create_iterator()

while iterator.has_next():
    value = iterator.next()
    print(value)
