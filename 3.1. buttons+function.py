import tkinter as tk
import random as rnd

def myClick(txt):
	color = rnd.choice(['red', 'black', 'green', 'blue'])
	tk.Label(root, text=txt, fg = color).pack()

root = tk.Tk()
root.title('this is a title')

tk.Button(root, text="Click Me!", command=lambda: myClick("hello")).pack()

# TODO: add a function that receives color + text and outputs a label with color and text.
# TODO: add 4 buttons when each calls the function with different params


root.mainloop()


