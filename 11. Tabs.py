from tkinter import *
from tkinter import ttk

root = Tk()
root.title('tabs')



tabControl = ttk.Notebook(root, width = 1000, height = 500)
tabControl.pack()


def show():
	tabControl.add(my_frame2, text="Red Tab")

my_frame1 = Frame(tabControl, bg="blue")
my_frame2 = Frame(tabControl, bg="red")

tabControl.add(my_frame1, text="Blue Tab")
tabControl.add(my_frame2, text="Red Tab")

# Hide a tab
Button(my_frame1, text="Hide Tab 2", command=lambda: tabControl.hide(my_frame2)).pack(pady=10)

# Show a tab
# Button(my_frame1, text="Show Tab 2", command=show).pack(pady=10)

# Navigate to a tab
# Button(my_frame1, text="Navigate To Tab 2", command=lambda: tabControl.select(1)).pack(pady=10)

Label(my_frame2, text = "this is a label").pack()
root.mainloop()

