import itertools
import collections
import math
import copy
 
inpt = []
inpt1 = []
counts = collections.defaultdict(int)
corners = [(0,0), (0,99), (99,0), (99,99)]



def updateCell(coord):
    count = 0
    try:
        if inpt[coord[0] + 1][coord[1]] == "#" and coord[0] + 1 < len(inpt):
            count += 1
    except:
        pass
    try:
        if inpt[coord[0] - 1][coord[1]] == "#" and coord[0] - 1 >= 0:
            count += 1
    except:
        pass
    try:
        if inpt[coord[0]][coord[1] + 1] == "#" and coord[1] + 1 < len(inpt):
            count += 1
    except:
        pass
    try:
        if inpt[coord[0]][coord[1] - 1] == "#" and coord[1] - 1 >= 0:
            count += 1
    except:
        pass
    try:
        if inpt[coord[0] + 1][coord[1] + 1] == "#" and coord[1] + 1 < len(inpt) and coord[0] + 1 < len(inpt):
            count += 1
    except:
        pass
    try:
        if inpt[coord[0] + 1][coord[1] - 1] == "#" and coord[1] - 1 >= 0: 
            count += 1
    except:
        pass
    try:
        if inpt[coord[0] - 1][coord[1] + 1] == "#" and coord[0] - 1 >= 0:
            count += 1
    except:
        pass
    try:
        if inpt[coord[0] - 1][coord[1] - 1] == "#" and coord[1] - 1 >= 0 and coord[0] - 1 >= 0:
            count += 1
    except:
        pass
    if inpt[coord[0]][coord[1]] == "#" and not count in (2,3) and not coord in corners:
        inpt1[coord[0]][coord[1]] = "."
    elif inpt[coord[0]][coord[1]] == "." and count == 3:
        inpt1[coord[0]][coord[1]] = "#"




def updatePass():
    for k,v in enumerate(inpt):
        for a,b in enumerate(v):
            updateCell((a,k))


with open("input18.txt") as f:
    for line in f:
        inpt.append(list(line.strip("\n")))

inpt1 = copy.deepcopy(inpt)
for x in range(100):
    updatePass()
    inpt = copy.deepcopy(inpt1)
tot = 0
for y in inpt:
    for z in y:
        if z == "#":
            tot +=1
print inpt
print tot