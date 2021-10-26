from tkinter import *
from tkinter import ttk
import mysql.connector
import os
import sys

mysql.connector.__version__
def get_city_data():
    conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="gooly")
    cur = conn.cursor()
    sql = "select * from city;"
    cur.execute(sql)
    ans = [_[0] for _ in cur.fetchall()]
    return ans


root = Tk()
root.title('title')
root.geometry("400x400")

cities = get_city_data()
clicked = StringVar(value = cities[0])

myCombo = ttk.Combobox(root, value=cities, textvariable=clicked, state="readonly")
myCombo.pack()

Label(root, textvariable=clicked).pack()

root.mainloop()
