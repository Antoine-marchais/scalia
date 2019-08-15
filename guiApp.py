import tkinter as tk
from randomSequence import *
import prompts
import game
from sequencePersistence import *
from components.welcomeUI import WelcomeUI
from components.selectionUI import SelectionUI
from components.gameUI import GameUI

class ScaliaGUI :
    """
    graphical interface for the scalia App
    """
    def __init__(self,master):
        """
        showing title screen before going to the selection menu
        """
        master.title("Scalia")
        self.master = master
        self.rd = SequenceSet()
        self.currentUI = WelcomeUI(self,900,700)
        self.currentUI.pack()
        self.currentUI.pack_propagate(0)
        self.master.after(3000,self.showUI,SelectionUI)

    def showUI(self,UI):
        """
        destroy the last UI before showing the next one
        """
        self.currentUI.destroy()
        self.currentUI = UI(self,900,700)
        self.currentUI.pack()
        self.currentUI.pack_propagate(0)

    def updateSequences(self,sequences):
        self.rd.flush()
        print(sequences)
        for seq in sequences:
            self.rd.addSequence(seq.split())
        print(self.rd.picks)

    def startGame(self,mode,*params):
        self.gameMode=mode
        self.gameParams=params
        self.showUI(GameUI)

    def endGame(self):
        self.rd.flush()
        self.showUI(SelectionUI)

    def getMaster(self):
        return self.master

if __name__ == "__main__" :
    root = tk.Tk()
    scaliaGUI = ScaliaGUI(root)
    root.mainloop()