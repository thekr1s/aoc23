import os

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
for l in f.readlines():
    l = l.strip().split(" ")
    locs[l[0]] = [l[1], l[2]]
    if not loc:
        loc=l[0]

dirs="LRLRRRLRLLRRLRLRRRLRLRRLRRLLRLRRLRRLRRRLRRRLRLRRRLRLRRLRRLLRLRLLLLLRLRLRRLLRRRLLLRLLLRRLLLLLRLLLRLRRLRRLRRRLRRRLRRLRRLRRRLRLRLRRLRLRLRLRRLRRRLLRLLRRLRLRRRLRLRRRLRLRRRLRRRLRRLRLLLLRLRRRLRLRRLRLRRLRRLRRLLRRRLLLLLLRLRRRLRRLLRRRLRRLLLRLRLRLRRRLRRLRLRRRLRRLRRRLLRRLRRLLLRRRR"
i=0
loc="AAA"
while loc != "ZZZ":
    dir = dirs[i % len(dirs)]
    if dir=='L':
        loc=locs[loc][0]
    else:
        loc=locs[loc][1]
    # print(loc)
    i+=1
    
print(i)
    
    
    