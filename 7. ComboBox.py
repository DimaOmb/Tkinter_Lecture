from tkinter import *
from tkinter import ttk

root = Tk()
root.title('title')

root.geometry("400x400")

clicked = StringVar()

Label(root, text = "what is your favorite color?").pack()
myCombo = ttk.Combobox(root,
					   value=["red","green","blue","yellow"],
					   textvariable = clicked,
					   # state="readonly",
					   state="disabled"
					   )
# myCombo.current(0)
myCombo.pack()

Label(root, textvariable = clicked).pack()


root.mainloop()