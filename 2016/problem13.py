frontier = [(1,1,0)]
explored = {}

def get_wall(tup):
    num = tup[0] * tup[0] + 3 * tup[0] + 2 * tup[0] * tup[1] + tup[1] + tup[1] * tup[1] + 1364
    return bin(num)[2:].count("1") % 2 == 0 and tup[0] >= 0 and tup[1] >= 0

def get_next(tup):
    cand = [(0,1), (0,-1), (1,0), (-1,0)]
    return [(x[0] + tup[0], x[1] + tup[1], tup[2] + 1) for x in cand if get_wall((x[0] + tup[0], x[1] + tup[1]))]

while len(frontier) > 0:
    new = frontier.pop()
    explored[(new[0], new[1])] = new[2]
    frontier += [x for x in get_next(new) if not (x[0], x[1]) in explored or explored[(x[0], x[1])] > x[2]]

print explored[(31,39)], len([explored[x] for x in explored.keys() if explored[x] <= 50])