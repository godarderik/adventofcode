def same(string):
    val = True
    for k,v in enumerate(string[:-1]):
        val = v == string[k-1] and val
    return val

def problema():
    f = open("input5.txt")
    count = 0
    tot = 0
    for line in f:
        test1 = line.count("a") + line.count("e") + line.count("i") + line.count("o") + line.count("u") >= 3
        test2 = False
        test3 = line.count("ab") + line.count("cd") + line.count("pq") + line.count("xy") == 0
        for k,v in enumerate(line[:-1]):
            if v == line[k+1]:
                test2 = True
        if test1 and test3 and test2:
            count += 1
        tot += 1
    f.close()
    return count
def problemb():
    f = open("input5.txt")
    count = 0
    tot = 0
    for line in f:
        tot += 1
        line = line.strip("\n")
        test1 = False
        test2 = False
        pairs = {}
        rec = None
        for k,v in enumerate(line[:-1]):
            pair = v + line[k+1]
            if pair in pairs and (pair != rec):
                test2 = True
                break
            elif pair in pairs and k > 2 and same(line[k-2:k+1]):
                test2 = True
                break
            else:
                pairs[pair] = 1
            rec = pair
        for k,v in enumerate(line[:-2]):
            if v == line[k + 2]:
                test1 = True
        if test1 and test2:
            count += 1
    f.close()
    return count


print problema(), problemb()