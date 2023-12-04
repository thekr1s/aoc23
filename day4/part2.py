import os 
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
ORANGE = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
for l in f.readlines():
    lines.append([l.strip(),1])
    
    
sum = 0
for i,g in enumerate(lines):
    l = g[0].split(':')
    sets = l[1].split('|')
    points = 0
    sum += g[1]
    
    count = 0
    for n in sets[0].strip().split(' '):
        set1 = []
        for x in sets[1].split(' '):
            try:
                set1.append(int(x.strip()))
            except:
                pass
        try:
            if int(n.strip()) in set1:
                count +=1
        except:
            pass
    for x in range(count):
        lines[i+1+x][1]+=g[1]
    sum += points
    points = 0
            
    pass
print(sum)
    
    
    