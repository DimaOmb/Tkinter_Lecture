import tkinter as tk
from tkinter.messagebox import *


root = tk.Tk()
root.title('title')

def popup():
    # response = showinfo(title="this is title", message="this is msg")
    response = showwarning(title="this is title", message="this is msg")
    # response = askquestion(title="this is title", message="this is msg")
    response = askokcancel(title="this is title", message="this is msg")
    # response = askyesno(title="this is title", message="this is msg")
    response = askyesnocancel(title="this is title", message="this is msg")


tk.Button(root, text='show pop up', command= popup).pack()

tk.mainloop()
