nums = [0] * 1000000000

tot = 29000000

for x in range(1,1000000):
    ind = 1
    for y in range(50):
        nums[x * ind] += 11 * x
        ind += 1
for k,v in enumerate(nums):
    #print v
    if v > tot:
        print k
        break
#print nums
