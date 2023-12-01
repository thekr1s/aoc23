
def get_calibration_value(line: str):
    first = None
    last = None
    pos = 0
    for c in line:
        if c.isdigit():
            if first == None:
                first = int(c)
                firstpos = pos
            last = int(c)
            lastpos = pos
        pos += 1

    return first * 10 + last
                
f = open("day1/input.txt")
sum = 0
for l in f.readlines():
    sum += get_calibration_value(l)
    
print(sum)
    
    
    