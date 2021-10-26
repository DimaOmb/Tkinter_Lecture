import tkinter as tk

# tk.TkVersion

# 1. create window
root = tk.Tk()
root.title('this is a title')

"""---- set window_size + location ----"""
root.geometry("500x100") # .geometry("widthxheight")
# root.geometry("500x100+300+300") # .geometry("window width x window height + position right + position down")


"""---- set max\min window size ----"""
root.maxsize(width = 500, height=200)
root.minsize(width = 100, height=10)

"""---- set max\min window size ----"""
root.resizable(width=False, height=True)

"""---- set window background color ----"""
# root.configure(bg='blue') # bg = background_color
# root['bg']='green'
root['background']='yellow'
# root['background']='#856ff8' # Using HEX code for background color

root['cursor'] = "pirate" # arrow \ pirate \ mouse

""" ====================== content goes here ====================== """


# 2. run window
tk.mainloop() # clicking on the X closes the window and ends the program


