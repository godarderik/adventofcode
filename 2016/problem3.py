count = 0

def check(line):
    return line[0] + line[1] > line[2] and line[0] + line[2] > line[1] and line[1] + line[2] > line[0]

with open("input3.txt") as f:
    while True:     
        line1 = [int(x) for x in f.readline().strip("\n").split()]
        line2 = [int(x) for x in f.readline().strip("\n").split()]
        line3 = [int(x) for x in f.readline().strip("\n").split()]
        if len(line1) == 0:
            break
        count += check([line1[0], line2[0], line3[0]])
        count += check([line1[1], line2[1], line3[1]])
        count += check([line1[2], line2[2], line3[2]])
print count