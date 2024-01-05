#decorator pattern is used to add a behaviour to an object

def good_morning(func):
    def wrapper(name):
        print ('good morning ')
        func(name)
        print('welcome to the program')

    return wrapper

def good_night(func):
    def wrapper(name):
        print ('good night ')
        func(name)
        

    return wrapper


#give the decorators you want before the program so that they get called 
@good_morning
@good_night
def name(name):
    print('my name is',name)

name('srihari')
