from tkinter import *

root = Tk()
root.title('title')
root.geometry("400x400")


def show():
    text = want_pizza.get() + " " +  size.get()
    Label(root, text=text).pack()


want_pizza = StringVar()
size = StringVar()

pizza_check = Checkbutton(root, text="Want a pizza?", variable=want_pizza, onvalue="Yes :)", offvalue="No :(" , command=show)
size_check = Checkbutton(root, text="Big?", variable=size, onvalue="Big", offvalue="Small"  ,command=show)

pizza_check.deselect()
pizza_check.pack()

size_check.deselect()
size_check.pack()
# c.pack(pady = 20, padx = 20)

myButton = Button(root, text="Show Selection", command=show).pack()
root.mainloop()
