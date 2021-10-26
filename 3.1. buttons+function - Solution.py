import tkinter as tk

def myClick(txt, color):
	tk.Label(root, text=txt, fg = color).pack()

root = tk.Tk()
root.title('this is a title')
root.geometry("300x500")

tk.Button(root, text="red", command=lambda: myClick("hello", "red")).pack()
tk.Button(root, text="yellow", command=lambda: myClick("hello","yellow")).pack()
tk.Button(root, text="green", command=lambda: myClick("hello", "green")).pack()
tk.Button(root, text="blue", command=lambda: myClick("hello", "blue")).pack()

root.mainloop()


