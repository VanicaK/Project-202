import socket
from threading import Thread
from tkinter import *

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip="127.0.0.1"
port=8000

#nickname=input("Enter nickname:")

print("Connected to server")





class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")

        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=300)
        self.pls = Label(self.login,
					text = "Please login to continue",justify = CENTER,font = "Helvetica 14 bold")
        self.pls.place( relheight = 0.15,
                        relx = 0.2,
                        rely = 0.07)

        self.labelName = Label(self.login,
							text = "Name: ",
							font = "Helvetica 12")
        
        self.labelName.place(relheight = 0.2,
							relx = 0.1,
							rely = 0.2)

        self.entryName = Entry(self.login,font = "Helvetica 14")
        self.entryName.place(relwidth = 0.4,relheight = 0.12,relx = 0.35,rely = 0.2)
        self.entryName.focus()

        self.nameButton= Button(self.login,text="ENTER",command=lambda: self.loginfunc(self.entryName.get()))
        self.nameButton.place(relx= 0.55,rely=0.42,relwidth=0.3,relheight=0.12,anchor=CENTER)

        self.Window.mainloop()

    def loginfunc(self,name):
        self.login.destroy()
        self.name=name
        newthreadrec=Thread(target=self.receiveMessage)
        newthreadrec.start()

    def receiveMessage(self):
        print("you received a message")
        while True:
            try:
                message=client.recv((2048).decode("utf-8"))
                if message =="NICKNAME":
                    client.send(nickname.encode("utf-8"))
                else:
                    print(message)
            except:
                print("ERROR OCCURED, APPLICATION CLOSING")
                client.close()
                break
    


g = GUI()

        




#newthread=Thread(target=sendMessage)
#newthread.start()


