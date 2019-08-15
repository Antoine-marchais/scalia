import tkinter as tk 
from components import customWidgets as cw

class GameUI(tk.Frame):
    """
    game UI where the user is shown sequences according to its previous selection
    """
    def __init__(self,parent,w,h):
        """
        initialize the frame with a display for the randomized sequences and a next
        and exit button
        """
        super().__init__(parent.master,width=w,height=h)
        self.parent = parent
        self.mode = parent.gameMode
        self.params = parent.gameParams

        #setting the display as a white canvas
        self.display = tk.Canvas(self,bg="white")
        self.display.pack(fill="both",expand=1)

        #adding next an exit buttons
        buttons = tk.Frame(self)
        buttons.pack(fill="x")
        exitButton = cw.Button(buttons,"end game",self.endGame)
        exitButton.pack(side=tk.LEFT)
        nextButton = cw.Button(buttons,"next",self.nextSequence)
        nextButton.pack(side=tk.RIGHT)

        #initializing the game

    def nextSequence(self):
        """
        display the next sequence on the string
        """
        pass

    def endGame(self):
        self.parent.endGame()

    
        