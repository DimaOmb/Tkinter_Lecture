from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Title')
# root.geometry("700x400")

table = ttk.Treeview(root, columns = ["ID", "Name", "Last Name", 'Favorite Ice Cream'])
# my_tree['columns'] = ["ID", "Name", "Last Name", 'Favorite Ice Cream']

# Create Headings
# my_tree.heading(col_name, text = header_name, anchor=CENTER)
table.heading("#0", text="", anchor=CENTER)
table.heading("ID", text="ID", anchor=CENTER)
table.heading("Name", text="Name", anchor=CENTER)
table.heading("Last Name", text="Last Name", anchor=CENTER)
table.heading("Favorite Ice Cream", text="Favorite Ice Cream", anchor=CENTER)

# Format Columns
table.column("#0", width=0, stretch=NO)
table.column("ID", anchor=CENTER, width=10)
table.column("Name", anchor=CENTER, width=140)
table.column("Last Name", anchor=CENTER, width=140)
table.column("Favorite Ice Cream", anchor=CENTER, width=140)


"""============================  Data  ============================"""
data = [(1,"ישראל", "רוזן", "Coffee"),
        (2,"Dima", "Omberg", "Choco Chips"),
        (3,"Shlomo", "Artzi", "banana"),
        (4,"Arik", "Einstein", "Strawberry"),
        (5, "Yevgeni", "?", "Thina")
        ]

def add_row(row):
    table.insert(parent='', index='end', values=row)


for row in data:
    table.insert(parent='', index='end', values=row)
    # add_row(row)

# TODO: add more rows/data
# TODO: add new column "favorite movie" and add content

table.pack()
root.mainloop()
