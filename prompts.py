def parse(promptList) :
    parsed = {}
    currentPromptName = ""
    currentPrompt = ""
    for line in promptList : 
        if not(line[0] in ["\n","\t"]):
            parsed[currentPromptName] = stripNewLine(currentPrompt)
            currentPrompt = ""
            currentPromptName = "".join(e for e in line if e.isalnum())
        else : 
            if line[0] == "\t":
                currentPrompt = currentPrompt + line[1:]
            else : currentPrompt = currentPrompt + line
    return parsed

def stripNewLine(msg):
    pre = False
    suf = False
    i = 0
    newMsg = msg
    while (not(pre) or not(suf)) and i<len(msg) :
        if msg[i] != "\n" and not(pre):
            newMsg = newMsg[i:]
            pre = True
        if msg[-(i+1)] != "\n" and not(suf):
            newMsg = newMsg[:-i]
            suf = True
        i+=1
    return newMsg

class Prompter:
    def __init__(self,filename):
        f = open(filename)
        L = f.readlines()
        f.close()
        self.prompts = parse(L)

    def get(self,key): 
        if self.prompts.__contains__(key):
            return self.prompts[key]
        else : 
            return ""

    def display(self,key) :
        if self.prompts.__contains__(key):
            print(self.prompts[key])

    def getPromptList(self):
        return list(self.prompts.keys())

1    
