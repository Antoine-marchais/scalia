import json

class PersistSequence :

    def __init__(self,path) :
        self.path = path
        with open(path,"r") as f:
            self.sequences = json.load(f)

    def getSequences(self) :
        return self.sequences["sequences"]

    def getSequence(self,name) :
        for seq in self.sequences["sequences"] :
            if seq["name"]==name :
                return seq["items"]
                break

    def saveSequence(self,name,items) :
        seq = {}
        seq["name"] = name
        seq["items"] = items
        self.sequences["sequences"].append(seq)
        self.syncSequences()

    def forgetSequence(self,name) :
        self.sequences["sequences"] = [seq for seq in self.sequences["sequences"] if seq["name"] != name]
        self.syncSequences()

    def syncSequences(self) :
        with open(self.path,"w") as f :
            json.dump(self.sequences,f)
