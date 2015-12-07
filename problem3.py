def move(coord, char):
    if char == "<":
        coord = (coord[0] - 1, coord[1])
    elif char == ">":
        coord = (coord[0] + 1, coord[1])
    elif char == "v":
        coord = (coord[0], coord[1] - 1)
    elif char == "^":
        coord = (coord[0], coord[1] + 1)
    return coord

def problema():
    f = open("input3.txt")
    l = f.read()
    locs = {}

    coord1 = (0,0)
    coord2 = (0,0)

    locs[coord1] = 1

    count = 0
    for char in l:
        if count % 2 == 0:
            coord1 = move(coord1, char)
            locs[coord1] = 1
        else:
            coord2 = move(coord2, char)
            locs[coord2] = 1
        count += 1
        

    print len(locs)
        
problema()