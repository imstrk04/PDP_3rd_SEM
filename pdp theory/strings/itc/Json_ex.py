import json

class book:
    def __init__(self,title):
        self.title = title

b = book("python pgm") 

classITA ={"strength":70, "location":"gf"}



dump_obj = json.dumps(classITA)

print(dump_obj)
print("After dumping: ", type(dump_obj))



