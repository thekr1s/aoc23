import os

FAIL

def calc(po, row, col):
    v= int(lines[row][col])
    p = paths[row][col]
    if v < p[1] or p[1] == 0:
        p[0] = po[0]
        p[0].append([row,col])
        p[1] = po[1]+v
        l = len(p[0])
        if p[0][l-1][0] == p[0][l-2][0] == p[0][l-3][0] == p[0][l-4][0]:
            return
        if p[0][l-1][1] == p[0][l-2][1] == p[0][l-3][1] == p[0][l-4][1]:
            return
            
        paths[row][col] = p
        
    

def calc_neigbours(row,col):
    if row < len(lines) and col < len(lines[0]):
        p = paths[row][col]
        if row < len(lines)-1:
            calc(p, row+1, col)
        if col < len(lines[0])-1:
            calc(p, row,col+1)

def printpaths():
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            print(f"{paths[r][c][1]:03} ", end="")
        print()

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
for l in f.readlines():
    lines.append(l.strip())

# paths = [ [[[],0]]*len(lines[0]) for i in range(len(lines))]    
paths=[]
for r in range(len(lines)):
    p = []
    for c in range(len(lines[0])):
        p.append([[],0])
    paths.append(p)
        
        

done=False
paths[0][0]=[[[0,0]],int(lines[0][0])]
for i in range(0, max(len(lines)*2, len(lines[0])*2)):
    print(i)
    for j in range(i+1):
        calc_neigbours(j, i - j)
    printpaths()  
print(paths[len(lines)-1][len(lines[0])-1])   
    

sum = 0
for l in lines:
    pass
print(sum)
    
    
    