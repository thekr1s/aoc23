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

def line_to_bin(l:str):
    l=l.replace("#","1")
    l=l.replace(".","0")
    return int(l,2)

def is_mirror(a, l,r, fixed):
    d=a[l]^a[r]
    b=bin(d).count('1') == 1
    if a[l]==a[r] or (b and not fixed):
        if b:
            print(l, bin(a[l]), r, bin(a[r]), a[l], a[r], d, bin(d))
            fixed=True
        if l > 0 and r < len(a)-1:
            return is_mirror(a,l-1, r+1, fixed)
        else:
            return fixed
    return False

def find_mirror(lines):
    lb =[]
    cb=[]
    sum=0
    for l in lines:
        lb.append(line_to_bin(l))
        
    for i in range(len(lines[0])):
        s = ""
        for l in lines:
            s+=l[i]  
        cb.append(line_to_bin(s))

    for i in range(len(lines)-1):
        # print(i)
        if is_mirror(lb, i, i+1, False):
            n = i+1
            print(" l", n*100)
            sum += n * 100
            # break
    for i in range(len(lines[0])-1):
        # print(i)
        if is_mirror(cb, i, i+1, False):
            n = i+1
            print(" c", n)
            sum += n
            # break
    return sum

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
sum = 0
for l in f.readlines():
    l=l.strip()
    if l=="":
        n=find_mirror(lines)  
        sum += n   
        print(n)
        lines=[]
    else:
        lines.append(l.strip())
    print(l)
    

        
print(sum)
    
    
    