import re

def check_pass(str):
    pattern = re.compile(r'^[A-Za-z\d_@$!%*?&#]{8,}$')
    return bool(pattern.search(str))


if __name__ ==  '__main__':
    if check_pass(input('Enter password: ')):
        print('Password is valid')
    else:
        print('Password is invalid')