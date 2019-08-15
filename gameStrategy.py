def startGame(randomizer,mode,args):
    if mode=="complete":
        return CompleteGame(randomizer)
    else:
        return ArcadeGame(randomizer)

class ArcadeGame :
    def __init__(self,rd):
        self.rd = rd
    def next(self):
        return self.rd.pickReturn()

class CompleteGame :
    def __init__(self,rd):
        self.rd = rd
    def next(self):
        if len(self.rd.picks)>0:
            return self.rd.pickNoReturn()
        else : 
            return None

