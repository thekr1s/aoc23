numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

def get_calibration_value(line: str):
    first = None
    firstpos = 0xffffffffffff
    last = None
    lastpos = -1
    pos = 0
    for c in line:
        if c.isdigit():
            if first == None:
                first = int(c)
                firstpos = pos
            last = int(c)
            lastpos = pos
        pos += 1
        
    for i,n in enumerate(numbers):
        p = line.find(n)
        if p != -1:
            if p < firstpos:
                first = i + 1
                firstpos = p
            p = line.rfind(n)
            if p > lastpos:
                last = i + 1
                lastpos=p
               
    print(first * 10 + last)
    return first * 10 + last
                
f = open("day1/input.txt")
sum = 0
for l in f.readlines():
    sum += get_calibration_value(l)
    
print(sum)
    
    
    