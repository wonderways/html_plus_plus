def removeEqualIndexes(data):
    lastState ="none"
    words = []
    buffer = ""
    holder = ""
    i = 0
    while  i < len(data):

        c = data[i]
        state= ""
        if c in stringChars:
            newI = jumpTo(data,i+1,c)
            if newI == None:

                buffer = data[i:len(data)]
                break
            holder = data[i:newI+1]
            i = newI
            state = "string"
        elif c in numberChars:
            state = "number"
        elif c in specialChars:
            state = "special"
        elif c in spaceChars:
            
            state = "space"
        else:
            state = "word" 
        if state != lastState:
            if lastState == "":
                pass
            
            
            elif lastState == "string":
                pass
            else:
                w = Word(buffer,lastState)
                words.append(w)
                buffer = ""
            if state == "string":
                words.append(Word(holder,"string"))
                c = ""
                pass
            lastState = state

        buffer += c
        i+=1
        

    w = Word(buffer,lastState)
    words.append(w)
    return words
    index = -1
    holder = []
    toRemove = []
    ops = []
    for i in range(len(data))
        elem = data[i]
        if index == elem[0]
            holder.append(elem)
        else:
            if len(holder):
                maxLen = 0;
                e = null
                for a in range(holder):
                    if len(a[1].word) > maxLen:
                        maxLen = len(a[1].word)
                        e = a
                holder.remove(e)
                toRemove += holder
                holder = []
        index = elem[0]
    for i in toRemove:
        data.remove(i)

    lastIndex = 0
    for i in range(0,len(data)):
        elem = data[i]
        if elem[i] != lastIndex:
            ops.append


combineSpecial = ["!=","==","<=",">=","</","/>"]
combineSpecial.sort()
combineSpecial.sort(key = len)
combineSpecial= combineSpecial[::-1]