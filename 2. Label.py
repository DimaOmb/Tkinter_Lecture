import tkinter as tk


# 1. create window
root = tk.Tk()
root.title('this is a title')
root.geometry("500x450")


# 2. add content
# 2.1 Creating a Label Widget
myLabel = tk.Label(root, text="Hello World!")
myLabel2 = tk.Label(root, text="label2")
""" ----- text color, font and size ----- """
myLabel['fg']="red"
myLabel['font']=("ariel", 18) # (font, font_size)

""" ----- background color ----- """
# myLabel['bg']="black"

""" ----- size ----- """
# myLabel['height']= 10
# myLabel['width']= 100
#
#
myLabel["text"] = "other text" # set new text

# 2.2 put it onto the screen
# myLabel.pack()
# myLabel.pack(anchor = "w")
# myLabel.pack(anchor = "e")

""" ----- padding ----- """
myLabel.pack(pady = 50, padx = 100)
myLabel2.pack()
# 3. run window
root.mainloop() # clicking on the X closes the window and ends the program
