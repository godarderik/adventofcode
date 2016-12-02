code = []

with open("input2.txt") as f:
    for line in f:
        line = line.strip("\n")
        code.append([line])

def move(pos, direc):
    oldPos = pos
    if direc == "U":
        pos = (pos[0], pos[1] - 1)
    elif direc == "R":
        pos = (pos[0] + 1, pos[1])
    elif direc == "L":
        pos = (pos[0] - 1, pos[1])
    elif direc == "D":
        pos = (pos[0], pos[1] + 1)

    if abs(pos[0]) + abs(pos[1]) > 2:
        return oldPos
    return pos

pos = (-2,0)

for x in code:
    for k in x[0]:
        pos = move(pos, k)
    print pos
