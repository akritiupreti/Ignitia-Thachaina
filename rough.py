import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox


my_window = Tk()
my_window.geometry("650x350")

class Thachaina(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=False)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Home, Main):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

def openFile():
    filepath = filedialog.askopenfilename(title="Open file",
                                          filetypes=(("JPG files", "*.jpg"), ("PNG files", "*.png"), ("JPEG files", "*.jpeg"), ("all files", "*.*")))
    if filepath:
        with open(filepath, 'r') as file:
            # Do something with the file
            pass
    print(filepath)


my_window.resizable(False, False)
my_window.title("Ignitia Hackathon")

# Create a style for ttk widgets
style = ttk.Style(my_window)
style.theme_use('clam')

# Configure style for the 'Open' button
style.configure('TButton',
                font=('Helvetica', 12),
                padding=10)

# Configure style for the label
style.configure('TLabel',
                font=('Helvetica', 15),
                padding=10)

# Configure style for the main window
style.configure('TFrame',
                background='#aedb9f')

main_frame = ttk.Frame(my_window, style='TFrame')
main_frame.pack(pady=20)

# Create a spacer frame to occupy space at the top
spacer_frame = ttk.Frame(main_frame, height=100)
spacer_frame.pack()

# Create the label
label = ttk.Label(main_frame, text="Team Thachaina", style='TLabel')
label.pack()

p1 = PhotoImage(file='logo.png')
my_window.iconphoto(False, p1)

# Create a spacer frame to occupy space in the middle
spacer_frame = ttk.Frame(main_frame, height=100)
spacer_frame.pack()

# Create the 'Open' button
open_button = ttk.Button(main_frame, text="Open", command=openFile)
open_button.pack()

# Create a spacer frame to occupy space at the bottom
spacer_frame = ttk.Frame(main_frame, height=100)
spacer_frame.pack()

# Configure background color for the main window
my_window.configure(bg='#e6f2ff')

my_window.mainloop()
