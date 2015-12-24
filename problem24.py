import itertools
import operator

nums = []

with open('input24.txt') as f:
    for line in f:
        nums.append(int(line.strip("\n")))
tot = sum(nums)/5

def hasSum(lst, sub):
    quant = 1e99
    for y in range(1,len(lst)):
        for x in itertools.combinations(lst, y):
            if sum(x) == tot and sub == 2:
                return True
            elif sub != 2 and sum(x) == tot and hasSum(list(set(lst) - set(x)), sub - 1):
                quant = min(quant, reduce(operator.mul, x, 1))
        if quant < 1e99:
            return quant
print hasSum(nums, 5)
