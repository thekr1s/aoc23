import os
import numpy
def string_to_ints(str, separator):
    s = str.strip().split(separator)
    a = []
    for n in s:
        a.append(int(n.strip()))
    return a

l="6 4 3 7 1 9 2 5 8"
nrs=string_to_ints(l," ")

for r in range(100):
    if r%100 == 0:
        print(r)
    s = nrs[1:4]
    nrs = nrs[0:1] + nrs[4:]
    n=nrs[0]
    i = -1
    while i == -1:
        n -= 1 
        if n == 0:
            n = 9
        if n in nrs:       
            i = nrs.index(n)
        else:
            i = -1
    nrs=nrs[1:i+1] + s + nrs[i+1:] + nrs[0:1]
    
i = nrs.index(1)
nrs=nrs[i+1:] + nrs[0:i]

for n in nrs:
    print(n, end="")
print()