BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
ORANGE = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def is_symbol(c):
    return c != '.' and not c.isdigit()

def has_adjacent_symbol(lines, ln, cn):
    if ln > 0:
        if is_symbol(lines[ln-1][cn]): return True
        if cn > 0:
            if is_symbol(lines[ln-1][cn-1]): return True
        if cn < len(lines[ln])-2:
            if is_symbol(lines[ln-1][cn+1]): return True      
    if ln < len(lines)-1:
        if is_symbol(lines[ln+1][cn]): return True
        if cn > 0:
            if is_symbol(lines[ln+1][cn-1]): return True
        if cn < len(lines[ln])-2:
            if is_symbol(lines[ln+1][cn+1]): return True
    if cn > 0:
        if is_symbol(lines[ln][cn-1]): return True
    if cn < len(lines[ln])-2:
        if is_symbol(lines[ln][cn+1]): return True
    return False
  
f = open("day3/input.txt")
lines=f.readlines()
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
            is_part |= has_adjacent_symbol(lines, ln, cn)
        if not c.isnumeric() or cn == len(l)-1:
            if is_part: 
                if v != 0: print(GREEN + str(v), end="")
                sum += v
            elif v != 0: print (RED + str(v), end="")
            if not c.isnumeric():
                print(ENDC + str(c), end="")
            v = 0
            is_part = False
print("\n")
print(sum)
    
    
    