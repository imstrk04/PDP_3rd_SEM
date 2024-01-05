import re

def check_var_name(str):
    pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    return bool(pattern.search(str))


if __name__ ==  '__main__':
    if check_var_name(input('Enter variable name: ')):
        print('Variable name is valid')
    else:
        print('Variable name is invalid')