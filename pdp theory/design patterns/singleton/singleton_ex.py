class s_class:
    s_instance = None
    def __new__(cls,*args,**kwargs):
        print("I am Called from new")        
        if not cls.s_instance:
            cls.s_instance = super().__new__(cls,*args,**kwargs)
        return cls.s_instance
    def __init__(self):
        print("I am new init") 


x = s_class()
y = s_class()
print("hi")
print(x)
print(y)
