import random
import collections

pos = (0,0)

direction = 0

locs = set()
first = []

def nextDir(direc):
    if direc == "R":
        return direction + 1 if direction < 3 else 0
    if direc == "L":
        return direction - 1 if direction > 0 else 3

def move(position, direction):
    if direction == 0:
        return (position[0], position[1] + 1)
    elif direction == 1:
        return (position[0] + 1, position[1])
    elif direction == 2:
        return (position[0], position[1] - 1)
    elif direction == 3:
        return (position[0] - 1, position[1])

with open("input1.txt") as f:
    line = f.read().strip("\n").split(",")
    for x in line:
        direction = nextDir(x[0])
        for x in range(int(x[1:])):
            pos = move(pos, direction)
            if pos in locs:
                first.append(pos)
            else:
                locs.add(pos)

print "part 1:", abs(pos[0]) + abs(pos[1])
print "part 2:", abs(first[0][0]) + abs(first[0][1])