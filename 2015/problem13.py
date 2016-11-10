import itertools

relations = {}
people = ["Me"]

with open("input13.txt") as f:
    for line in f:
        line = line.strip("\n")
        line = line.split(" ")
        if line[0] not in people:
            people.append(line[0])
            relations[line[0] + '-Me'] = 0
            relations['Me-' + line[0]] = 0
        amt = int(line[3])
        if line[2] == 'lose':
            amt *= -1
        relation = line[0] + "-" + line[-1].strip(".")
        relations[relation] = amt
optimal = -999999
for x in itertools.permutations(people):
    tot = 0

    for k,v in enumerate(x):
        if k == 0:
            tot += relations[v + '-' + x[-1]]
            tot += relations[v + '-' + x[1]]
        elif k == len(x) - 1:
            tot += relations[v + '-' + x[0]]
            tot += relations[v + '-' + x[-2]]
        else:
            tot += relations[v + '-' + x[k+1]]
            tot += relations[v + '-' + x[k-1] ]    
    optimal = max(tot,optimal)

print optimal