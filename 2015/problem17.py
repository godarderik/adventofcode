import itertools
import collections
 
inpt = []
counts = collections.defaultdict(int)

with open("input17.txt") as f:
    for line in f:
        inpt.append(int(line.strip("\n")))
for x in range(len(inpt)):
    for y in itertools.combinations(inpt, x):
        if sum(y) == 150:
            counts[x] += 1
print sum(counts.values()), counts[min(counts.keys())]
