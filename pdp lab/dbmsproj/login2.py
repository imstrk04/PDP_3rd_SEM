import sqlite3
from tkinter import *
from tkinter import messagebox
import re
import json
import tkinter as tk

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
                            password TEXT,
                            name TEXT,
                            address TEXT,
                            telephone TEXT
                )    ''')
        self.conn.commit()

    def add_user(self, name, address, telephone, username, password):
        if username in self.users:
            return False  # User already exists
        self.users[username] = {'password': password, 'name': name, 'address': address, 'telephone': telephone}
        self.store_users()
        return True

    def check_user_exists(self, username):
        return username in self.users

    def store_users(self):
        self.cursor.execute("DELETE FROM users")
        for username, user_info in self.users.items():
            self.cursor.execute("INSERT INTO users (username, password, name, address, telephone) VALUES (?, ?, ?, ?, ?)",
                                (username, user_info['password'], user_info['name'], user_info['address'], user_info['telephone']))
        self.conn.commit()

    def retrieve_users(self):
        try:
            self.cursor.execute("SELECT username, password, name, address, telephone FROM users")
            users = {row[0]: {'password': row[1], 'name': row[2], 'address': row[3], 'telephone': row[4]} for row in self.cursor.fetchall()}
            return users
        except AttributeError:
            return {}

class RegisterPage:
    def __init__(self, root):
        self.root = root
        self.user_manager = UserManager()

        self.root.geometry("600x400")
        self.root.title("Registration")

        self.name = StringVar()
        self.address = StringVar()
        self.telephone = StringVar()
        self.username = StringVar()
        self.password = StringVar()

        Label(root, text="Name:").pack()
        Entry(root, textvariable=self.name).pack()

        Label(root, text="Address:").pack()
        Entry(root, textvariable=self.address).pack()

        Label(root, text="Telephone:").pack()
        Entry(root, textvariable=self.telephone).pack()

        Label(root, text="Username:").pack()
        Entry(root, textvariable=self.username).pack()

        Label(root, text="Password:").pack()
        Entry(root, textvariable=self.password, show="*").pack()

        Button(root, text="Register", command=self.register).pack()

    def register(self):
        name = self.name.get()
        address = self.address.get()
        telephone = self.telephone.get()
        username = self.username.get()
        password = self.password.get()

        if (len(password) < 8):
            self.display_error("Please enter a minimum of 8 characters")
        elif not re.search(r"[a-z]", password):
            self.display_error("Please enter a minimum of one lower case alphabets")

        elif not re.search(r"[A-Z]", password):
            self.display_error("Please enter a minimum of one upper case alphabets")

        elif not re.search(r"[0-9]", password):
            self.display_error("Please enter a minimum of one digit ")

        elif not re.search(r"[_!@#$%^&]", password):
            self.display_error("Please enter a minimum of one special character")

        elif re.search(r"\s", password):
            self.display_error("Please don't include spaces")
        else:
            if self.user_manager.add_user(name, address, telephone, username, password):
                messagebox.showinfo("Success", "User successfully registered!")
                self.root.destroy()
            else:
                self.display_error("User Already Exists")

    def display_error(self, message):
        messagebox.showerror("Registration Error", message)

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.user_manager = UserManager()

        self.root.geometry("600x300")
        self.root.title("Login")

        self.username = StringVar()
        self.password = StringVar()

        Label(root, text="Username:").pack()
        Entry(root, textvariable=self.username).pack()

        Label(root, text="Password:").pack()
        Entry(root, textvariable=self.password, show="*").pack()

        Button(root, text="Login", command=self.login).pack()

    def login(self):
        username = self.username.get()
        password = self.password.get()

        if self.user_manager.check_user_exists(username):
            stored_password = self.user_manager.users[username]['password']
            if password == stored_password:
                messagebox.showinfo("Success", "Login successful!")
                self.root.destroy()
            else:
                self.display_error("Incorrect password")
        else:
            self.display_error("User does not exist")

    def display_error(self, message):
        messagebox.showerror("Login Error", message)

def main():
    root = tk.Tk()
    register_page = RegisterPage(Toplevel(root))
    root.withdraw()
    root.protocol("WM_DELETE_WINDOW", root.destroy)

    login_page = LoginPage(Toplevel(root))
    root.mainloop()

if __name__ == '__main__':
    main()
