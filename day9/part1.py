import os

def string_to_ints(str, separator):
    s = str.strip().split(separator)
    a = []
    for n in s:
        a.append(int(n.strip()))
    return a

def find_val(hist):
    all_zero=True
    new=[]
    for i in range(len(hist)-1):
        d = hist[i+1] - hist[i]
        new.append(d)
        if (d) != 0:
            all_zero = False  

    if all_zero:
        return hist[-1]
    else:
        v = find_val(new)
        return hist[-1] + v

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
sum=0
for l in f.readlines():
    l = l.strip()
    hist=string_to_ints(l, " ")
    val = find_val(hist)
    print(val)
    sum += val
print(sum)
    
    
    