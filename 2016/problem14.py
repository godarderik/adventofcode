import hashlib

key = "jlmsuwbz"
num = 0
check = {}
seen = []
seen_hash = {}

def contains_triple(string):
    for a in range(len(string) - 2):
        if string[a] == string[a+1] and string[a+1] == string[a+2] and string[a] == string[a+2]:
            return string[a]

def contains_five(string, c):
    return any([string[a] == c and string[a+1] == c and string[a+2] == c  and string[a+3] == c  and string[a+4] == c  for a,_ in enumerate(string[:-4])])

while True:
    val = hashlib.md5(key + str(num)).hexdigest().lower()
    for z in range(2016):
        val = hashlib.md5(val).hexdigest().lower()
    for k,v in check.iteritems():
        if contains_five(val, v) and not (k, v) in seen_hash:
            seen.append((k,v))
            seen_hash[(k,v)] = 1
    if len(seen) >= 64:
        print seen[-1], num, seen
        break
    if contains_triple(val):
        check[num] = contains_triple(val)
    if num - 1000 in check:
        del check[num-1000]
    num += 1
print list(sorted(seen, key = lambda x: x[0]))[63]
    