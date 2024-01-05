'''import pickle

class Fruit:

    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
    
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, calories={self.calories})"

fruit = Fruit('banana', 100)

with open("fruit.pickle",'wb') as file:
    pickle.dump(fruit,file)

with open("fruit.pickle", 'rb') as file:
    f = pickle.load(file)
'''
import string
import re
'''delimiters = r'[ \n *]+'
s = "The quick brown\nfox jumps*over the lazy dog."
delimiter_pattern = re.compile(delimiters)
print("delimiter pattern:", delimiter_pattern)
result = delimiter_pattern.split(s)
print(result)
ans = ""
for word in result:
    ans += " " + word
print(ans)'''

'''
def make_bitsseq(s):
    if not s.isascii():
        raise ValueError
    return " ".join(f"{ord(i):08b}" for i in s)

print(make_bitsseq("sada"))'''

'''l = [1,2,3,4]
l_byte = bytearray(l)
print(l_byte)

s = "sada vada"
s_byte = bytearray(s, 'utf-8')
print(s_byte)
'''
'''import json

d = {'name': 'sada', 'age': 19}

with open("learning.json", 'w') as file:
    json.dump(d, file)
'''

'''import re
results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))'''

x = [i for i in range(10) if i % 2 == 0]
print(x)