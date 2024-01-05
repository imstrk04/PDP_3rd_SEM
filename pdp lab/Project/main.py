import tkinter as tk
from tkinter import Toplevel
from pdpProj.login import LoginPage, UserManager
from clock import Clock
from todo import Todo

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.user_manager = UserManager()
        self.login_page = LoginPage(self.root, on_login_callback=self.on_login)

    def on_login(self, username):
        if username:
            self.login_page.destroy()
            self.show_dashboard()

    def show_dashboard(self):
        dashboard = Toplevel(self.root)
        dashboard.geometry("800x600+200+100")
        dashboard.title("Dashboard")

        # Clock
        Clock(dashboard).pack(side="top", anchor="ne")

        # Todo List
        todo_frame = Todo(dashboard)
        todo_frame.pack(expand=True, fill="both")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.run()
