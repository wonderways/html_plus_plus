
header = """
const http = require('http');

const hostname = '127.0.0.1';
const port = 80;
"""

body=""""
const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html');
  res.end(htmlCode);
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
"""
specialChars = "+-.,;:][{}()&%$#!|<>=/~^"
combineSpecial = ["~=","^=","/==","*=","-=","+=","--","++","===","!==","!=","==","<=",">=","</","/>"]
combineSpecial.sort()
combineSpecial.sort(key = len)
combineSpecial= combineSpecial[::-1]
numberChars = "1234567890"
spaceChars = " \t\n\r"
stringChars = "\"'´"

notWords = specialChars + numberChars +spaceChars

class Part:
    def __init__(self,p):
        self.code = ""
        self.type = ""
        self.childs = []
        self.pos  = 0
        self.parent = p
def jumpTo(data,pos,char):
    for i in range(pos,len(data)):
        c = data[i]
        if c == char:
            return i
    return None


def getWord(data,pos):
    
    word = ""
    state = 0;
    for i in range(pos ,len(data)):
        c = data[i]
        if state == 0:
            if not (c in notWords):
                state = 1
                word += c
        elif state == 1:
            if (c in notWords):
               return word , i 
            else:
                word += c
    return word , None
def getText2Word(data,pos):
    word = ""
    for i in range(pos,len(data)):
        c = data[i]
        if not(c in data):
            return word , i
        else:
            word += c
    return word,None
def getSpecialChar(data,pos):
    word = ""
    state = 0;
    for i in range(pos ,len(data)):
        c = data[i]
        if state == 0:
            if c in specialChars:
                state = 1
                word += c
        elif state == 1:
            if not(c in specialChars):
               return word , i 
            else:
                word += c
    return word , None
def jumpSpaces(data,pos):
    for i in range(pos,len(data)):
        c = data[i]
        if not( c in spaceChars):
            return i
    return None
def findJSPart(parent , data,pos):
    part = Part(parent)
    cCount = 0
    passed =False
    entered = -1
    for i in range(pos,len(data)):
        c = data[i]
        if c == "{":
            cCount += 1
            if cCount == 1:
                entered = i
        elif c == "}":
            cCount -= 1
            if cCount == 0:
                part.code = data.substring(pos,i+1)
                part.pos = entered
    
                passed = True
    if entered == -1:
        return "empty"
    elif not passed:
        print("foun unclose curlibraces")
        return "missing"
    else:
        return part
def isTag(data,pos):
    for i in range(pos,len(data)):
        pass
def findHTMLPart(parent,data,pos):
    tag = ""
    state = 0
    for i in range( pos,len(data)):
        c = data[i]
        if state == 0:
            if c == "<":
                p = jumpSpaces(i+1)
                w,p = getWord(data,i)
                if p != None and w != "":
                    p = jumpSpaces(p)

def getParts(data,type):
    if type == "html":
        pass
    elif type == "js":
        pass

def process(data):
    
    return getParts(data,"html")

class Word:
    def __init__(self,_word,_type):
        self.word = _word
        self.type = _type
    def __str__(self):
        return "["+self.word + " - " + self.type+"]"

def segmentData(data):
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

def sepSpecialParts(data):
    i = len(data)-1
    while i >= 0:
        w = data[i]
        if w.type == "special":
            text = data[i].word
            parts = getSpecialParts(text)
            parts = list(map(lambda x:Word(x,"special"),parts))
            data = data[0:i] + parts + data[i+1:len(data)]
            i-=1

def getSpecialParts(data):
    print(data)
    indexes = []
    ops = []
    for i in combineSpecial:
        index = data.find(i)
        if index != -1:
            indexes.append([index,i])
    scanEnd = len(data)
    if len(indexes):
        scanEnd = indexes[0][0]
    state = 0
    count  = 0
    opCount = 0
    while True:
        print(count)
        if count == len(data):
            break
        if count == scanEnd:
            state = 1
        if state == 0:
            ops.append(data[count])
        else:
            ops.append(indexes[opCount][1])
            state = 0
            count = len(indexes[opCount][1])
            opCount += 1
            if opCount == len(indexes):
                scanEnd = len(data)
            else:
                scanEnd += indexes[opCount][0]
            
        pass
        count += 1
    return ops

file = open("text.jsx","r")
data= file.read()
file.close()

seg = segmentData(data)
# seg = sepSpecialParts(seg)

print("start")

for w in seg:
    print(w)
    pass
data = "htmlCode = " +"`"+ data+"`"

file = open("output.js","wb")
output = (header + body + data).encode("utf-8")
data= file.write(output)
file.close()
print("run")
