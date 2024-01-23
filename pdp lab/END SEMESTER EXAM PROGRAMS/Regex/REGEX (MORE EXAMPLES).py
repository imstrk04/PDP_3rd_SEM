import re
'''import re


#question 1 
text1 = 'abc1234#AZ'
pattern1 = re.compile(r'^(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%&*])(?=.*[A-Z])[a-z0-9!@#$%&*A-Z]{9,}$')
if re.search(pattern1, text1):
    print(text1, 'is valid ')
else:
    print(text1, 'is NOT valid ')


#question 2 
text2='123456799'
pattern2=re.compile('^.{10}$')
print(re.search(pattern2,text2))


#question3
text3='srihariforthew@gmail.com'
pattern3=re.compile(r'^[a-zA-Z._]+@{1}[a-zA-Z0-9]+\.{1}[a-zA-Z0-9]{2,3}')
print(re.search(pattern3,text3))



#question 4 (date)
import re

date_string = "2022-01-15"
pattern4 = re.compile(r'^\d{4}-\d{2}-\d{2}$')

if re.search(pattern4, date_string):
    print(date_string, 'is a valid date.')
else:
    print(date_string, 'is NOT a valid date.')

#question 5
text5='Mypa#8r5'
pattern5=re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%&*])[a-zA-Z0-9!@#$%&*]{8,}$')
if re.search(pattern5,text5):
    print('valid')
else:
    print('not valid')'''

#question 6
text6='47890564733789756'
pattern6=re.compile(r'^[456]+[0-9]{1,15}$')
if re.search(pattern6,text6):
    print('valid')
else:
    print('not valid')