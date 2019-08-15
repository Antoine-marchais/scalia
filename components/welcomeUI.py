import tkinter as tk

class WelcomeUI(tk.Frame):
    """
    title screen for the Scalia App
    """
    def __init__(self,parent,w,h):
        super().__init__(parent.master,width=w,height=h)
        title = tk.Label(self,text="Welcome to the scalia App",font=("Fixedsys",20,"bold"))
        title.place(relx=0.5,rely=0.5,anchor=tk.CENTER)




