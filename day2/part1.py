
def check_can_do(s):
    a = {
    'red':  0,
    'green': 0,
    'blue': 0,
    }

    cs = s.lstrip().split(',')
    for c in cs:
        f = c.lstrip().split(' ')
        a[f[1]] += int(f[0])
            
    can_do=a['red'] <= 12 and a['green'] <= 13 and a['blue']<=14
    return can_do
                
f = open("day2/input.txt")
sum = 0
for l in f.readlines():
    l1 = l.strip().split(':')    
    sets = l1[1].split(';')
    can_do = True
    for s in sets:
        if not check_can_do(s):
            can_do = False
    if can_do:
        n = int(l1[0].split(' ')[1])
        sum += n
        print(n)
        
print(sum)
    
    
    