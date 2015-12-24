import itertools
import operator

nums = []

with open('input24.txt') as f:
    for line in f:
        nums.append(int(line.strip("\n")))
tot = sum(nums)/4

def hasSum(lst, sub):
    quant = 1e9
    for y in range(1,len(lst)):
        for x in itertools.combinations(lst, y):
            if sum(x) == tot and sub:
                return True
            elif not sub and sum(x) == tot and hasSum(list(set(nums) - set(x)), True):
                quant = min(quant, reduce(operator.mul, x, 1))
        if quant < 1e9:
            return quant
print hasSum(nums, False)
