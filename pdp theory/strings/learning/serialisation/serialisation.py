#practicing serialisation
'''import pickle

class Fruit:

    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
    
    def decribe_fruit(self):
        print(f"{self.name} : {self.calories}")'''

'''fruit = Fruit('banana', 100)
fruit.decribe_fruit()'''

'''with open("data.pickle", 'wb') as file:
    pickle.dumps(fruit, file)

with open("data.pickle", 'rb') as file:
    f = pickle.loads(file)'''

'''f = Fruit('sada', 200)
'f_ser = pickle.dumps(f)
f_load = pickle.loads(f_ser)
print(f_load)''

import pickle

class Hospital:

    def __init__(self, pid, name, age):
        self.pid = pid
        self.name = name
        self.age = age
    
    def decribe_patient(self):
        print(f"PID: {self.pid}\nName: {self.name}\nAge: {self.age}")

p1 = {'pid': 101, 'name': "ABC", 'age' : 22}
p2 = {'pid': 102, 'name': "DEF", 'age' : 11}
p3 = {'pid': 103, 'name': "GHI", 'age' : 40}
p4 = {'pid': 104, 'name': "JKL", 'age' : 35}
p5 = {'pid': 105, 'name': "MNO", 'age' : 60}

data = []
data.append(p1)
data.append(p2)
data.append(p3)
data.append(p4)
data.append(p5)
#print(data)

with open('datas.pickle', 'wb') as file:
    pickle.dump(data, file)

file1 = open("datas.pickle", 'rb')

try:
    while (1):
        p = pickle.load(file1)
        print("Data",p, "\n")
except:
    print("Reached EOF")

print("Reading Completed")
file1.close()
'''

import pickle  
  
class forexample_class:  
    the_number = 25  
    the_string = " hello"  
    the_list = [ 1, 2, 3 ]  
    the_dict = { " first ": " a ", " second ": 2, " third ": [ 1, 2, 3 ] }  
    the_tuple = ( 22, 23 )  
  
user_object = forexample_class()  
  
user_pickled_object = pickle.dumps( user_object )  # here, user is Pickling the object  
print( f" This is user's pickled object: \n { user_pickled_object } \n " )  
  
user_object.the_number = None  
  
user_unpickled_object = pickle.loads( user_pickled_object )  # here, user is Unpickling the object  
print(  
    f" This is the_dict of the unpickled object: \n { user_unpickled_object.the_dict } \n " )  