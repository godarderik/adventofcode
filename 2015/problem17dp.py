inpt = []

with open("input17.txt") as f:
    for line in f:
        inpt.append(int(line.strip("\n")))

res = []
for x in range(len(inpt)):
    res.append([0] * len(inpt))

def counts(cap, bottles):
    if cap == 0: 
        return 1 
        # this combination contains all the water
    if cap < 0 or len(bottles) == 0:
        return 0 
        # if negative or out of bottles it doesn't work
    first = bottles[0]
    rest = bottles[1:]
    return counts(cap-first,rest) + counts(cap, rest) 

cache_1 = {1:1, 0:1}
def p(n):
    if n < 0:
        return 0
    elif n in cache_1:
        return cache_1[n]
    else:
        num = 0
        for x in range(1,n+1):
            num1 = p(n - x * (3*x - 1)/2) 
            num2 = p(n - x * (3*x + 1)/2)
            add = (-1)**(x+1) * (num1 + num2)
            num += add
        cache_1[n] = num
        return num

cache_2 = {}
def p_2(n, k):
    if n == k:
        return 1
    elif k > n:
        return 0
    elif k == 0:
        return 0
    elif (n,k) in cache_2:
        return cache_2[(n,k)]
    else:
        cache_2 [(n,k)] = p_2(n-1, k-1) + p_2(n-k, k)
        return cache_2 [(n,k)]
    
print p(500) 
print p_2(500,100)
print p(63)
count = 0
for x in range(0,100):
    count += p(x)
print p(500) - count


