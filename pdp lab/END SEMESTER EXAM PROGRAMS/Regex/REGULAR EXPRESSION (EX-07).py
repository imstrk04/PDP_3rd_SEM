import re

#check password validity
def check_password(password):
    if len(password<8):
        return 'invalid'
    elif not re.search(r'[a-z]',password):
        return 'invalid'

    elif not re.search(r"[A-Z]", password):
        return "Invalid"
    
    elif not re.search(r"[0-9]", password):
        return "Invalid"
    
    elif not re.search(r"[!@#$%^&*]", password):
        return "Invalid"
    
    elif re.search(r"\s", password):
        return "Invalid"
    
    else:
        return "Valid"

'''#validity of string 
def validity(string):
    pattern=re.compile(r'^[a-zA-Z]+(.)*[a-zA-Z0-9]$')

    if re.search(pattern,string) is not None:
        return 'valid'
    else:
        return 'invalid' '''

#another way
def validity(string):
    pattern = r'^[a-zA-Z]+(.*)[a-zA-Z0-9]$'

    if re.search(r'[!@#$%^&*()]+',string):
        return "Invalid Format! Inclusion of special character."

    #result of findall list is not empty
    if re.findall(r'\s',string)!=[]:
        return 'white psaces occured pass invalid'

    if re.match(pattern,string):
        return 'valid'
    else:
        return 'invalid'
    
print(validity('Partial_sum1'))
print(validity('1partial'))
print(validity('1partial  sum'))

#checking the binary number squence
def check_binary(seq):
    pattern=re.compile(r'^[01]+$')
    if re.search(pattern,seq) is not None:
        return 'valid'
    else:
        return 'invalid'

print(check_binary('010101'))
print(check_binary('1011111'))


#single pattern for password checking
def pwd_single(passwd):
    regex= r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[a-zA-Z\d@$!%*#?&]{6,20}$"
    pat = re.compile(regex)
    mat = re.search(pat, passwd)
    if mat:
        print("Password is valid.")
    else:
        print("Password invalid !!")

print(pwd_single("1!a123A"))





