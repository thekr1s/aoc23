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

def map_seeds(seeds, map):
    for i in range(len(seeds)):
        s = seeds[i]
        for m in map:
            if s >= m[1] and s < (m[1] + m[2]):
                seeds[i] += m[0]-m[1]
                break;
                
    return seeds

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
for l in f.readlines():
    lines.append(l.strip())

seeds = string_to_ints(lines[0].split(":")[1], " ")
seeds_org=seeds.copy()
map = []
for l in lines[2:]:
    if ":" in l: continue
    if l == "":
        print (f"MAP:\n{seeds}\n{map}")
        seeds = map_seeds(seeds, map)
        print (f"{seeds}")
        map = []
    else:
        map.append(string_to_ints(l, " "))


seeds = map_seeds(seeds, map)
lowest = -1
for s in seeds:
    # if s in seeds_org:
        if lowest== -1 or s < lowest:
            lowest = s        

print(lowest)    