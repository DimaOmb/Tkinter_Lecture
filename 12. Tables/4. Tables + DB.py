from tkinter import *
from tkinter import ttk


import mysql.connector

conn_gooly = mysql.connector.connect(host="localhost", user="root", password="1234", database="Gooly")
cursor = conn_gooly.cursor()

"""========== funtions =========="""
def get_data_from_DB(cur, columns_list=[]):
    if len(columns_list) > 0:
        columns = ", ".join(columns_list)
        cur.execute(f'SELECT {columns} FROM gooly.sadnaot;')
        ans = cur.fetchall()
        return ans


def add_row(row):
    my_table.insert(parent='', index='end', values=row)


def populate_table(cur, columns_list=[]):
    data = get_data_from_DB(cur, columns_list)
    for row in data:
        add_row(row)


def populate_entries_with_selected_row(event):
    # print(event)

    values = my_table.item(my_table.focus(), 'values')

    # turn values (list) to dictionary {col_name: value)
    ans = {my_table['columns'][i]: val for i, val in enumerate(values)}
    ans = {}
    for i, val in enumerate(values):
        key = my_table['columns'][i]
        ans[key]= val

    for col in ans.keys():
        selected_sadna[col].set(ans[col])



"""========================================"""

root = Tk()
root.title('Title')

my_table = ttk.Treeview(root, columns=["sadna_id", "name", "description", "duration", "base_cost", "base_price"])

# Formate Our Columns + Create Headings
my_table.column("#0", width=0, stretch=NO)
my_table.heading("#0", text="", anchor=CENTER)

for col in my_table['columns']:
    my_table.column(col, anchor=CENTER, minwidth=10, stretch=YES)
    my_table.heading(col, text=col, anchor=CENTER)

populate_table(cursor, my_table['columns'])

selected_sadna = {"sadna_id": StringVar(),
                  "name": StringVar(),
                  "description":StringVar(),
                  "duration": StringVar(),
                  "base_cost": StringVar(),
                  "base_price": StringVar()
                  }

# ----------- set text entry -----------
entry_frame = LabelFrame(root, padx=10, pady=10, text="Row Frame")
entry_frame.pack(pady=20)

for i, (col, var) in enumerate(selected_sadna.items()):
    Label(entry_frame, text=col).grid(row=0, column=i)
    if col == 'sadna_id':
        Label(entry_frame, textvariable = var,  width=20, justify='center').grid(row = 1, column = i)
    else:
        Entry(entry_frame, textvariable = var,  width=20, justify='center').grid(row = 1, column = i)


my_table.bind("<<TreeviewSelect>>", populate_entries_with_selected_row)
my_table.pack()



root.mainloop()

# TODO: change the table to select data from customers
