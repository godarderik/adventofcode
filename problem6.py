def problemb():
    f = open("input6.txt")

    grid = []

    for x in range(1000):
        newLine = [False] * 1000
        grid.append(newLine)

    for line in f:
        line = line.split(" ")

        if line[0] == "toggle":
            coord1 = line[1].strip("\n").split(",")
            coord2 = line[3].strip("\n").split(",")

            width = int(coord2[0]) - int(coord1[0])
            height = int(coord2[1]) - int(coord1[1])
            
            for x in range(height+1):
                for y in range(width+1):
                    grid[int(coord1[0]) + y][int(coord1[1]) + x] += 2

        elif line[1] == "on":
            coord1 = line[2].strip("\n").split(",")
            coord2 = line[4].strip("\n").split(",")
            width = int(coord2[0]) - int(coord1[0])
            height = int(coord2[1]) - int(coord1[1])
            for x in range(height+1):
                for y in range(width+1):
                    grid[int(coord1[0]) + y][int(coord1[1]) + x] += 1
            
        elif line[1] == "off":
            coord1 = line[2].strip("\n").split(",")
            coord2 = line[4].strip("\n").split(",")
            width = int(coord2[0]) - int(coord1[0])
            height = int(coord2[1]) - int(coord1[1])
            for x in range(height+1):
                for y in range(width+1):
                    grid[int(coord1[0]) + y][int(coord1[1]) + x] -= 1
                    grid[int(coord1[0]) + y][int(coord1[1]) + x] = max(grid[int(coord1[0]) + y][int(coord1[1]) + x] , 0)
    count = 0
    for x in grid:
        for y in x:
            count += y
    print count

def problema():
    f = open("input6.txt")

    grid = []

    for x in range(1000):
        newLine = [False] * 1000
        grid.append(newLine)

    for line in f:
        line = line.split(" ")

        if line[0] == "toggle":
            coord1 = line[1].strip("\n").split(",")
            coord2 = line[3].strip("\n").split(",")

            width = int(coord2[0]) - int(coord1[0])
            height = int(coord2[1]) - int(coord1[1])
            
            for x in range(height+1):
                for y in range(width+1):
                    grid[int(coord1[0]) + y][int(coord1[1]) + x] = not grid[int(coord1[0]) + y][int(coord1[1]) + x]

        elif line[1] == "on":
            coord1 = line[2].strip("\n").split(",")
            coord2 = line[4].strip("\n").split(",")
            width = int(coord2[0]) - int(coord1[0])
            height = int(coord2[1]) - int(coord1[1])
            for x in range(height+1):
                for y in range(width+1):
                    grid[int(coord1[0]) + y][int(coord1[1]) + x] = True
            
        elif line[1] == "off":
            coord1 = line[2].strip("\n").split(",")
            coord2 = line[4].strip("\n").split(",")
            width = int(coord2[0]) - int(coord1[0])
            height = int(coord2[1]) - int(coord1[1])
            for x in range(height+1):
                for y in range(width+1):
                    grid[int(coord1[0]) + y][int(coord1[1]) + x] = False

 
    count = 0
    for x in grid:
        for y in x:
            count += y
    print count