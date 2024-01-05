import re

def check_transaction_id(transac_id):
    pattern=re.compile(r'^[0-9]+$')
    if re.search(pattern,transac_id):
        print('id is valid')
    else:
        print ('id is invalid')
