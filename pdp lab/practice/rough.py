'''#practicing serialisation
import pickle
import json

class Fruit:

    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
    
    def decribe_fruit(self):
        print(f"{self.name} : {self.calories}")


with open('data.pickle', 'rb') as file:
    fruit: Fruit = pickle.load(file)

fruit.decribe_fruit()

fruit.calories += 200
fruit.decribe_fruit()'''


'''import pickle

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