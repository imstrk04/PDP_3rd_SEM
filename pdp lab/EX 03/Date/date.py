class Date:
    
    __slots__ = ["year", "month", "date"]

    def __init__(self, y=0, m=0, d=0):
        self.year = y
        self.month = m
        self.date = d

    def set_date(self, y, m, d):
        if len(y)==4 and y.isdigit():
            self.year = int(y)
        else:
            raise ValueError("Year must have 4 numbers")
        if len(m)==2 and m.isdigit():
            self.month = int(m)
        else:
            raise ValueError("Month must have 2 numbers")
        if len(d)==2 and d.isdigit():
            self.date = int(d)
        else:
            raise ValueError("Date must have 2 numbers")

    def show_date(self):
        print(f"{self.date}/{self.month}/{self.year}")