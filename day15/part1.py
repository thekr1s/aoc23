import os

def dohash(t):
    h = 0
    for c in t:
        h += ord(c)
        h*=17
        h&=0xff
    return h
        
print(dohash("HASH"))
dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
l=f.readline().strip()

sum=0
s = l.split(",") 
for p in s:
    sum += dohash(p) 
print(sum)
