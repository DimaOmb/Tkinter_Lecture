from tkinter import *
from tkinter import ttk

root = Tk()
root.title('title')
root.geometry("400x400")


def show_order():
	top_text = ""
	for top in toppings.values():
		if top.get() != "":
			top_text += top.get() +", "
	text = f"{pizza_size.get()}\n{top_text}"
	Label(root, text = text).pack(pady = 5)

	orders = [child_obj for child_name, child_obj in root.children.items() if 'label' in child_name.lower()]
	if len(orders) > 3:
		for ord in orders:
			ord.destroy()


pizza_size_options = ["Small", "Medium", "Large"]

pizza_size = StringVar(value=pizza_size_options[0])
# pizza_size = StringVar()

for pz in pizza_size_options:
	Radiobutton(root, text=pz, variable=pizza_size, value=pz).pack(anchor=W, pady= 5)

Label(root, name = "top", text = "Topping").pack()

toppings = {
		'Pepperoni': StringVar(),
		 'Cheese': StringVar(),
		 'Mushroom': StringVar(),
		 'Onion' : StringVar()
		}

for top_name, top_var in toppings.items():
	Checkbutton(root, text=top_name, variable=top_var, onvalue=top_name, offvalue="").pack(anchor=W)


Button(root, text="show order", command = show_order).pack()
root.mainloop()