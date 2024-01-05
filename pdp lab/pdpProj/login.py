'''from tkinter import *
import tkinter as tk
from tkinter import messagebox
import json
import re

class UserManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserManager, cls).__new__(cls)
            cls._instance.users = cls._instance.retrieve_users()
        return cls._instance

    def add_user(self, username, password):
        if username in self.users:
            return False  # User already exists
        self.users[username] = password
        self.store_users()
        return True

    def check_user_exists(self, username):
        return username in self.users

    def store_users(self):
        with open("login_details.json", "w") as file:
            json.dump(self.users, file)

    def retrieve_users(self):
        try:
            with open("login_details.json", "r") as file:
                users = json.load(file)
            return users
        except FileNotFoundError:
            return {}

class LoginPage:

    def __init__(self, root):
        self.root = root
        self.user_manager = UserManager()

        # Design
        self.root.geometry("1280x720+150+80")
        self.root.configure(bg="#d7dae2")
        self.root.title("LOGIN PAGE")

        # Label
        lb1Title = Label(text="Login System", font=('Arial', 50, 'bold'), fg="Black", bg="#d7dae2").pack(pady=50)

        # Frame
        bordercolor = Frame(root, bg="black", width=800, height=400)
        bordercolor.pack()

        mainframe = Frame(bordercolor, bg="#d7dae2", width=800, height=400)
        mainframe.pack(padx=20, pady=20)

        Label(mainframe, text="Username", font=("arial", 30, "bold"), bg="#d7dae2").place(x=100, y=50)
        Label(mainframe, text="Password", font=("arial", 30, "bold"), bg="#d7dae2").place(x=100, y=150)

        self.username = StringVar()
        self.password = StringVar()

        self.entry_username = Entry(mainframe, textvariable=self.username, width=12, bd=2, font=('arial', 30))
        self.entry_username.place(x=400, y=50)

        self.entry_password = Entry(mainframe, textvariable=self.password, width=12, bd=2, font=('arial', 30), show="*")
        self.entry_password.place(x=400, y=150)

        button_width = 15
        button_height = 2

        Button(mainframe, text="Register", height=button_height, width=button_width, bg="#FFA500", fg="white", bd=0,
               command=self.register).place(x=50, y=250)
        Button(mainframe, text="Login", height=button_height, width=button_width, bg="#ed3833", fg="white", bd=0,
               command=self.login).place(x=200, y=250)
        Button(mainframe, text="Reset", height=button_height, width=button_width, bg="#1089ff", fg="white", bd=0,
               command=self.reset).place(x=350, y=250)
        Button(mainframe, text="Exit", height=button_height, width=button_width, bg="#00bd56", fg="white", bd=0,
               command=self.root.destroy).place(x=500, y=250)

    def reset(self):
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def displayError(self, message):
        messagebox.showerror("Login Error", message)

    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if (len(password) < 8):
            self.displayError("Please enter a minimum of 8 characters")

        elif not re.search(r"[a-z]", password):
            self.displayError("Please enter a minimum of one lower case alphabets")

        elif not re.search(r"[A-Z]", password):
            self.displayError("Please enter a minimum of one upper case alphabets")

        elif not re.search(r"[0-9]", password):
            self.displayError("Please enter a minimum of one digit ")

        elif not re.search(r"[_!@#$%^&]", password):
            self.displayError("Please enter a minimum of one special character")

        elif re.search(r"\s", password):
            self.displayError("Please don't include spaces")

        else:
            if self.user_manager.add_user(username, password):
                messagebox.showinfo("Success", "User successfully registered!")
                self.entry_username.delete(0, tk.END)
                self.entry_password.delete(0, tk.END)
            else:
                self.displayError("User Already Exists")

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if self.user_manager.check_user_exists(username):
            stored_password = self.user_manager.users[username]
            if password == stored_password:
                messagebox.showinfo("Success", "Login successful!")
                self.entry_username.delete(0, tk.END)
                self.entry_password.delete(0, tk.END)
                self.on_login_callback(username)
            else:
                self.displayError("Incorrect password")
        else:
            self.displayError("User does not exist")
    

def main():
    root = tk.Tk()
    login = LoginPage(root)
    root.mainloop()

if __name__ == '__main__':
    main()'''


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import json
import re
from datetime import datetime
from abc import ABC
from util import Observable
from netbanking_app import NetBankingApp

class BankTransactionCommand:
    def execute(self, amount, transaction_type):
        account = BankAccount()._instance
        if transaction_type == "Deposit":
            account.deposit(amount)
        elif transaction_type == "Withdraw":
            account.withdraw(amount)


class Observable(ABC):
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()

class UserAccount(Observable):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.balance = 0
        self.transactions = []

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +{amount} ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")
        self.notify_observers()

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -{amount} ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")
            self.notify_observers()
        else:
            messagebox.showwarning("Insufficient Balance", "You do not have sufficient balance.")

    def get_transactions(self):
        return self.transactions

class UserManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserManager, cls).__new__(cls)
            cls._instance.users = cls._instance.retrieve_users()
            cls._instance.user_accounts = {}
        return cls._instance

    def add_user(self, username, password):
        if username in self.users:
            return False  # User already exists
        self.users[username] = password
        self.user_accounts[username] = UserAccount(username)
        self.store_users()
        return True

    def get_user_account(self, username):
        return self.user_accounts.get(username)

    def check_user_exists(self, username):
        return username in self.users

    def store_users(self):
        with open("login_details.json", "w") as file:
            json.dump(self.users, file)

    def retrieve_users(self):
        try:
            with open("login_details.json", "r") as file:
                users = json.load(file)
            return users
        except FileNotFoundError:
            return {}

class LoginPage:

    def __init__(self, root):
        self.root = root
        self.user_manager = UserManager()

        # Design
        self.root.geometry("1280x720+150+80")
        self.root.configure(bg="#d7dae2")
        self.root.title("LOGIN PAGE")

        # Label
        lb1Title = Label(text="Login System", font=('Arial', 50, 'bold'), fg="Black", bg="#d7dae2").pack(pady=50)

        # Frame
        bordercolor = Frame(root, bg="black", width=800, height=400)
        bordercolor.pack()

        mainframe = Frame(bordercolor, bg="#d7dae2", width=800, height=400)
        mainframe.pack(padx=20, pady=20)

        Label(mainframe, text="Username", font=("arial", 30, "bold"), bg="#d7dae2").place(x=100, y=50)
        Label(mainframe, text="Password", font=("arial", 30, "bold"), bg="#d7dae2").place(x=100, y=150)

        self.username = StringVar()
        self.password = StringVar()

        self.entry_username = Entry(mainframe, textvariable=self.username, width=12, bd=2, font=('arial', 30))
        self.entry_username.place(x=400, y=50)

        self.entry_password = Entry(mainframe, textvariable=self.password, width=12, bd=2, font=('arial', 30), show="*")
        self.entry_password.place(x=400, y=150)

        button_width = 15
        button_height = 2

        Button(mainframe, text="Register", height=button_height, width=button_width, bg="#FFA500", fg="white", bd=0,
               command=self.register).place(x=50, y=250)
        Button(mainframe, text="Login", height=button_height, width=button_width, bg="#ed3833", fg="white", bd=0,
               command=self.login).place(x=200, y=250)
        Button(mainframe, text="Reset", height=button_height, width=button_width, bg="#1089ff", fg="white", bd=0,
               command=self.reset).place(x=350, y=250)
        Button(mainframe, text="Exit", height=button_height, width=button_width, bg="#00bd56", fg="white", bd=0,
               command=self.root.destroy).place(x=500, y=250)

    def reset(self):
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def displayError(self, message):
        messagebox.showerror("Login Error", message)

    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if len(password) < 8:
            self.displayError("Please enter a minimum of 8 characters")
        elif not re.search(r"[a-z]", password):
            self.displayError("Please enter a minimum of one lowercase alphabet")
        elif not re.search(r"[A-Z]", password):
            self.displayError("Please enter a minimum of one uppercase alphabet")
        elif not re.search(r"[0-9]", password):
            self.displayError("Please enter a minimum of one digit ")
        elif not re.search(r"[_!@#$%^&]", password):
            self.displayError("Please enter a minimum of one special character")
        elif re.search(r"\s", password):
            self.displayError("Please don't include spaces")
        else:
            if self.user_manager.add_user(username, password):
                messagebox.showinfo("Success", "User successfully registered!")
                self.entry_username.delete(0, tk.END)
                self.entry_password.delete(0, tk.END)
            else:
                self.displayError("User Already Exists")

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if self.user_manager.check_user_exists(username):
            stored_password = self.user_manager.users[username]
            if password == stored_password:
                messagebox.showinfo("Success", "Login successful!")
                self.entry_username.delete(0, tk.END)
                self.entry_password.delete(0, tk.END)
                user_account = self.user_manager.get_user_account(username)
                self.on_login_callback(username, user_account)
            else:
                self.displayError("Incorrect password")
        else:
            self.displayError("User does not exist")

def main():
    root = tk.Tk()
    login_page = LoginPage(root)
    login_page.on_login_callback = lambda username, user_account: open_net_banking_app(root, username, user_account)
    root.mainloop()

def open_net_banking_app(root, username, user_account):
    root.destroy()
    net_banking_app = NetBankingApp(username, user_account)
    net_banking_app.mainloop()

if __name__ == '__main__':
    main()
