from transaction import Transaction
from serialisation import save_data,load_data
from regex import check_transaction_id


t1=Transaction(acc_no='1001',balance='900000',transaction_id='456')
t2=Transaction(acc_no='1002',balance='560000',transaction_id='789')

t_list=[t1,t2]

save_data(t_list,'transactions.txt')
loaded=load_data('transactions.txt')

for transac in loaded:
    check_transaction_id(transac.transaction_id)


