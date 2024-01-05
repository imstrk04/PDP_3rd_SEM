import tkinter
from tkinter import *

class Todo:

    def __init__(self):
        root = Tk()
        root.title("To-Do-List")
        root.geometry("400x650+400+100")
        root.resizable(False, False)

        self.task_list = []  # Define task_list as an attribute of the class

        def addTask():
            task = task_entry.get()
            task_entry.delete(0, END)

            if task:
                with open("tasklist.txt", 'a') as taskfile:
                    taskfile.write(f"\n{task}")
                self.task_list.append(task)
                listbox.insert(END, task)
        
        def deleteTask():
            task = str(listbox.get(ANCHOR))
            if task in self.task_list:
                self.task_list.remove(task)
                with open("tasklist.txt", 'w') as taskfile:
                    for task_item in self.task_list:
                        taskfile.write(task_item + '\n')
                listbox.delete(ANCHOR)

        def openTaskFile():
            try:
                with open("tasklist.txt", "r") as taskfile:
                    tasks = taskfile.readlines()

                for task in tasks:
                    if task != '\n':
                        self.task_list.append(task)
                        listbox.insert(END, task)
            except FileNotFoundError:
                file = open('tasklist.txt', 'w')
                file.close()

        #icon
        Image_icon = PhotoImage(file = "assets/task.png")
        root.iconphoto(False, Image_icon)

        #top bar
        TopImage = PhotoImage(file = "assets/topbar.png")
        Label(root, image= TopImage).pack()

        dockImage = PhotoImage(file = "assets/dock.png")
        Label(root, image= dockImage, bg = "#32405b").place(x = 30, y = 25)

        noteImage = PhotoImage(file = "assets/task.png")
        Label(root, image= noteImage, bg = "#32405b").place(x = 340, y = 20)

        heading = Label(root, text = "ALL TASK", font = "arial 20 bold", fg = "white", bg = "#32405b")
        heading.place(x = 150, y = 20)

        #main
        frame = Frame(root, width=400, height=50, bg="white")
        frame.place(x =0, y = 180)

        task = StringVar()
        task_entry = Entry(frame, width=18, font = "arial 20", bd = 0)
        task_entry.place(x = 10, y= 7)
        task_entry.focus()

        button = Button(frame, text="ADD", font= "arial 20 bold", width=6, bg = "#5a95ff", fg="#fff", bd = 0, command=addTask)
        button.place(x = 300, y = 0)

        #listbox
        frame1 = Frame(root, bd = 3, width=700, height=280, bg="#32405b")
        frame1.pack(pady=(160,0))

        listbox = Listbox(frame1, font = ('arial', 12), width=40, height=16, bg = "#32405b", fg = "white", cursor= "hand2", selectbackground="#5a95ff")
        listbox.pack(side=LEFT, fill=BOTH, padx=2)
        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side = RIGHT, fill = BOTH)

        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)


        #delete
        Delete_icon = PhotoImage(file = "assets/delete.png")
        Button(root, image=Delete_icon, bd = 0, command=deleteTask).pack(side = BOTTOM, pady=13 )

        Button(root, text="EXIT", height=2, width=23, bg="#00bd56", fg="white", bd=0, command=root.destroy).pack(side=BOTTOM, pady=10)

        openTaskFile()


        root.mainloop()

t = Todo()