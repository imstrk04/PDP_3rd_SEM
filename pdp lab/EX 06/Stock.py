import pickle

class Stock:
    def __init__(self, company, rate, date, time):
        self.company = company
        self.rate = rate
        self.date = date
        self.time = time

    def display(self):
        print(f"{self.company:10} {self.rate:5} {self.date:10} {self.time:8}")

with open("Stock.txt", 'wb') as f:
    stock_list = [
        Stock("Apple", 100.0, "2023-11-01", "09:00 AM"),
        Stock("Samsung", 75.5, "2023-11-01", "09:15 AM")
    ]
    pickle.dump(stock_list, f)

with open("Stock.txt", 'rb') as f:
    stock_list = pickle.load(f)

print(f"{'Company':10} {'Rate':5} {'Date':10} {'Time':8}")
print('-'*40)
for stock in stock_list:
    stock.display()