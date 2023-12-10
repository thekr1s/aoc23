import os
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
ORANGE = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def string_to_ints(str, separator):
    s = str.strip().split(separator)
    a = []
    for n in s:
        a.append(int(n.strip()))
    return a

    
def get_connected(p):
    dirs="WNES"
    c=[]
    ct=lines[p[1]][p[0]]
    # print(ct, end=":")
    for dir in dirs:
        t="."
        if dir == "W" and p[0]>0:
            if ct=="J" or ct == "-" or ct == "7" or ct == "S":
                np=[p[0]-1, p[1]]
                t=lines[np[1]][np[0]]
                if t == "F" or t == "L" or t == "-" or t=="S":
                    c.append(np)
                    print(end=RED)
        if dir == "N" and p[1]>0:
            if ct=="J" or ct == "|" or ct == "L" or ct == "S":
                np=[p[0], p[1]-1]
                t=lines[np[1]][np[0]]
                if t == "F" or t == "|" or t == "7" or t=="S":
                    c.append(np)
                    print(end=RED)
        if dir == "E" and p[0]<len(lines[0])-1:
            if ct=="F" or ct == "-" or ct == "L" or ct == "S":
                np=[p[0]+1, p[1]]
                t=lines[np[1]][np[0]]
                if t == "J" or t == "-" or t == "7" or t=="S":
                    c.append(np)
                    print(end=RED)
        if dir == "S" and p[1]<len(lines)-1:
            if ct=="F" or ct == "|" or ct == "7" or ct == "S":
                np=[p[0], p[1]+1]
                t=lines[np[1]][np[0]]
                if t == "J" or t == "|" or t == "L" or t=="S":
                    c.append(np)
                    print(end=RED)
        # print(t, end="")
        print(ENDC, end="")
        
        
    # print()
    
    assert(len(c) == 2)

    return c
                 
    
dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
for i,l in enumerate( f.readlines()):
    lines.append(l.strip())
    s = l.find("S")
    if s != -1:
        p = [s,i]        
    
path=[p]
i = 0
while True:
    np = None
    # print(i, path[i], end=" ")
    c = get_connected(path[i])
    if i > 0 and c[0] != path[i-1]:
        np=c[0]
    else:
        np=c[1]
    i+=1
    path.append(np) 
    t = lines[np[1]][np[0]]
    if  t == "S":
        break;
    

for y,l in enumerate(lines):
    for x,c in enumerate(l):
        if [x,y] in path:
            print(RED+BOLD, end="")
            print(c, end="")
            print(ENDC, end="")
        else:
            print(c, end="")
            
    print()    
sum = 0


print(i, int(i/2))
    
    
    