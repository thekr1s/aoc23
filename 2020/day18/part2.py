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

def calc(a, op, b):
    if op == "+":
        return a + b
    if op == "*":
        return a * b
    assert(False)
    
def find_matching(s):
    assert(s[0] == "(")
    p = 1
    h=1
    while h != 0:
        if s[p] == "(":
            h+=1
        if s[p] == ")":
            h-=1
        p+=1
    return s[1:p-1], s[p:]

def evaluate(l):
    s=0
    op = "+"
    while len(l) > 0:
        c = l[0]
        if c.isdigit():
            s = calc(s,op,int(c))
        if c == "+":
            op=c                
        if c == "*":
            s = calc(s,c,evaluate(l[1:]))  
            l=""  
        elif c == "(":
            intern, l = find_matching(l)
            s = calc(s, op, evaluate(intern))
        else:
            l = l[1:]

    return s

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
for l in f.readlines():
    lines.append(l.strip().replace(" ", ""))
    
    
sum = 0
for l in lines:
    s = evaluate(l)
    print(l,s)
    sum += s
    
    pass
print(sum)
    
    
    