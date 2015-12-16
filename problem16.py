f = open("input16.txt")

g  = open("inpt.txt")

props = {}
for line in g:
    line = line.strip("\n")
    line = line.split(" ")
    props[line[0]] = int(line[1])

def check(types, value):
    value = int(value)
    if types == "cats:" or types == "trees:":
        return props[types] < value
    elif types == "pomeranians:" or types == "goldfish:":
        return props[types] > value
    return props[types] == value

for line in f:
    line = line.strip("\n")
    line = line.split(" ")
    if (check(line[2], line[3].strip(",")) and check(line[4], line[5].strip(",")) and check(line[6], line[7])):
        print line 