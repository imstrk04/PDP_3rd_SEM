import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import json
import re
from typing import Any

class UserManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserManager, cls).__new__(cls)
            cls._instance.users = cls._instance.retrieve_users()
        return cls._instance

    def __init__(self):
        self.conn = sqlite3.connect('user_database.db')
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                            username TEXT PRIMARY KEY,
                            password TEXT
                )    ''')
        self.conn.commit()

    def add_user(self, username, password):
        if username in self.users:
            return False  # User already exists
        self.users[username] = password
        self.store_users()
        return True

    def check_user_exists(self, username):
        return username in self.users

    def store_users(self):
        self.cursor.execute("DELETE FROM users")
        for username, password in self.users.items():
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        self.conn.commit()

    def retrieve_users(self):
        try:
            self.cursor.execute("SELECT username, password FROM users")
            users = {username: password for username, password in self.cursor.fetchall()}
            return users
        except AttributeError:
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
            else:
                self.displayError("Incorrect password")
        else:
            self.displayError("User does not exist")

    def clean_on_exit(self):
        self.user_manager.conn.close()
        self.root.destroy()

def main():
    root = tk.Tk()
    login = LoginPage(root)
    root.protocol("WM_DELETE_WINDOW", login.clean_on_exit)  # Add this line
    root.mainloop()


if __name__ == '__main__':
    main()