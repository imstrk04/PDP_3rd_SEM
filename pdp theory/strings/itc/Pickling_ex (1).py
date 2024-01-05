import pickle

class book:
    def __init__(self,title):
        self.title = title

b = book("python pgm") 
k=book("harry potter")
dump_obj = pickle.dumps(b)
file=open("test.txt",'wb+')

pickle.dump(b,file)

pickle.dump(k,file)
file.close()


file=open("test.txt",'ab+')

pickle.dump(b,file)

pickle.dump(k,file)
file.close()



print(b.title)
print(dump_obj)

c = pickle.loads(dump_obj)
print(c.title)

print("Reading from file")
file2= open("test.txt", 'rb')
try:
    while(1):
        s=pickle.load(file2)
        print(s.title)
except:
    print("thats it")

print("all is well")
file2.close()
