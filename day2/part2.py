
def get_power(sets):
    a = {
    'red':  0,
    'green': 0,
    'blue': 0,
    }

    for s in sets:
        cs = s.lstrip().split(',')
        for c in cs:
            f = c.lstrip().split(' ')
            color = f[1]
            count = int(f[0])
            if count > a[color]: a[color] = count            
    cres = a['red'] * a['green'] * a['blue']
    return cres
                
f = open("day2/input.txt")
sum = 0
for l in f.readlines():
    l1 = l.strip().split(':')    
    sets = l1[1].split(';')
    can_do = True
    sum += get_power(sets)
        
print(sum)
    
    
    