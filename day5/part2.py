from dataclasses import dataclass
import os

@dataclass
class SeedsSet:
    first: int
    last: int
    
def string_to_ints(str, separator):
    s = str.strip().split(separator)
    a = []
    for n in s:
        a.append(int(n.strip()))
    return a

def do_map(value, map):
    return value + map[0] - map[1]

def map_seeds(sets: SeedsSet, map):
    mapped_sets = []
    i = 0
    while i < len(sets):
        set: SeedsSet = sets[i]
        for m in map:
            fst = max(set.first, m[1])
            lst = min(set.last, m[1]+m[2] - 1)
            if fst <= lst:
                mapped_sets.append(SeedsSet(do_map(fst, m), do_map(lst,m)))
                if fst != set.first:
                    sets.append(SeedsSet(set.first, m[1]-1))
                if lst != set.last:
                    sets.append(SeedsSet(m[1]+m[2], set.last))
                sets.remove(set)
                i-=1
                break
        i+=1
    for s in sets:
        mapped_sets.append(s)

    return mapped_sets

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
for l in f.readlines():
    lines.append(l.strip())

seeds = string_to_ints(lines[0].split(":")[1], " ")
seeds_org=seeds.copy()
seed_sets= []
for i in range(0, len(seeds), 2):
    seed_sets.append(SeedsSet(seeds[i], seeds[i] + seeds[i+1] - 1))
seeds=None    
map = []
for l in lines[2:]:
    if ":" in l: continue
    if l == "":
        print (f"MAP:\n{seed_sets}\n{map}")
        seed_sets = map_seeds(seed_sets, map)
        print (f"{seed_sets}")
        map = []
    else:
        map.append(string_to_ints(l, " "))


lowest = -1
for s in seed_sets:
        if lowest== -1 or s.first < lowest:
            lowest = s.first        

print(lowest)    