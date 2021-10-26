from tkinter import *


def login_Dima(username, password):
	if username == "Dima" and password == "123":
		# usernameLabel.destroy()
		# usernameEntry.destroy()
		# passwordLabel.destroy()
		# passwordEntry.destroy()
		# login_Button.destroy()

		# we can do it with this function also
		for child in tkWindow.winfo_children():
			child.destroy()

		Label(tkWindow, text = "Hello Dima").grid(row=0, column=0, pady = 20,  padx = 20 )

#window
tkWindow = Tk()
tkWindow.title('Tkinter Login Form')
tkWindow.geometry("+300+300")

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
login_Button = Button(tkWindow, text="Login", command=lambda: login_Dima(usernameEntry.get(), passwordEntry.get()))
# login_Button = Button(tkWindow, text="Login", command=login_Dima)
login_Button.grid(row=4, column=0, columnspan = 2)




tkWindow.mainloop()