from datetime import datetime

class Current:

    def curr_time(self):
        return datetime.now().strftime("%H:%M:%S")

    def def_date(self):
        return datetime.today().strftime("%d.%m.%y")

    def dif_date(self):
        return datetime.today().strftime("%m.%d.%y")
    
    def str_time(self):
        return datetime.today().strftime("%m/%d/%Y, %H:%M:%S")