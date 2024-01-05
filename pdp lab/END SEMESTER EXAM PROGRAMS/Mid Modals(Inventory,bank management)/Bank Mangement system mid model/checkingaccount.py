from accountmodule import account 

class checking_account(account):

    def __init__(self,account_number,balance,gst_registered,**kwargs):
        super().__init__(account_number,balance,**kwargs)
        self.gst_registered=gst_registered

    def display(self):
        return f'{self.account_number},{self.balance},{self.gst_registered}'
