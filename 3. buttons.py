import tkinter as tk
import random as rnd

root = tk.Tk()
root.title('this is a title')

myButton = tk.Button(root, text="i dont do anything")

"""--------- activeforeground \ activeforeground ---------"""
myButton.config(activeforeground= 'yellow')
myButton.config(activebackground= 'blue')

""" ---- state ---- """
# myButton['state'] = tk.DISABLED
# myButton['state'] = tk.ACTIVE

"""--------- size ---------"""
myButton['width'] = 100
myButton['height'] = 10

myButton.pack()

"""============= button with command ================"""
tk.Button(root, text="i print Hello!", command=lambda: print("hello")).pack()

tk.mainloop()
