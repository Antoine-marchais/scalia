import tkinter as tk 
from components import customWidgets as cw
import gameStrategy

class GameUI(tk.Frame):
    """
    game UI where the user is shown sequences according to its previous selection
    """
    def __init__(self,parent):
        """
        initialize the frame with a display for the randomized sequences and a next
        and exit button
        """
        super().__init__(parent.master)
        self.parent = parent
        self.picker = parent.picker
        self.nWidgets = len(parent.rd.sequences)

        #initializing and setting up the display
        self.display = tk.Canvas(self,bg="white",bd=2,relief="sunken")
        self.computeGridDim()
        self.createDisplay()
        self.nextSequence()
        self.bind("<Configure>",self.updateDisplay)

        #adding next an exit buttons
        self.display.pack(fill="both",expand=1,padx=20,pady=(12,0))
        buttons = tk.Frame(self)
        buttons.pack(fill="x",padx=20,pady=(8,12))
        exitButton = cw.Button(buttons,"end game",self.endGame)
        exitButton.pack(side=tk.LEFT)
        nextButton = cw.Button(buttons,"next",self.nextSequence)
        nextButton.pack(side=tk.RIGHT)
        self.bind("<KeyPress-space>",lambda event:self.nextSequence())
        self.focus_set()
        self.after(50,self.updateDisplay)

    def test(self,event):
        print("hello")

    def nextSequence(self):
        """
        compute the next sequence and updates the display
        """
        self.seq = self.picker.next()
        self.updateDisplay("followingNext")

    def endGame(self):
        self.parent.endGame()

    def computeGridDim(self):
        """
        given the number of widgets m, returns the dimensions (k,n)
        of the grid
        """
        self.cols = int(roof(self.nWidgets**0.5))
        self.rows = int(roof(self.nWidgets/self.cols)) 

    def createDisplay(self):
        """
        creates the widgets and a list of tag that allows acces to each 
        widget
        """
        index = 0
        L = self.display.winfo_width()
        H = self.display.winfo_height()
        size = int(L/(5*self.cols))
        self.widgetTags = []

        #filling all rows except the last one
        for i in range(self.cols):
            for j in range(self.rows-1):
                x,y = getCoord(self.cols,self.rows,i,j,H,L)
                self.display.create_text(x,y,tag=f"widget{index}",font=("Arial",size,"bold"))
                self.widgetTags.append(f"widget{index}")
                index+=1

        #centering the widgets on the last row
        v = self.nWidgets-self.cols*(self.rows-1)
        for i in range(v):
            x,y = getCoord(v,self.rows,i,self.rows-1,H,L)
            self.display.create_text(x,y,tag=f"widget{index}",font=("Arial",size,"bold"))
            self.widgetTags.append(f"widget{index}")
            index+=1

    def updateDisplay(self,*args):
        index = 0
        L = self.display.winfo_width()
        H = self.display.winfo_height()
        size = int(L/(5*self.cols))

        #filling all rows except the last one
        for i in range(self.cols):
            for j in range(self.rows-1):
                x,y = getCoord(self.cols,self.rows,i,j,H,L)
                self.display.coords(self.widgetTags[index],x,y)
                self.display.itemconfig(self.widgetTags[index],font=("Arial",size,"bold"))
                index+=1

        #centering the widgets on the last row
        v = self.nWidgets-self.cols*(self.rows-1)
        for i in range(v):
            x,y = getCoord(v,self.rows,i,self.rows-1,H,L)
            self.display.coords(self.widgetTags[index],x,y)
            self.display.itemconfig(self.widgetTags[index],font=("Arial",size,"bold"))
            index+=1

        if self.seq == None : 
            self.endGame()
        else :
            for i in range(len(self.seq)):
                self.display.itemconfig(self.widgetTags[i],text=self.seq[i])



def roof(x):
    """
    returns the int above x if x has a non zero decimal part
    """
    if x//1==x:
        return x
    else:
        return x//1 + 1

def getCoord(k,n,i,j,H,L):
    """
    computes the coordinate of widget of indexes i,j given the dimensions
    of the widget and the grid

    Parameters:
        k (int): number of columns
        n (int):number of lines
        i (int): index of the column
        j (int): index of the line
        H (float): height of the canvas
        L (float): width of the canvas

    Returns:
        (x,y) (tuple of floats): couple of coordinates

    """
    x = L/k*i + L/(2*k)
    y = H/n*j + H/(2*n)
    return (x,y)    