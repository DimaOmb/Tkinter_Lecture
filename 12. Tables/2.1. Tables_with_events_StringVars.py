from tkinter import *
from tkinter import ttk


def add_row(row):
    my_table.insert(parent='', index='end', values=row)


def populate_entries_with_selected_row(event):
    # print(event)
    row_index = my_table.focus()
    values = my_table.item(row_index, 'values')

    selected_row['id'].set(values[0])
    selected_row['name'].set(values[1])
    selected_row['last_name'].set(values[2])
    selected_row['ice_cream'].set(values[3])

    # for i, var in enumerate(selected_row.values()):
    #     var.set(values[i])




root = Tk()
root.title('Title')
root.geometry("700x400")

my_table = ttk.Treeview(root)
my_table['columns'] = ["id", "name", "last_name", 'ice_cream']

# Formate Our Columns
my_table.column("#0", width=0, stretch=NO)
my_table.column("id", anchor=CENTER, width=10)
my_table.column("name", anchor=CENTER, width=140)
my_table.column("last_name", anchor=CENTER, width=140)
my_table.column("ice_cream", anchor=CENTER, width=140)

# Create Headings
my_table.heading("#0", text="", anchor=CENTER)
my_table.heading("id", text="ID", anchor=CENTER)
my_table.heading("name", text="Name", anchor=CENTER)
my_table.heading("last_name", text="Last Name", anchor=CENTER)
my_table.heading("ice_cream", text="Favorite Ice Cream", anchor=CENTER)


"""============================  Data  ============================"""

data = [(1,"ישראל", "רוזן", "Coffee"),
        (2,"Dima", "Omberg", "Choco Chips"),
        (3,"Shlomo", "Artzi", "banana"),
        (4,"Arik", "Einstein", "Strawberry"),
        ]

selected_row = {
    'id': StringVar(),
    'name': StringVar(),
    'last_name': StringVar(),
    'ice_cream':StringVar()
}

for row in data:
    add_row(row)

# ----------- set text entry -----------
entry_frame = LabelFrame(root, padx=10, pady=10, text = "Row Frame")
entry_frame.pack(pady=20)

for i, (col, var) in enumerate(selected_row.items()):
    Label(entry_frame, text=col).grid(row=0, column=i)
    Entry(entry_frame, textvariable = var,  width=20, justify='center').grid(row = 1, column = i)


my_table.bind("<<TreeviewSelect>>", populate_entries_with_selected_row)

my_table.pack()
root.mainloop()
