template = "hi{},where is your{},is{} fine?"
print(template.format("vasu"," kannamma"," it"))
v  = [{" pv "} ,{"cute"}]
print(v[1])
print(f"yas {v[0]} is {v[1]}" )

name_mail =["pv", "v@ssn" ]
template = """
name: <{name}> mail: <{mail}>"""
print(name_mail[0])
print(template.format(name='pv',mail='pv@123'))

template = ''' vasuki
VasukiP@ssn.edu.in'''
if(template.find('i')!=True):
    print(template)
s =template.split()

class student:
    def __init__(self, name,reg,mail="xyz@gmail.com"):
        self.name = name
        self.reg = reg
        self.mail = mail


    def dis(self):
        template = """
        name   : {0.name}
        reg No.: {0.reg}
        email   :{0.mail}
        """
        print(template.format(self))

s = student("vas",123)
s.dis();
p =student("jothy", 234,'jothy@123.com')
template = """
        name   : {0.name}      reg No.: {0.reg}       email  : {0.mail}
        """

print(template.format(p))
print(f"{{ }}  used for single brace")
template ="{0}{1:^25}{2:<8}{3:>5}"
print(template.format("Name","Age","Exp","CTC"))
template ="{0}{1:^25}{2:<8}${3:>5.2f}"
print(template.format("kanna","52","23",30.555))


#******

chare = b'\x63\x6C'
print(chare)
print(chare.decode("latin-1"))
print(chare.decode("UTF-8"))
print(chare.decode("ascii"))




        
    

