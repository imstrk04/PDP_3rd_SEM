a = "this is a sample"
print(a) #this is a sample

b = a.encode('ascii')

print(b) #b'this is a sample'

c = a.encode("UTF-8")
print(c) #b'this is a sample'

#கலாச்சாரம்

d = "க"
e = d.encode('UTF-8')
print(d) #க
print(e) #b'\xe0\xae\x95'

f = "லா"
g = f.encode("UTF-8")
print(g) #b'\xe0\xae\xb2\xe0\xae\xbe'

h = g.decode('utf-8')
print(h) #லா

i = g.decode('ascii', errors='replace') #������
print(i) #UnicodeDecodeError: 'ascii' codec can't decode byte 0xe0 in position 0: ordinal not in range(128)

j = "லா HELLO"
k = j.encode('utf-8')
print(k) #b'\xe0\xae\xb2\xe0\xae\xbe HELLO'

l = k.decode('utf-8')
print(l) #லா HELLO

m = "hello"
n = m.encode('ascii')
print(n) #b'hello'

o = n.decode('utf-8', errors='replace')
print(o) #hello

