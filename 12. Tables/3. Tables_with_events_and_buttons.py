from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Title')
# root.geometry("700x400")

def set_table(columns):
    table = ttk.Treeview(root, columns = columns)

    # Formate Our Columns
    table.column("#0", width=0, stretch=NO)
    table.heading("#0", text="", anchor=CENTER)

    for col in columns:
        table.column(col, anchor=CENTER, width=140)
        # Create Headings
        table.heading(col, text=col, anchor=CENTER)

    table.column("ID", anchor=CENTER, width=10)
    return table
my_table = set_table(["ID", "Name", "Last Name", 'Favorite Ice Cream'])

data = [(1,"ישראל", "רוזן", "Coffee"),
        (2,"Dima", "Omberg", "Choco Chips"),
        (3,"Shlomo", "Artzi", "banana"),
        (4,"Arik", "Einstein", "Strawberry"),
        ]

def add_row(row):
    my_table.insert(parent='', index='end', values=row)

for row in data:
    add_row(row)

selected_row = {
    'id': StringVar(),
    'name': StringVar(),
    'last_name': StringVar(),
    'ice_cream': StringVar()
}

# ----------- set text entry -----------
entry_frame = LabelFrame(root, padx=10, pady=10, text = "Row Frame")
entry_frame.pack(pady=20)

for i, (col, var) in enumerate(selected_row.items()):
    Label(entry_frame, text=col).grid(row=0, column=i)
    Entry(entry_frame, textvariable = var,  width=20, justify='center').grid(row = 1, column = i)

def clear_entries():
    for var in selected_row.values():
        var.set('')

def populate_entries_with_selected_row(event):
    # print(event)
    values = my_table.item(my_table.focus(), 'values')
    # print(values)
    for i, var in enumerate(selected_row.values()):
        var.set(values[i])

def add_new_row():
    new_row = [var.get() for var in selected_row.values()]
    add_row(new_row)
    clear_entries()

def update_selcted_row():
    selected_row_index = my_table.focus() # index
    values_from_dict = [var.get() for var in selected_row.values()]
    my_table.item(selected_row_index, values=values_from_dict)

def delete_selected_rows():
    clear_entries()
    for record in my_table.selection():
        my_table.delete(record)


my_table.bind("<<TreeviewSelect>>", populate_entries_with_selected_row)
my_table.pack()

# ----------- buttons -----------
button_frame = LabelFrame(root, padx=10, pady=10, text = "Buttons Frame")
button_frame.pack(pady=20)



clear_btn = Button(button_frame, text = 'Clear Entry', comman = clear_entries)
clear_btn.grid(row = 0, column = 0, padx= 5)
add_new_row_btn = Button(button_frame, text = 'Add New', comman = add_new_row)
add_new_row_btn.grid(row = 0, column = 1, padx= 5)
update_row_btn = Button(button_frame, text = 'Update', comman = update_selcted_row)
update_row_btn.grid(row = 0, column = 2, padx= 5)
delete_rows_btn = Button(button_frame, text = 'Delete', comman = delete_selected_rows)
delete_rows_btn.grid(row = 0, column = 3, padx= 5)

root.mainloop()
