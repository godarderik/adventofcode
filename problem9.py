import itertools

def problema():
    f = open("input9.txt")
    edges = []
    cities = []
    for line in f:
        line = line.strip("\n")
        line = line.split(" ")
        tup = (line[0], line[2], int(line[4])) #make these negative for part 2
        cities.append(line[0])
        tup1 = (line[2], line[0], int(line[4])) #make these negative for part 2
        cities.append(line[2])
        edges.append(tup)
        edges.append(tup1)
    cities = list(set(cities))
    minCost = 999999999
    route = []
    count = 0
    for path in itertools.permutations(cities):
        cost = 0
        for k,v in enumerate(path[:-1]):
            found = False
            for x in edges:
                if x[0] == v and x[1] == path[k+1]:
                    cost += x[2]
                    found = True
            if not found:
                cost = 99999999
                break
        if cost < minCost:
            minCost = cost
            route = path
        
        if found:
            count += 1
    return minCost

print problema()