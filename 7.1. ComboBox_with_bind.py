from tkinter import *
from tkinter import ttk
from tkinter import ttk

root = Tk()
root.title('title')

root.geometry("400x400")


def comboclick(event):
	msg = f"index: {myCombo.current()}, value: {myCombo.get()}"
	Label(root, text=msg).pack()
	Label(root, text=clicked.get()).pack()


options = [
	"red",
	"green",
	"blue",
	"yellow"
]
clicked = StringVar(value=options[0])

Label(root, text = "what is your favorite color?").pack()
myCombo = ttk.Combobox(root, value=options, textvariable = clicked)


myCombo.bind("<<ComboboxSelected>>", comboclick)
myCombo.pack()


root.mainloop()

# TODO: create a combo box that gets its values from the DB "City" table
