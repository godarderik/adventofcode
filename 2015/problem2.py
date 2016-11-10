arr = []
f = open("input2.txt")
for line in f:
    line = line.split("x")
    arr.append((int(line[0]), int(line[1]), int(line[2])))

def problema():
    tot = 0
    for x in arr:
        tot += 2 * x[0]*x[1] + 2*x[1]*x[2] + 2*x[2]*x[0]
        lst = sorted(list(x))
        tot += lst[0] * lst[1]
    return tot
def problemb():
    tot = 0
    for x in arr:
        lst = sorted(list(x))
        tot += 2 * lst[0] + 2*lst[1] + lst[0] * lst[1] * lst[2]
    return tot
    
print problema(), problemb()
    