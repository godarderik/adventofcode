# coding: utf8

from collections import *

with open("input6.txt") as f:
    lines = [line.strip("\n") for line in f]
    out = [[line[k] for line in lines] for k in range(8)]
    
print "".join([Counter(x).most_common(1)[0][0] for x in out])
print "".join([Counter(x).most_common()[::-1][0][0] for x in out])
