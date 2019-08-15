import tkinter as tk 

bigFont = ("Fixedsys",16,"bold")
mediumFont = ("Fixedsys",12,"bold")
smallFont = ("Fixedsys",10)
smallItalic = ("Fixedsys",10,"italic")

class Button(tk.Button):

    def __init__(self,parent,text,command):
        super().__init__(parent,text=text,command=command,font=smallFont)

class InField(tk.Frame):
    """
    custom text field that supports placeholders and an add button
    """
    def __init__(self,parent,command,textVariable=None,placeholder="click to type in"):
        """
        initializing the field with placeholder if no value was set before
        """
        super().__init__(parent)
        self.config(bg="white",bd=2,relief="sunken")
        self.placeholder = placeholder
        self.command=command

        #creating the variable if it does not already exist
        if textVariable!=None:
            self.var = textVariable
        else : 
            self.var = tk.StringVar()
        val = self.var.get()
        self.display = tk.StringVar()
        
        #adding the entry field
        self.entry = tk.Entry(self,textvariable=self.display)
        self.entry.pack(side=tk.LEFT,padx=12,pady=6,fill=tk.X,expand=1)
        self.entry.config(bd=0,highlightthickness=0,bg="white")

        #setting the placeholder if the variable is empty
        if val == "":
            self.display.set(placeholder)
            self.entry.config(font=smallItalic)
            self.entry.config(fg="gray")
        else: 
            self.display.set(val)

        #adding and styling the button
        self.addButton = tk.Button(self,command=self.validate,text="+",font=("Fixedsys",12,"bold"),bg="lightblue",fg="white")
        self.addButton.config()
        self.addButton.pack(side=tk.LEFT,padx=10,pady=6)
        self.bind("<FocusIn>",self.removePlaceholder)
        self.bind("<FocusOut>",self.displayPlaceholder)
        self.entry.bind("<Any-KeyRelease>",self.updateVar)
        self.entry.bind("<KeyPress-Return>",self.validate)

    def removePlaceholder(self,*args):
        """
        remove placeholder when the field gains focus
        """
        if self.var.get() == "":
            self.entry.config(font=smallFont)
            self.entry.config(fg="black")
            self.display.set("")
        
    def displayPlaceholder(self,*args):
        """
        putting back placeholder when the field loses focus and the vaiable is empty
        """
        if self.var.get() == "":
            self.entry.config(font=smallFont)
            self.entry.config(fg="gray")
            self.display.set(self.placeholder)

    def updateVar(self,*args):
        """
        binds the displayed value to the string variable provided
        """
        self.var.set(self.display.get())

    def validate(self,*args):
        self.command(self.var)
        self.display.set("")
        self.var.set("")


class MutableListBox(tk.Frame):
    """
    a list box that updates according to a list of elements, from which you can remove items
    """
    def __init__(self,parent,height=181):
        """
        initializing the widget with a scrollbar
        """
        #initializing the widget with a frame inside a canvas
        super().__init__(parent,height=181)
        self.config(bd=2,relief="sunken")
        self.canvas = tk.Canvas(self,borderwidth=0,height=180)
        self.frame = tk.Frame(self.canvas)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.canvas.pack(side="left", fill="x", expand=True)
        self.canvas.create_window((0,0), window=self.frame, anchor="nw",tags="self.frame",width=self.winfo_width())

        #binding frame movement to the scrollbar
        self.bind("<Configure>", self.updateWidth)
        self.frame.bind("<Configure>",self.onFrameConfigure)

        #trace the modification of the listed elements
        self.elements=tk.StringVar()
        self.elements.trace("w",self.updateDisplay)
        self.displayedElts = []
        self.updateDisplay()

    def onFrameConfigure(self,event):
        '''Reset the scroll region to encompass the inner frame'''
        if len(self.getElts())>5 :
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            self.vsb.pack(side="right", fill="y")
            self.vsb.update()
        else : 
            self.vsb.pack_forget()

    def updateWidth(self,event):
        """
        follow the width of the parent widget
        """
        self.canvas.itemconfigure("self.frame",width=int(event.width))
    
    def updateDisplay(self,*args):
        """
        modify the list displayed whenever there is a modification of the
        variable that lists the elements
        """
        i=0
        for elt in self.displayedElts:
            elt.destroy()
        self.displayedElts = []
        for elt in self.getElts():
            if i%2 == 0 :
                displayedElt = RemovableElement(self,elt,bg="white")
            elif i%2 == 1 :
                displayedElt = RemovableElement(self,elt,bg="lightgray")
            self.displayedElts.append(displayedElt)    
            displayedElt.pack(fill=tk.X)
            i+=1
        while i<5 :
            if i%2 == 0 :
                displayedElt = tk.Frame(self.frame,bg="white",height=36)
            elif i%2 == 1 :
                displayedElt = tk.Frame(self.frame,bg="lightgray",height=36)
            self.displayedElts.append(displayedElt)    
            displayedElt.pack(fill=tk.X)
            i+=1
        self.onFrameConfigure("whatever")

    def trace(self,callback):
        """
        gets called when the list is modified, the call back must take
        the list of elements as argument
        """
        def extendedCallback(*args):
            callback(self.getElts())
        self.elements.trace("w",extendedCallback)

    def setElts(self,elts):
        """
        setter for the list of elements
        """
        self.elements.set("/".join(elts))

    def getElts(self):
        """
        getter for the lis of elements
        """
        if self.elements.get() == "":
            return []
        else :
            return self.elements.get().split("/")

class RemovableElement(tk.Frame):
    """
    a removable element to be inserted in a listBox
    """
    def __init__(self,parent,text,bg="white"):
        super().__init__(parent.frame,bg=bg)
        self.text = text
        self.parent = parent
        self.label = tk.Label(self,text=text,bg=bg,anchor="w",font=smallFont)
        self.label.pack(side=tk.LEFT,fill=tk.X,expand=True)
        self.button = tk.Button(self,text="-",font=("Fixedsys",8,"bold"),command=self.destroyElt)
        self.button.pack(side=tk.LEFT,padx=30,pady = 6)

    def destroyElt(self,*args):
        elts = self.parent.getElts()
        elts.remove(self.text)
        self.parent.setElts(elts)
