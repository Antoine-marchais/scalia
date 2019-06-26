import random

def combine(sequences,sequence):
    combined = []
    for eltA in sequences :
        for eltB in sequence :
            comb = eltA + [eltB]
            combined.append(comb)
    return combined

class SequenceSet :
    def __init__(self):
       self.sequences = []
       self.picks = []

    def addSequence(self,seq):
        self.sequences.append(seq)
        self.computePicks()

    def computePicks(self):
        self.picks = []
        for elt in self.sequences[0]:
             self.picks.append([elt])
        if len(self.sequences)>0:
            for i in range(1,len(self.sequences)):
                self.picks = combine(self.picks,self.sequences[i])

    def pickReturn(self):
        return random.choice(self.picks)

    def pickNoReturn(self):
        pick = random.choice(self.picks)
        self.picks.remove(pick)
        return pick
