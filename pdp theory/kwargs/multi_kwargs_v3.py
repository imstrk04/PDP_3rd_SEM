#super() for multiple inheritance with multiple arguments and polymorphism

class A():
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.var1=50  #given a default value to check whether it can be changed permanently
        self.x=30
    def fun(self):
        print("I'm function 1")

class B(A):
    def __init__(self,var2,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.var2=var2
    def fun(self):
        super().fun()
        print("I'm function 2")

class C(A):
    def __init__(self,var3,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.var3=var3
        self.var1=40  # changed var1 to 40

    def fun(self):
        super().fun()
        print("I'm function 3")
        


class D(B,C):
    def __init__(self,var4,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.var4=var4
        
    def fun(self):
        super().fun()
        print("I'm function 4")
        

d=D(10,20,30)
print(D.__mro__)
print(vars(d))
print(d.var1,d.var2,d.var3,d.var4,d.x)
d.fun()

a=A() #created an other object for A class and printed the value of var1
print("var1 for object named as d",d.var1)
print("var1 for other object ",a.var1)



'''summary : an instance variable of inherited class (parent class) can be changed with in an object and
can't be changed permenantly but with in that object of the class it can be changed anytime and
follows last recently updated value  once an anthor object is created  for same parent class
it will regain its default value'''
                 
