from tkinter import Toplevel
from todo import Todo
from clock import Clock

class Home:
    def __init__(self, root):
        self.root = root

    def open_dashboard(self):
        dashboard = Toplevel(self.root)
        dashboard.geometry("800x600+200+100")
        dashboard.title("Dashboard")

        # Clock
        Clock(dashboard).pack(side="top", anchor="ne")

        # Todo List
        todo_frame = Todo(dashboard)
        todo_frame.pack(expand=True, fill="both")
