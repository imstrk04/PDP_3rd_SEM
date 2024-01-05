class A():
    def __init__(self, a='a', *args, **kwargs):
        #self.a = a 
        super().__init__(*args, **kwargs)

class B():
    def __init__(self, b='b', *args, **kwargs):
        self.b = b
        super().__init__(*args, **kwargs)

class C(A,B):
    def __init__(self, c='c', *args, **kwargs):
        self.c = c
        super().__init__(*args, **kwargs)

c_obj = C()
print(vars(c_obj))
d_obj=C(a='A',b='B',c='C')
print(vars(d_obj))

