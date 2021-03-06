f = open("input14.txt")

times = {}
points = {}
state = {}
dist = {}


for line in f:
    line = line.strip("\n")
    line = line.split(" ")
    times[line[0]] = [int(line[3]), int(line[6]), int(line[-2])]
    points[line[0]] = 0
    dist[line[0]] = 0
    state[line[0]] = [True, int(line[6])]


def problemab():
    for x in range(2503):
        for k,v in times.iteritems():
            if state[k][0] == True and state[k][1] == 0:
                state[k][0] = False
                state[k][1] = v[2]
            elif state[k][0] == False and state[k][1] == 0:
                state[k][0] = True
                state[k][1] = v[1]
            if state[k][0] == True:
                dist[k] += v[0]
            state[k][1] -=1


        maxDist = 0
        maxP = []
        for j,p in dist.iteritems():
            if p > maxDist:
                maxDist = p
                maxP = [j]
            elif p == maxDist:
                maxDist = p
                maxP.append(j)
        for y in maxP:
            points[y] += 1
    print max(points.values()), max(dist.values())

problemab()



    