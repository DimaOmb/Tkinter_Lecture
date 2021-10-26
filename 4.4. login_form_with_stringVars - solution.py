from tkinter import *


def xyz(username, password):
	if username == "Rotem" and password == "123":
		for child in tkWindow.winfo_children():
			child.destroy()
		Label(tkWindow, text = "Hello Rotem").grid(row=0, column=0, pady = 20,  padx = 20 )

#window
tkWindow = Tk()
tkWindow.title('Tkinter Login Form')
tkWindow.geometry("+300+300")


data = {
		'user': StringVar(),
		'pass': StringVar()
		}

#username label and text entry box
Label(tkWindow, text="User Name").grid(row=0, column=0)
Entry(tkWindow, textvariable = data['user']).grid(row=0, column=1)

#password label and password entry box
Label(tkWindow,text="Password").grid(row=1, column=0)
Entry(tkWindow, show='*', textvariable = data['pass']).grid(row=1, column=1)

#login button
login_Button = Button(tkWindow, text="Login", command=lambda: xyz(data['user'].get(), data['pass'].get()))
login_Button.grid(row=4, column=0, columnspan = 2)




tkWindow.mainloop()