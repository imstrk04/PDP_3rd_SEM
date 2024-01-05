'''Raising an exception'''
class EvenOnly(list):
    def append(self, value):
        if not isinstance(value, int):
            raise TypeError("Only integers can be added")
        if value % 2 != 0:
            raise ValueError("Only even numbers can be added")
        super().append(value)
e=EvenOnly()
#e.append(10)
#print(e)
#e.append(13)
#e.append('a')
print(e)

