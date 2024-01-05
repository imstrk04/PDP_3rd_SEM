import re

def check_bin(str):
    pattern = re.compile(r'^[0-1]*$')
    return bool(pattern.search(str))


if __name__ ==  '__main__':
    if check_bin(input('Enter binary number: ')):
        print('Number is binary')
    else:
        print('Number is not binary')