from tkinter import *

root = Tk()
root.geometry("300x100")

e = Entry(root, width=20)
e.pack()


def myClick():
	Label(root, text = e.get()).pack()
	main_label['text'] = e.get()
	e.delete(0, 'end')

Button(root, text="Say Hello", command=myClick).pack()
main_label = Label(root)
main_label.pack()

root.mainloop()

