import random
import collections

pos = (0,0)

direction = 0

locs = set()
first = []

moves = [(0,1), (1,0), (0,-1), (-1,0)]

def nextDir(direc):
    return (direction + 1 if direction < 3 else 0) if direc == "R" else (direction - 1 if direction > 0 else 3)

def move(position, direction):
    return (position[0] + moves[direction][0], position[1] + moves[direction][1]) 

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