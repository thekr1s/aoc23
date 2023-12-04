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
    lines.append(l.strip())
    
    
sum = 0
for i,l in enumerate(lines):
    l = l.split(':')
    sets = l[1].split('|')
    points = 0
    for n in sets[0].strip().split(' '):
        set1 = []
        for x in sets[1].split(' '):
            try:
                set1.append(int(x.strip()))
            except:
                pass
        try:
            if int(n.strip()) in set1:
                if points == 0:
                    points = 1
                else: 
                    points *= 2
        except:
            pass
    sum += points
    points = 0
            
    pass
print(sum)
    
    
    