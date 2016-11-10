import itertools


dicti = {"a":1, "b":0}

lines = []

with open('input23.txt') as f:
    for line in f:
        line = line.strip("\n").split(" ")
        lines.append(line)

pointer = 0
while pointer < len(lines) and pointer >= 0:
    curr = lines[pointer]
    if curr[0] == "hlf":
        dicti[curr[1]] /= 2.0
        pointer += 1
    elif curr[0] == "tpl":
        dicti[curr[1]] *= 3
        pointer += 1
    elif curr[0] == "inc":
        dicti[curr[1]] += 1
        pointer += 1
    elif curr[0] == "jmp":
        pointer += int(curr[1])
    elif curr[0] == "jie":
        if dicti[curr[1]] % 2 == 0:
            pointer += int(curr[2])
        else:
            pointer += 1
    elif curr[0] == "jio":
        if dicti[curr[1]] == 1:
            pointer += int(curr[2])
        else:
            pointer += 1
print dicti