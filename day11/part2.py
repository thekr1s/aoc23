import os

def string_to_ints(str, separator):
    s = str.strip().split(separator)
    a = []
    for n in s:
        a.append(int(n.strip()))
    return a

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
for l in f.readlines():
    lines.append(l.strip())

# Find empty colums
ec=[]
for c, _ in enumerate(lines[0]):
    found = False
    for l in lines:
        if l[c]=="#":
            found=True
            break
    if not found:
        print("col",c,"is empty")
        ec.append(c)

# find empty lines
el = []
for r, l in enumerate(lines):
    if l.find("#") == -1:
        el.append(r)
        print("empty line:", r)

gals=[]
for r, l in enumerate(lines):
    for c, g in enumerate(l):
        if g == '#':
            gals.append([r,c])
                 
f = 1000000
sum = 0
for i1, g1 in enumerate(gals):
    for g2 in gals[i1+1:]:
            
        d = abs(g1[0]-g2[0]) + abs(g1[1]-g2[1])
        s = min(g1[0], g2[0])
        e = max(g1[0], g2[0])
        for r in range(s, e+1):
            if r in el:
                d+= f-1
        s = min(g1[1], g2[1])
        e = max(g1[1], g2[1])
        for r in range(s, e+1):
            if r in ec:
                d+= f-1
        sum += d
print(sum)
    
    
    