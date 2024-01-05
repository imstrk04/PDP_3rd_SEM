from savingsaccount import savings_account
from checkingaccount import checking_account

class total_account(savings_account,checking_account):

    def __init__(self,acc_no,balance,acc_holder,gst_registered,transferdate,**kwargs):
        super().__init__(acc_no=acc_no,balance=balance,acc_holder=acc_holder,gst_regustered=gst_registered)
        self.transferdate=transferdate

    def display(self):
        print(f'{self.account_number},{self.balance},{self.account_holder},{self.gst_registered},{self.transfer_date}')


    
