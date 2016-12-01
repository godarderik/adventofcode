import random
import collections


pos = (0,0)

direction = 0


locs = {}
first = []

def nextDir(direc):
    global direction
    if direc == "R":
        direction += 1
        if direction == 4:
            direction = 0
    if direc == "L":
        direction -= 1
        if direction == -1:
            direction = 3
def move(position, delta, direction):
    if direction == 0:
        for x in range(delta):
            num = (position[0], position[1] + x)
            if not num in locs:
                locs[num] = 1
            else:
                first.append(num)
        return (position[0], position[1] + delta)
    elif direction == 1:
        for x in range(delta):
            num = (position[0] + x, position[1])
            if not num in locs:
                locs[num] = 1
            else:
                first.append(num)
        return (position[0] + delta, position[1])
    elif direction == 2:
        for x in range(delta):
            num = (position[0], position[1] - x)
            if not num in locs:
                locs[num] = 1
            else:
                first.append(num)
        return (position[0], position[1] - delta)
    elif direction == 3:
        for x in range(delta):
            num = (position[0] - x, position[1])
            if not num in locs:
                locs[num] = 1
            else:
                first.append(num)
        return (position[0] - delta, position[1])


with open("input1.txt") as f:
    line = f.read().strip("\n").split(",")
    for x in line:
        nextDir(x[0])
        pos = move(pos, int(x[1:]), direction)

print "part 1:", abs(pos[0]) + abs(pos[1])
print "part 2:", abs(first[0][0]) + abs(first[0][1])