import tkinter as tk
from tkinter.ttk import *

def close_current_window_show_main(win):
    root.deiconify()
    win.destroy()

def open_new_window():
    root.withdraw()
    # global newWindow # need to be global else the new window is a local variable and cannot be closed
    newWindow = tk.Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("300x200+150+300")
    Label(newWindow, text="This is a new window").pack()
    l = Label(root, text="This is the main window")
    Button(newWindow, text = "Go back", command = lambda : close_current_window_show_main(newWindow)).pack()


root = tk.Tk()
root.title('this is a title')

tk.Label(root, text = "click the button").pack()
tk.Button(root, text="Click Me!", command= open_new_window).pack()

root.mainloop()


