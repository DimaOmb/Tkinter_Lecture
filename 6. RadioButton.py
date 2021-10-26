from tkinter import *

root = Tk()
root.title('title')

TOPPINGS = ['Pepperoni', 'Cheese', 'Mushroom', 'Onion']

pizza = StringVar()
pizza.set(TOPPINGS[0])

for text in TOPPINGS:
	# Radiobutton(root, text=text, variable=pizza, value=text, command = lambda: clicked(pizza.get())).pack(anchor=W, pady= 5)
	Radiobutton(root, text=text, variable=pizza, value=text).pack(anchor=W, pady= 5)


def clicked(value):
	Label(root, text=value).pack()


myButton = Button(root, text="Add Pizza Topping", command=lambda: clicked(pizza.get()))
myButton.pack(pady=20)
mainloop()

#TODO: create a pizza menu:
#	Radiobox to select size of pizza: small, medium, large
#	check boxes for the topping
#	button will display the order in a new label