import os

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
for l in f.readlines():
    l = l.strip().replace("#","").replace("(","").replace(")","")
    s = l.split(" ")
    lines.append(s)
    
p=[]
minx = 0
miny=0
pos=[0,0]
sum=0
peri = 0
for l in lines:
    minx=min(minx,pos[0])
    miny=min(miny,pos[1])
    dir=l[2][-1]
    dist=l[2][:-1]
    p.append(pos.copy())
    l[0]="RDLU"[int(dir)]
    l[1]=int(dist,16)
    if l[0] == "U":
        pos[1]+= int(l[1])
    if l[0] == "D":
        pos[1]-= int(l[1])
    if l[0] == "R":
        pos[0]+= int(l[1])
    if l[0] == "L":
        pos[0]-= int(l[1])
    peri += int(l[1])
    sum += p[-1][1] * pos[0]
    sum -= p[-1][0] * pos[1]
assert(pos==[0.,0])
print(sum/2, peri/2+1)
print(sum/2 + peri/2+1)

    