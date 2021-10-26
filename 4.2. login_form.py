from tkinter import *

def Login(username, password):
	print("username entered :", username)
	print("password entered :", password)

#window
tkWindow = Tk()
tkWindow.title('Tkinter Login Form')
# tkWindow.geometry("500x100+300+300")


#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name")
usernameLabel.grid(row=0, column=0)
usernameEntry = Entry(tkWindow)
usernameEntry.grid(row=0, column=1)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password")
passwordLabel.grid(row=1, column=0)
passwordEntry = Entry(tkWindow, show='*')
passwordEntry.grid(row=1, column=1)

#login button
login_Button = Button(tkWindow, text="Login", command=lambda: Login(usernameEntry.get(), passwordEntry.get()))
login_Button.grid(row=2, column=0, columnspan = 2)

# TODO: add function that if the user_name == YOUR_NAME and password == 123 then delete everything on the screen and add "Hello YOUR_NAME" Label


tkWindow.mainloop()