from tkinter import *

root = Tk()
# root.geometry("200x100")
e = Entry(root)

"""-------- size --------"""
e.config(width = 100)
e.config(font = 100)
e.config(bd  = 5) # border

"""-------- color --------"""
# e.config(fg = "red")
# e.config(bg = "yellow")

"""-------- state --------"""
# e.config(state = DISABLED)

"""-------- password mode --------"""
# e.config(show="*")


e.pack()
# e.pack(pady = 100, padx = 50)
e.insert(0, "name: ")

root.mainloop()

