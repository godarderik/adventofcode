from collections import *

reg = {"a": 0, "b": 0, "c": 1, "d": 0}
ind = 0
lines = []

with open('input12.txt') as f:
    lines = [line.strip().split() for line in f]

def value(key, dic):
    return dic[key] if key in dic.keys() else int(key)

while ind != len(lines):
    line = lines[ind]

    if line[0] == "inc":
        reg[line[1]] += 1
    elif line[0] == "dec":
        reg[line[1]] -= 1
    elif line[0] == "cpy":
        reg[line[2]] = value(line[1], reg)
    elif line[0] == "jnz" and value(line[1], reg) != 0:
        ind += int(line[2])
        continue
    ind += 1
print reg["a"]