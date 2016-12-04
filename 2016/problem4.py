import collections

count = 0
arr = []

#process input
with open("input4.txt") as f:
    for line in f:
        line = line.strip("\n").split("-")

        key = int(line[-1][:3])
        code = line[-1][4:-1]
        s = "".join(line[:-1])

        arr.append({"s":s, "key":key, "code":code})

#part a 
for item in arr:
    c = collections.Counter(item["s"])
    c = list(sorted(c, key=lambda word: (-c[word], word)))[:5]
    if "".join([v[0] for v in c]) == item["code"]:
        count += item["key"]
print count

#part b
lets = "abcdefghijklmnopqrstuvwxyz"
def rotate(char,x):
    z = lets.index(char) + (x % 26)
    if z > 25:
        z = abs(25 - z)
    return lets[z]

for item in arr:
    out = "".join([rotate(x, item["key"]) for x in item["s"]])
    if out.find("north") >= 0:
        print item["key"]
        break