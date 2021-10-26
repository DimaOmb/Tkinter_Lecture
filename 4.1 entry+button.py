from tkinter import *

root = Tk()
# root.geometry("100x100")


e = Entry(root, width=20)
e.pack()
e.insert(0, "name: ")


def myClick():
	hello = "Hello " + e.get()
	myLabel = Label(root, text=hello)
	e.delete(0, 'end')
	myLabel.pack()

Button(root, text="Say Hello", command= lambda: myClick() ).pack()
Button(root, text="remove entry", command=e.destroy).pack()

#TODO: 1. add button that changes text in the same Label
#TODO: 2. add button that changes text in the same Label and adds another label

root.mainloop()

