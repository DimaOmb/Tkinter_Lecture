from tkinter import *


root = Tk()
root.title('title')
root.geometry("400x400")

def show():
	text = var.get()
	Label(root, text=text).pack()

var = StringVar()

c = Checkbutton(root, text="Want a pizza?",
			   variable=var,
			   onvalue="Yes :)",
			   offvalue="No :(",
				# bg = 'yellow',
				# selectcolor = 'red',
				# font = 20,
				# state=DISABLED,
				# pady = 20, padx = 20,
			   command = lambda : show())

c.deselect() # without it the check box starts as selected by default
c.pack()
# c.pack(pady = 20, padx = 20)

myButton = Button(root, text="Show Selection", command=show).pack()
root.mainloop()

#TODO: add another checkbox and every time one of the check boxes will be checked both string's values will be shown