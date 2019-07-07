def startGame(rd,args):
    parsedArgs = args.split(" ")
    if parsedArgs[0] in ["arcade",''] :
        startArcade(rd)
    elif parsedArgs[0] == "complete" :
        startComplete(rd)

def startArcade(rd) :
    end = False
    while not(end) :
        print(" ".join(rd.pickReturn()))
        cmd = input()
        if cmd == "end" :
            end = True

def startComplete(rd) :
    end = False
    while not(end) and len(rd.picks)>0 :
        print(" ".join(rd.pickNoReturn()))
        cmd = input()
        if cmd == "end" :
            end = True

