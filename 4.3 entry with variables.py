from tkinter import *

root = Tk()
root.geometry("100x100")

my_name = StringVar()
# my_name.set("Dima")

Entry(root, width=20, textvariable = my_name).pack()
Label(root, textvariable = my_name).pack()
Button(root, text = 'remove text', command = lambda: my_name.set("")).pack()

#TODO: login form with string vars

root.mainloop()

