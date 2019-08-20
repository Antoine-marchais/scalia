import tkinter as tk
from components import customWidgets as cw

class SelectionUI(tk.Frame):
    """
    Selection menu where the user sets up his next game
    """
    def __init__(self,parent):
        """
        pack the Gamemode menu, the sequence menu and a start button
        """
        super().__init__(parent.master)
        self.parent = parent

        #title 
        title = tk.Label(self,text="Game selection",font=("Fixedsys",16,"bold"))
        title.pack(pady = (40,20))

        #gamemode Frame
        self.gamemode = tk.Frame(self,bd=2,relief="sunken")
        self.gamemode.pack(fill="both",padx=30,pady=20,expand=1)
        
        #adding mode selection in the gamemode frame
        modeSelection = tk.Frame(self.gamemode)
        modeSelection.pack(side=tk.LEFT)
        modeLabel = tk.Label(modeSelection,text="select a mode",font=("Fixedsys",12,"bold"))
        modeLabel.pack(padx=20,pady=10)
        modes = ["complete","arcade"]

        #adding the corresponding mode parameters to the left in the gamemode Frame
        self.modeParameters = tk.Frame(self.gamemode,bd=2,relief="groove")
        self.modeParameters.pack(side=tk.LEFT,padx=15,pady=10,fill="both",expand=1)

        #binding mode selection to the mode parameter frame
        self.chosenMode = tk.StringVar(self.gamemode)
        self.chosenMode.trace("w",self.updateModeSelection)
        self.chosenMode.set("complete")
        mode = tk.OptionMenu(modeSelection,self.chosenMode,*modes)
        mode.config(font=("Fixedsys",10))
        mode.pack(padx=20,pady=10)
        
        #sequence Frame
        sequences = tk.Frame(self)
        sequences.pack(fill=tk.X,padx=30,pady=20)

        #adding the display of current sequences
        newSequences = tk.Frame(sequences)
        newSequences.pack(side=tk.LEFT,fill=tk.X,expand=1)
        self.sequenceList = cw.MutableListBox(newSequences)
        self.sequenceList.trace(self.parent.updateSequences)
        self.sequenceList.pack(fill=tk.X,pady=(0,6))

        #adding the add sequence input
        self.addedSeq = tk.StringVar()
        addSequence = cw.InField(newSequences,self.updateSequences,textVariable=self.addedSeq,placeholder="type a sequence here to add it")
        addSequence.pack(fill=tk.X)        

        #start button
        start = cw.Button(self,"Start Game",self.startGame)
        start.pack(pady=(20,40))

    def updateSequences(self,*args):
        seqs = self.sequenceList.getElts()
        seqs.append(self.addedSeq.get())
        self.sequenceList.setElts(seqs)
        self.addedSeq.set("")

    def updateModeSelection(self,*args):
        """
        changes the mode selection frame when a different mode is picked
        """
        self.modeParameters.destroy()
        mode = self.chosenMode.get()
        if mode == "complete":
            self.modeParameters = CompleteParams(self.gamemode)
            self.modeParameters.pack(side=tk.LEFT,padx=15,pady=10,fill="both",expand=1)
        elif mode == "arcade":
            self.modeParameters = ArcadeParams(self.gamemode)
            self.modeParameters.pack(side=tk.LEFT,padx=15,pady=10,fill="both",expand=1)

    def startGame(self):
        mode=self.chosenMode.get()
        params=self.modeParameters.getParams()
        self.parent.startGame(mode,params)

class CompleteParams(tk.Frame):
    """
    parameters frame for a complete game
    """
    def __init__(self,parent):
        super().__init__(parent,bd=2,relief="groove")
        text = tk.Label(self,text="this gamemode does not \nhave parameters to set")
        text.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

    def getParams(self):
        return []

class ArcadeParams(tk.Frame):
    """
    parameters frame for an arcade game
    """
    def __init__(self,parent):
        super().__init__(parent,bd=2,relief="groove")
        text = tk.Label(self,text="this gamemode also does \nnot have parameters to set")
        text.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

    def getParams(self):
        return []
