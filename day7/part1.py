import os
CARDS="AKQJT98765432";

def string_to_ints(str, separator):
    s = str.strip().split(separator)
    a = []
    for n in s:
        a.append(int(n.strip()))
    return a

def get_hand_type(h):
    counts = []
    type=0
    for c in CARDS:
        counts.append(h.count(c))
    
    if counts.count(5) == 1:
        type=1
    elif counts.count(4) == 1:
        type=2
    elif counts.count(3) == 1 and counts.count(2) == 1:
        type=3
    elif counts.count(3) == 1:
        type=4
    elif counts.count(2) == 2:
        type=5
    elif counts.count(2) == 1:
        type=6
    else:
        type=7
        
    return type
                
        
def is_first_higher(h1, h2):
    t1 = get_hand_type(h1)
    t2 = get_hand_type(h2)
    if t1==t2:
        for i in range(len(h1)):
            if h1[i] != h2[i]:
                return CARDS.find(h1[i]) < CARDS.find(h2[i]) 
    else: return t1 < t2
    

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
hands = []
bids = []
for l in f.readlines():
    l = l.strip().split(" ")
    hands.append(l[0].strip())
    bids.append(int(l[1].strip()))
    
ranking=[]    
for n, h in enumerate(hands):   
    if  len(ranking) == 0:
        ranking.append(n)
        continue
    found=False
    for m, r in enumerate(ranking):
        if is_first_higher(hands[r], h):
            ranking.insert(m,n)
            found = True
            break
    if not found:
        ranking.append(n)
            
sum = 0 
for r,h in enumerate(ranking):
    v = bids[h] * (r+1)
    print(hands[h],bids[h], r+1 , v)
    sum += v
            
print(sum)  
    