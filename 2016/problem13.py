from collections import *
from itertools import *

frontier = [(1,1,0)]
explored = {}
seen = {}

def get_wall(tup):
    if tup[0]< 0 or tup[1] < 0:
        return False
    num = tup[0] * tup[0] + 3 * tup[0] + 2 * tup[0] * tup[1] + tup[1] + tup[1] * tup[1]
    num += 1364
    return bin(num)[2:].count("1") % 2 == 0

def get_n(tup, cost):
    outArr = []
    cand =  [(tup[0], tup[1] + 1, cost + 1), (tup[0] - 1, tup[1], cost + 1),(tup[0] + 1, tup[1], cost + 1),(tup[0], tup[1] - 1, cost + 1)]
    for y in cand:
        if get_wall(y):
            outArr.append(y)
    return outArr

while len(frontier) > 0:
    new = frontier.pop()
    explored[(new[0], new[1])] = new[2]
    if new[2] <= 50:
        seen[(new[0], new[1])] = 1
    for x in get_n((new[0], new[1]), new[2]):
        if not (x[0], x[1]) in explored or explored[(x[0], x[1])] > x[2]:
            frontier.append(x)
print explored[(31,39)], len(seen) 