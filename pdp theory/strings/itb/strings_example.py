'''
var1="Zoé"
print(var1.encode('ascii',errors='replace'))
print(var1.encode('ascii',errors='xmlcharrefreplace'))
print(var1.encode('ascii',errors='ignore'))
#print(var1.encode('ascii',errors='strict'))
print(var1.encode('ascii'))
'''
'''
var1="Zoé"
print(var1.encode('UTF-8',errors='replace'))
print(var1.encode('UTF-8',errors='xmlcharrefreplace'))
print(var1.encode('UTF-8',errors='ignore'))
print(var1.encode('UTF-8',errors='strict'))
'''


#use index and slice, replace notation on a bytes object 

str1 = bytearray(b"abcdefgh")
print(type(str1))
print(type(str1[1]))
print(str1[1])
print(str1[4])#prints the ascii value of the char in the index 

print(str1[4:6])#slicing
str1[4:6]=b"qw" #replacing 
print(str1)


str1[4]=ord('e')
#As the byte character is already int type only the replacement of 'e' in the position of 'q' happens
print(str1)

str1[5]=102
print(str1)



#Normal string and ordinal()

str2=['a','b','c']
print(type(str2))
print(type(str2[1]))
str2[0]=ord('b')#Ordinal function replaces 'a' with the ascii value of 'b' 
print(str2)









