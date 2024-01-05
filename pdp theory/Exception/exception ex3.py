'''Handling an exception'''
class EvenOnly(list):
    def append(self, value):
        try:
            if isinstance(value,int):
                pass
        except:
            print("type error occured")
        try:
            if value % 2 == 0:
                super().append(value)
        except:
            print("Value error occured")
        

e=EvenOnly()
e.append(10)
print(e)
print()
e.append(13)
print(e)
print(())
e.append('a')
print(type('a'))
print(e)
