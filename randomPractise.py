import cmd
from randomSequence import *
import prompts

class RandomShell(cmd.Cmd):

    def __init__(self):
        super().__init__()
        self.started = False
        self.rd = SequenceSet()
        self.prompt = '(scalia)'
        self.gameMode = "return"
        self.msgs = prompts.Prompter("prompts.txt")
        self.intro = self.msgs.get("Welcome") + self.msgs.get("Base")
    def do_help(self,arg):
        self.msgs.display("Help")

    def do_add(self,arg):
        if not(self.started):
            self.rd.addSequence(arg.split())

    def do_displaySequences(self,arg):
        self.msgs.display("DisplaySequences")
        for i in range(len(self.rd.sequences)):
            print(f"[{i+1}] "+ " ".join(self.rd.sequences[i]))
        print("\n")

    def do_remove(self,arg):
        self.rd.sequences.pop(int(arg)-1)

    def do_start(self,arg):
        self.msgs.display("GameStart")
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
                    self.msgs.display("GameEnd")
                    self.msgs.display("Base")
                    self.started=False
            else :
                print(" ".join(self.rd.pickReturn()))


    def do_end(self,arg):
        if self.started :
            self.msgs.display("GameEnd")
            self.msgs.display("Base")
            self.started = False

    def do_exit(self,arg):
        self.msgs.display("Quit")
        return True

if __name__ == "__main__" :
    RandomShell().cmdloop()
