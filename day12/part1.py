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
cnt=0
def get_options(s, n, l):
    print(l*" ", s,n)
    so,no = s,n
    h=0
    global cnt
    for i,c in enumerate(s):
        if c == "#" or (c == "?" and h>0):
            if h == 0:
                st=c
            h +=1
        elif c == "?":
            print(l*" ","? as .")
            get_options(s[i+1:], n, l+1) # treat a dot
            assert(h==0)
            h+=1 # treat as #
            st=c
        elif h>0:
            assert(c==".")
            return 0
        else:
            assert(c==".")
            print(l*" ","next is .")
            get_options(s[i+1:], n, l+1) # treat a dot
            return

        if h == n[0]:
            if len(n) == 1: # found last set
                if i == len(s)-1 or not "#" in s[i+1:]:
                    cnt +=1
                    print(l*" ", "found", cnt)
                    return  # Last set in line
                else:
                    return # This is not an option
            if i == len(s)-1:
                return
            elif s[i+1] == "#":
                return
            else: # next is . or ?
                print(l*" ","next ? or .")
                get_options(s[i+2:], n[1:], l+1)
                return 
            
            
            
    return 0
                    
        

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
ns=[]
ss=[]
for l in f.readlines():
    s = l.strip().split(" ")
    ns.append(string_to_ints(s[1],","))
    t = s[0].replace("..", ".")
    while t != s[0]:
        s[0] = t
        t = s[0].replace("..", ".")
    ss.append(t)
    
sum = 0
for i,s in enumerate(ss):
    cnt = 0
    get_options(s, ns[i],0)
    print(s,ns[i], cnt)
    sum += cnt
    
print(sum)
    
    
    