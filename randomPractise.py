import cmd
from randomSequence import *
import sequencePersistence
import prompters

class RandomShell(cmd.Cmd):
    intro = "Welcome to the randomizer \n  - add sequences with add \n  - start the game with start (complete)\n  - end the game with end"
    prompt = '(randomizer)'

    def __init__(self):
        super().__init__()
        self.started = False
        self.rd = SequenceSet()
        self.gameMode = "return"

    def do_add(self,arg):
        if not(self.started):
            self.rd.addSequence(arg.split())

    def do_start(self,arg):
        print("generated sequences\n press enter for next sequence")
        self.started = True
        if arg=="complete" :
            self.gameMode = "noReturn"
            print(" ".join(self.rd.pickNoReturn()))
        else :
            print(" ".join(self.rd.pickReturn()))

    def emptyline(self):
        if self.started :
            if self.gameMode == "noReturn":
                if len(self.rd.picks)>0:
                    print(" ".join(self.rd.pickNoReturn()))
                else :
                    print("game ended \n  - add sequences with add \n  - start the game with start (complete)\n  - end the game with end")
                    self.started=False
            else :
                print(" ".join(self.rd.pickReturn()))


    def do_end(self,arg):
        if self.started :
            print("game ended")
            print("- add sequences with add \n  - start the game with start (complete)\n  - end the game with end")
            self.started = False

    def do_exit(self,arg):
        print("goodBye")
        return True

if __name__ == "__main__" :
    RandomShell().cmdloop()
