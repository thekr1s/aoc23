import os
import numpy as np

def string_to_ints(str, separator):
    s = str.strip().split(separator)
    a = []
    for n in s:
        a.append(int(n.strip()))
    return a

def rotate( m ):
    return np.rot90(m)   

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")

lines = []
for l in f.readlines():
    ll=[char for char in l.strip()]
    lines.append(ll)

lines=np.array(lines)

for cicle in range(1):
    if cicle%10000 == 0:
        print(cicle)
    for j in range(1):
        nrl=len(lines)        
        sum = 0    
        stop=[]
        for c in lines[0]:
            if c == "O":
                sum +=nrl
            if c == ".":
                stop.append(0) 
            else:
                stop.append(1)
                
        for r,l in enumerate(lines):
            if r == 0:
                continue
            for c,ch in enumerate(l):
                if ch == "O":
                    p = stop[c]
                    lines[p][c]="O"
                    if p!=r:
                        lines[r][c]="."
                    stop[c]+=1
                    sum += nrl-p
                if ch == "#":
                    stop[c]=r+1
            
        
        # lines = rotate(lines)
    
print ("cicle", cicle+1)    
for l in lines:
    for c in l:
        print(c, end="")
    print()
print(sum)
