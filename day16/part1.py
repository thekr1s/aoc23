import os
import sys
sys.setrecursionlimit(15000)

def get_next_pos(rp):
    if rp[2] == "R":
        rp[1]+=1
    if rp[2] == "D":
        rp[0]+=1
    if rp[2] == "L":
        rp[1]-=1
    if rp[2] == "U":
        rp[0]-=1
    return rp.copy()

def trace(rp):
    if rp[0]<0 or rp[1]<0 or rp[0]>= len(lines) or rp[1]>=len(lines[0]):
        return
    if rp[2] in energized[rp[0]] [rp[1]]:
        return 
    energized[rp[0]] [rp[1]].append(rp[2])
    c = lines[rp[0]] [rp[1]]
    if c == ".":
        trace(get_next_pos(rp.copy()))
    elif c == "|" and (rp[2]=="U" or rp[2]=="D"):
        trace(get_next_pos(rp.copy()))
    elif c == "|":
        trace(get_next_pos([rp[0],rp[1],"U"]))
        trace(get_next_pos([rp[0],rp[1],"D"]))
    elif c == "-" and (rp[2]=="L" or rp[2]=="R"):
        trace(get_next_pos(rp.copy()))
    elif c == "-":
        trace(get_next_pos([rp[0],rp[1],"L"]))
        trace(get_next_pos([rp[0],rp[1],"R"]))
    elif c == "/":
        if rp[2] == "R" :
           trace(get_next_pos([rp[0],rp[1],"U"]))
        if rp[2] == "D" :
           trace(get_next_pos([rp[0],rp[1],"L"]))
        if rp[2] == "L" :
           trace(get_next_pos([rp[0],rp[1],"D"]))
        if rp[2] == "U" :
           trace(get_next_pos([rp[0],rp[1],"R"]))
    elif c == "\\":
        if rp[2] == "R" :
           trace(get_next_pos([rp[0],rp[1],"D"]))
        if rp[2] == "D" :
           trace(get_next_pos([rp[0],rp[1],"R"]))
        if rp[2] == "L" :
           trace(get_next_pos([rp[0],rp[1],"U"]))
        if rp[2] == "U" :
           trace(get_next_pos([rp[0],rp[1],"L"]))
    else:
        assert(False)
        
dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
energized = []
for l in f.readlines():
    a=[]
    e=[]
    for c in l.strip():
        a.append(c)
        e.append([])
    lines.append(a)
    energized.append(e)
    

rp=[0,0,"R"]    
trace(rp)
count=0
for l in energized:
    for c in l:
        print(len(c),end="")
        if len(c) > 0:
            count+=1
    print()
print (count)