import random

def combine(sequences,sequence):
    """
    a help function that returns a list of all the combinations of the
    list sequences with the list sequence
    """
    combined = []
    for eltA in sequences :
        for eltB in sequence :
            comb = eltA + [eltB]
            combined.append(comb)
    return combined

class SequenceSet :
    """
    a class that allows to create randomized set of sequences by 
    combining added sequences
    """
    def __init__(self):
        """
        basic initialisation that takes no argument
        """
        self.sequences = []
        self.picks = []

    def addSequence(self,seq):
        """
        adds a sequence (a list) to be randomized and computes
        all combinations that can be done with the current 
        sequences added
        """
        self.sequences.append(seq)
        self.computePicks()

    def computePicks(self):
        """
        compute all combinations that can be done with the current
        sequences added
        """
        self.picks = []
        for elt in self.sequences[0]:
             self.picks.append([elt])
        if len(self.sequences)>0:
            for i in range(1,len(self.sequences)):
                self.picks = combine(self.picks,self.sequences[i])

    def pickReturn(self):
        """
        picks a random combination without removing it from the possible
        picks
        """
        return random.choice(self.picks)

    def pickNoReturn(self):
        """
        pick a random combination and remove it from the possible picks
        """
        pick = random.choice(self.picks)
        self.picks.remove(pick)
        return pick

    def flush(self):
        """
        remove all sequences from the randomizer
        """
        self.sequences=[]
        self.picks=[]
