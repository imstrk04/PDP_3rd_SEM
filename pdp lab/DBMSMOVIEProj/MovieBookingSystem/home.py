from functools import partial
import tkinter as tk
from tkinter import messagebox, Canvas, Frame, Scrollbar, VERTICAL
from PIL import Image, ImageTk
import sqlite3
import io


class Movie:

  def __init__(self, title, image_data):
    self.title = title
    self.image_data = image_data

  def resize_image(self, width, height):
    img = Image.open(io.BytesIO(self.image_data))
    img = img.resize((width, height))
    return ImageTk.PhotoImage(img)


class MovieBookingSystem:

  def __init__(self, root):
    self.root = root
    self.root.title("Movie Booking System")
    self.create_gui_elements()

  def create_gui_elements(self):
    self.welcome_label = tk.Label(self.root,
                                  text="Welcome to the Movie Booking System",
                                  font=("Helvetica", 18),
                                  pady=20)
    self.welcome_label.pack()

    self.options_button = tk.Button(self.root,
                                    text="\u2261",
                                    font=("Helvetica", 16),
                                    command=self.show_options)
    self.options_button.place(x=10, y=10)

    self.frame = Frame(self.root)
    self.frame.pack(fill=tk.BOTH, expand=True)

    self.scrollbar = Scrollbar(self.frame, orient=VERTICAL)
    self.canvas = Canvas(self.frame,
                         bg="white",
                         yscrollcommand=self.scrollbar.set,
                         width=self.root.winfo_screenwidth() - 30,
                         height=self.root.winfo_screenheight())
    self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    self.scrollbar.config(command=self.canvas.yview)
    self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    self.movie_frame = Frame(self.canvas, bg="white")
    self.canvas.create_window((0, 0), window=self.movie_frame, anchor=tk.NW)

    self.load_movies()

  def show_options(self):
    options_menu = tk.Menu(self.root, tearoff=0)
    options_menu.add_command(
        label="My Profile",
        font=("Helvetica", 13),
        command=lambda: messagebox.showinfo("Option Selected", "My Profile"))
    options_menu.add_command(
        label="Bookings",
        font=("Helvetica", 13),
        command=lambda: messagebox.showinfo("Option Selected", "Bookings"))
    options_menu.add_command(
        label="Log Out",
        font=("Helvetica", 13),
        command=lambda: messagebox.showinfo("Option Selected", "Log Out"))
    options_menu.post(
        self.options_button.winfo_rootx(),
        self.options_button.winfo_rooty() + self.options_button.winfo_height())

  def fetch_movies_from_database(self):
    connection_obj = sqlite3.connect('MovieBookingSystem/data.db')
    cursor_obj = connection_obj.cursor()

    # Fetch movie details from the database
    cursor_obj.execute("SELECT name, image FROM MOVIES")
    movies = cursor_obj.fetchall()

    connection_obj.close()

    return [Movie(title, image_data) for title, image_data in movies]

  def load_movies(self):
    columns = 4
    movies = self.fetch_movies_from_database()

    # Store PhotoImage objects in a dictionary
    self.movie_images = {}

    for i, movie in enumerate(movies):
      poster_image = movie.resize_image(300, 450)

      button = tk.Button(self.movie_frame,
                         image=poster_image,
                         command=lambda: self.movie_selected(movie.title))
      button.photo = poster_image
      button.grid(row=i // columns, column=i % columns, padx=40, pady=20)

      # Store the PhotoImage object in the dictionary
      self.movie_images[movie.title] = poster_image

    self.canvas.update_idletasks()
    self.canvas.configure(scrollregion=self.canvas.bbox(tk.ALL))

  def movie_selected(self, movie_title):
    messagebox.showinfo("Movie Selected", f"You have selected {movie_title}")


def main(root):
  app = MovieBookingSystem(root)
  root.mainloop()
