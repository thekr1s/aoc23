import os
import math

def string_to_ints(str, separator):
    s = str.strip().split(separator)
    a = []
    for n in s:
        a.append(int(n.strip()))
    return a

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
locs = {}
loc=None
pos=[]
steps = []
for l in f.readlines():
    l = l.strip().split(" ")
    locs[l[0]] = [l[1], l[2]]
    if l[0][2]=="A":
        pos.append(l[0])
        steps.append(None)

dirs="LRLRRRLRLLRRLRLRRRLRLRRLRRLLRLRRLRRLRRRLRRRLRLRRRLRLRRLRRLLRLRLLLLLRLRLRRLLRRRLLLRLLLRRLLLLLRLLLRLRRLRRLRRRLRRRLRRLRRLRRRLRLRLRRLRLRLRLRRLRRRLLRLLRRLRLRRRLRLRRRLRLRRRLRRRLRRLRLLLLRLRRRLRLRRLRLRRLRRLRRLLRRRLLLLLLRLRRRLRRLLRRRLRRLLLRLRLRLRRRLRRLRLRRRLRRLRRRLLRRLRRLLLRRRR"
i=0
loc="AAA"
while loc != "ZZZ":
    dir = dirs[i % len(dirs)]
    for j, p in enumerate(pos):
        if dir=='L':
            pos[j]=locs[p][0]
        else:
            pos[j]=locs[p][1]
        # print(loc)
    i+=1
    for j, p in enumerate(pos):
        if p[2] == 'Z':
            if not steps[j]:
                steps[j] = i
                if not None in steps:
                    loc = "ZZZ"
                    break
            print(i, j, p)
print(steps, math.lcm(steps[0], steps[1], steps[2], steps[3], steps[4], steps[5]))

    
    
    