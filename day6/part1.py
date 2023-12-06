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
        if n != '':
            a.append(int(n.strip()))
    return a

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
for l in f.readlines():
    lines.append(l.strip())

race_time = string_to_ints(lines[0].split(':')[1], " ")    
dist = string_to_ints(lines[1].split(':')[1], " ")    

sum = 1
for i in range(len(race_time)):
    count = 0
    for t in range(race_time[i]):
        if t % 1000000==0:
            print(t)
        d = (race_time[i] - t) * t
        if d > dist[i]:
            count +=1
    print(count)
    sum *= count    
            

print(sum)
    
    
    