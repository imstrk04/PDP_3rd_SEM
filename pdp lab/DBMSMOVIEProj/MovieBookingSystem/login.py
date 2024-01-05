import sqlite3
from tkinter import *
from tkinter import messagebox
import re
import tkinter as tk
from MovieBookingSystem import home


class UserManager:
  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(UserManager, cls).__new__(cls)
      cls._instance.users = cls._instance.retrieve_users()
    return cls._instance

  def __init__(self):
    self.conn = sqlite3.connect(r'MovieBookingSystem/data.db')
    self.cursor = self.conn.cursor()
    self.create_table()
    self.users = self.retrieve_users()

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
    self.users[username] = {
        'password': password,
        'name': name,
        'address': address,
        'telephone': telephone
    }
    self.store_users()
    return True

  def check_user_exists(self, username):
    return username in self.users

  def store_users(self):
    self.cursor.execute("DELETE FROM users")
    for username, user_info in self.users.items():
      self.cursor.execute(
          "INSERT INTO users (username, password, name, address, telephone) VALUES (?, ?, ?, ?, ?)",
          (username, user_info['password'], user_info['name'],
           user_info['address'], user_info['telephone']))
    self.conn.commit()

  def retrieve_users(self):
    try:
      self.cursor.execute(
          "SELECT username, password, name, address, telephone FROM users")
      users = {
          row[0]: {
              'password': row[1],
              'name': row[2],
              'address': row[3],
              'telephone': row[4]
          }
          for row in self.cursor.fetchall()
      }
      return users
    except AttributeError:
      return {}


class WelcomePage:

  def __init__(self, root):
    self.root = root
    self.root.geometry("1280x720")
    self.root.configure(bg="#d7dae2")
    self.root.title("MOVIE BOOKING SYSTEM")
    Label(root,
          text="WELCOME TO μTICKETS",
          font=('Arial', 50, 'bold'),
          fg="#1089ff",
          bg="#d7dae2").pack(pady=50)
    Button(root,
           text="Register",
           command=self.open_register_page,
           height=3,
           width=15).pack(pady=100)
    Button(root,
           text="Login",
           command=self.open_login_page,
           height=3,
           width=15).pack(pady=20)

  def open_register_page(self):
    register_page = RegisterPage(Toplevel(self.root))

  def open_login_page(self):
    login_page = LoginPage(Toplevel(self.root))


class RegisterPage:

  def __init__(self, root):
    self.root = root
    self.root.configure(bg="#d7dae2")
    self.user_manager = UserManager()

    self.root.geometry("1280x720")
    self.root.title("Registration")

    Label(root,
          text="REGISTRATION PAGE",
          font=('Arial', 50, 'bold'),
          fg="#ed3833",
          bg="#d7dae2").pack(pady=20)

    self.name = StringVar()
    self.address = StringVar()
    self.telephone = StringVar()
    self.username = StringVar()
    self.password = StringVar()

    Label(root, text="Name:", font=("Arial", 20)).pack()
    Entry(root, textvariable=self.name, font=("Arial", 20)).pack()

    Label(root, text="Address:", font=("Arial", 20)).pack()
    Entry(root, textvariable=self.address, font=("Arial", 20)).pack()

    Label(root, text="Telephone:", font=("Arial", 20)).pack()
    Entry(root, textvariable=self.telephone, font=("Arial", 20)).pack()

    Label(root, text="Username:", font=("Arial", 20)).pack()
    Entry(root, textvariable=self.username, font=("Arial", 20)).pack()

    Label(root, text="Password:", font=("Arial", 20)).pack()
    Entry(root, textvariable=self.password, show="*",
          font=("Arial", 20)).pack()

    Button(root,
           text="Register",
           command=self.register,
           height=2,
           width=10,
           font=("Arial", 15)).pack(pady=10)
    Button(root,
           text="Back",
           command=self.go_back,
           height=2,
           width=10,
           font=("Arial", 15)).pack(pady=10)
    Button(root,
           text="Reset",
           command=self.reset,
           height=2,
           width=10,
           font=("Arial", 15)).pack(pady=10)

  def register(self):
    name = self.name.get()
    address = self.address.get()
    telephone = self.telephone.get()
    username = self.username.get()
    password = self.password.get()

    if not name or not address or not telephone or not username or not password:
      self.display_error("Enter all the fields")
    else:
      if len(telephone) != 10:
        self.display_error("Please enter 10 digits for a phone number")
      
      if (len(password) < 8):
        self.display_error("Please enter a minimum of 8 characters")
      elif not re.search(r"[a-z]", password):
        self.display_error("Please enter a minimum of one lowercase alphabet")
      elif not re.search(r"[A-Z]", password):
        self.display_error("Please enter a minimum of one uppercase alphabet")
      elif not re.search(r"[0-9]", password):
        self.display_error("Please enter a minimum of one digit")
      elif not re.search(r"[_!@#$%^&]", password):
        self.display_error("Please enter a minimum of one special character")
      elif re.search(r"\s", password):
        self.display_error("Please don't include spaces")
      else:
        if self.user_manager.add_user(name, address, telephone, username,
                                      password):
          messagebox.showinfo("Success", "User successfully registered!")
          self.root.destroy()
        else:
          self.display_error("User Already Exists")

  def reset(self):
    self.name.set("")
    self.address.set("")
    self.telephone.set("")
    self.username.set("")
    self.password.set("")

  def go_back(self):
    self.root.destroy()

  def display_error(self, message):
    messagebox.showerror("Registration Error", message)


class LoginPage:

  def __init__(self, root):
    self.root = root
    self.root.configure(bg="#d7dae2")
    self.user_manager = UserManager()

    self.root.geometry("1280x720")
    self.root.title("Login")
    Label(root,
          text="LOGIN PAGE",
          font=('Arial', 50, 'bold'),
          fg="#ed3833",
          bg="#d7dae2").pack(pady=20)

    self.username = StringVar()
    self.password = StringVar()

    Label(root, text="Username:", font=("Arial", 20)).pack()
    Entry(root, textvariable=self.username, font=("Arial", 20)).pack()

    Label(root, text="Password:", font=("Arial", 20)).pack()
    Entry(root, textvariable=self.password, show="*",
          font=("Arial", 20)).pack()

    Button(root,
           text="Login",
           command=self.login,
           height=2,
           width=10,
           font=("Arial", 15)).pack(pady=10)
    Button(root,
           text="Back",
           command=self.go_back,
           height=2,
           width=10,
           font=("Arial", 15)).pack(pady=10)

  def login(self):
    username = self.username.get()
    password = self.password.get()

    if self.user_manager.check_user_exists(username):
      stored_password = self.user_manager.users[username]['password']
      if password == stored_password:
        messagebox.showinfo("Success", "Login successful!")
        self.root.destroy()
        root = tk.Toplevel()
        home.main(root)
      else:
        self.display_error("Incorrect password")
    else:
      self.display_error("User does not exist")

  def go_back(self):
    self.root.destroy()

  def display_error(self, message):
    messagebox.showerror("Login Error", message)


# Modify your main() function to return the Tk instance
def main():
  root = tk.Tk()
  welcome_page = WelcomePage(root)
  root.mainloop()


main()
