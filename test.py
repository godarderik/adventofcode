import random
import collections

def count0(lst):
    count = 0
    for x in lst:
        if x > 0:
            count += 1
    return count
def findnum(lst):
    for x,y in enumerate(lst):
        if x > 0:
            x + 1

def a():
    counts = []
    for y in range(1,10):
        count2 = 0
        for x in range(100000):
            count = 0
            nums = range(1,y)
            while len(nums) > 1:

                ind = random.randrange(len(nums))
                nums[ind] -= 1
                if nums[ind] == 0:
                    if ind == 0 and count == 0:
                        count += 1
                    del nums[ind]
            #count += nums[0]
            count2 += count
        counts.append(1 - count2/100000.0)
        #print counts
    for k,v in enumerate(counts):
        print k,v
done = collections.defaultdict(int)
def b():
    orders = {}
    
    for x in range(100000):
        nums = range(1,4)
        track = [[], 1]
        old = count0(nums)
        while old > 0:
            ind = random.randrange(len(nums))
            if nums[ind] > 0:
                nums[ind] -= 1
                track[0].append(ind)
                track[1] *= 1.0/old
            old = count0(nums)
        if count0(nums) == 0:
            orders[tuple(track[0])] = track[1]
            done[findnum(nums)] += 1

    return orders
#a = b()
#tot = sum(a.values())
y = 0
out = 0

def calc(n):
    tot = 0
    for k in range(1,n+1):
        for j in range(1,k+1):
            if j == k:
                tot += j * (1.0/(n))**j
            else:
                tot += j * (1.0/(n))**j * ((n-1.0)/n)
            
    return tot

'''hasht = collections.defaultdict(int)
for k,v in a.iteritems():
    itera = -1
    lt = 0
    while k[itera] == k[-1]:
        lt += 1
        itera -= 1
    hasht[str(k[-1])*lt] += v
    out += lt * v'''
print a()


#print out, hasht, tot, len(a), sum(hasht.values())
#print calc(2)

