inputs = {}

with open("input15.txt") as f:
    for line in f:
        line = line.strip("\n")
        line = line.split(" ")
        inputs[line[0]] = [int(line[2].strip(",")), int(line[4].strip(",")), int(line[6].strip(",")), int(line[8].strip(",")), int(line[10])]

maxScore = 0

for a in range(101):
    for b in range(101 - a):
        for c in range(101 - a - b):
            for d in range(101 - a - b - c):
                score = 1
                scores = []
                for x in range(5):
                    scores.append(a * inputs["Frosting:"][x] + b * inputs["Candy:"][x] + c * inputs["Butterscotch:"][x] + d * inputs["Sugar:"][x]) 
                for y in scores[:-1]:
                    if y < 0:
                        y = 0
                    score *= y
                if scores[4] == 500:
                    maxScore = max(score, maxScore)
print maxScore

