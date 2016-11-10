import math
import itertools
import operator

inpt = []
inptd = {}

first = 20151125
mult = 252533
mod = 33554393

col = 3010
row = 3019

def findn(n):
    start = first
    for x in range(n):
        start = (start * mult) % mod
    return start

def coord(x,y):
    s = 1
    a = 2
    for t in range(x-1):
        s += a
        a += 1
    o = x
    for z in range(y-1):
        s += o
        o += 1
    return s
print findn(coord(3019,3010) - 1)



