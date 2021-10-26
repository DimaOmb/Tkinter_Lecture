from tkinter import *


root = Tk()
root.title('title')


frame1 = LabelFrame(root, padx=50, pady=50, text ="im a label")
frame1.pack(padx=10, pady=10)

frame2 = LabelFrame(root, padx=50, pady=50)
frame2.pack(padx=10, pady=10)

Button(frame1, text="Don't Click Here!").pack()
Label(frame1, text="im in the frame!").pack()
Label(root, text="im NOT in the frame!").pack()
Label(frame2, text="im in the OTHER frame!").pack()


root.mainloop()
