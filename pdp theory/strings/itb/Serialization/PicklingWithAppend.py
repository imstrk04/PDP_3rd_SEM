import pickle

class book:
    def __init__(self,title):
        self.title = title

a=book("Python3 Program") 
b=book("Design Patterns")
c=book("Gang of four") 
d=book("Non-software examples of DP")

'''file=open("test.txt",'wb')
pickle.dump(a,file)
pickle.dump(b,file)
file.close()'''

print()
print("reading a and b: ")

with open("test.txt",'wb') as file:
    pickle.dump(a,file)
    pickle.dump(b,file)

# file=open("test.txt",'ab')
# pickle.dump(c,file)
# pickle.dump(d,file)
# #file.close()

print()

with open("test.txt",'ab') as file:
    pickle.dump(c,file)
    pickle.dump(d,file)

print("Reading from file")

file2= open("test.txt", 'rb')
try:
    while(1):
        s=pickle.load(file2)
        print(s.title)
except:
    print()
    print("Reached EoF")
    print()

print("Reading completed")
file2.close()
