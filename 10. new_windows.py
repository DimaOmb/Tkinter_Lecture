import tkinter as tk
from tkinter.ttk import *

def open_new_window():
    newWindow = tk.Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("200x200")
    Label(newWindow, text="This is a new window").pack()
    l = Label(root, text="This is the main window")

root = tk.Tk()
root.title('this is a title')

tk.Button(root, text="Click Me!", command= open_new_window).pack()


root.mainloop()


