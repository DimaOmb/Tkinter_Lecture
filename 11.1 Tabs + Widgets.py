from tkinter import *
from tkinter import ttk

root = Tk()
root.title('tabs')



tabControl = ttk.Notebook(root, width = 1000, height = 500)
tabControl.pack()


sadnaot_tab = Frame(tabControl)
customers_tab = Frame(tabControl)
orders_tab = Frame(tabControl)

tabControl.add(sadnaot_tab, text="tab1")
tabControl.add(customers_tab, text="tab2")
tabControl.add(orders_tab, text="tab3")

Label(sadnaot_tab, text = "this is the first tab").pack(pady=20)
Entry(sadnaot_tab).pack()
Label(customers_tab, text = "this is the second tab").pack(pady=20)
Label(orders_tab, text = "this is the third tab").pack(pady=20)

# with function
def put_inside_tab(tab):
    Label(tab, text = "this is a label1 from function").pack()
    Label(tab, text = "this is a label2 from function").pack()
    Label(tab, text = "this is a label3 from function").pack()
    Label(tab, text = "this is a label4 from function").pack()

put_inside_tab(orders_tab)
put_inside_tab(sadnaot_tab)
put_inside_tab(sadnaot_tab)

root.mainloop()

