import cmd
from randomSequence import *
import prompts
import gameStrategy
from sequencePersistence import *

class RandomShell(cmd.Cmd):
    """
    Command line shell for the scalia App
    """
    def __init__(self):
        super().__init__()
        self.started = False
        self.saved = PersistSequence("./assets/savedSequences.json")
        self.rd = SequenceSet()
        self.prompt = '(scalia)'
        self.gameMode = "return"
        self.msgs = prompts.Prompter("./assets/prompts.txt")
        self.intro = self.msgs.get("Welcome") + "\n" + self.msgs.get("Base")

    def do_help(self,args):
        self.msgs.display("Help")

    def do_add(self,args):
        if args[0] == "$" :
            seq = self.saved.getSequence(args[1:])
            if seq == None :
                print("Unknown sequence")
            else :
                self.rd.addSequence(seq)
        else :
            self.rd.addSequence(args.split())

    def do_remove(self,args):
        self.rd.sequences.pop(int(args)-1)

    def do_current(self,args):
        self.msgs.display("DisplaySequences")
        for i in range(len(self.rd.sequences)):
            print(f"[{i+1}] "+ " ".join(self.rd.sequences[i]))

    def do_save(self,args):
        items = args.split()
        name = input("Sequence name : ")
        self.saved.saveSequence(name,items)

    def do_forget(self,args):
        self.saved.forgetSequence(args)

    def do_saved(self,args):
        self.msgs.display("SavedSequences")
        savedSequences = self.saved.getSequences()
        for seq in savedSequences :
            print(f"- [{seq['name']}] "+" ".join(seq["items"]))

    def do_start(self,args):
        self.msgs.display("GameStart")
        end = False
        if len(args)==0:
            game = gameStrategy.startGame(self.rd,"",[])
        else:
            game = gameStrategy.startGame(self.rd,args.split()[0],args.split()[1:])
        while not(end):
            seq = game.next()
            if seq != None : 
                print(" ".join(seq))
            else :
                print("no more combinations, type enter to quit")
                end = True
            command = input()
            if command == "end":
                end = True
        self.rd.flush()


    def do_exit(self,args):
        self.msgs.display("Quit")
        return True

if __name__ == "__main__" :
    RandomShell().cmdloop()
