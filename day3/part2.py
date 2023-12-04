BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
ORANGE = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def is_asterix(c):
    return c == '*'

def has_adjacent_asterix(lines, ln, cn):
    if ln > 0:
        if is_asterix(lines[ln-1][cn]): return (ln-1,cn)
        if cn > 0:
            if is_asterix(lines[ln-1][cn-1]): return (ln-1,cn-1)
        if cn < len(lines[ln])-2:
            if is_asterix(lines[ln-1][cn+1]): return (ln-1,cn+1)      
    if ln < len(lines)-1:
        if is_asterix(lines[ln+1][cn]): return (ln+1,cn)
        if cn > 0:
            if is_asterix(lines[ln+1][cn-1]): return (ln+1,cn-1)
        if cn < len(lines[ln])-2:
            if is_asterix(lines[ln+1][cn+1]): return (ln+1,cn+1)
    if cn > 0:
        if is_asterix(lines[ln][cn-1]): return (ln,cn-1)
    if cn < len(lines[ln])-2:
        if is_asterix(lines[ln][cn+1]): return (ln,cn+1)
    return (-1,1)
  
f = open("day3/input.txt")
lines=f.readlines()
matrix=[[1]* len(lines[0])] * len(lines)
matrix = [[1 for _ in range(len(lines[0]))] for _ in range(len(lines))]
sum = 0
for ln, l in enumerate(lines):
    print(f"{BLUE}\nl:{ln:03}  ", end="")
    v = 0
    is_part = False
    l = l.strip()
    for cn,c in enumerate(l):
        if c.isnumeric():
            v *= 10
            v+= int(c)   
            la, ca = has_adjacent_asterix(lines, ln, cn)
            if la != -1:
                is_part = True
                las = la
                cas = ca
        if not c.isnumeric() or cn == len(l)-1:
            if is_part: 
                if v != 0: 
                    print(GREEN + str(v), end="")
                    matrix[las][cas]*= -v
                    if matrix[las][cas] > 0: 
                        sum += matrix[las][cas]
                        sum = sum
            elif v != 0: print (RED + str(v), end="")
            if not c.isnumeric():
                print(ENDC + str(c), end="")
            v = 0
            is_part = False
print("\n")
print(sum)
    
    
    