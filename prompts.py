def parse(promptList) :
    parsed = {}
    currentPromptName = ""
    currentPrompt = ""
    for line in promptList : 
        if not(line[0] in ["\n","\t"]):
            parsed[currentPromptName] = currentPrompt
            currentPrompt = ""
            currentPromptName = "".join(e for e in line if e.isalnum())
        else : 
            if line[0] == "\t":
                currentPrompt = currentPrompt + line[1:]
            else : currentPrompt = currentPrompt + line
    parsed[currentPromptName] = currentPrompt
    return parsed

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

    