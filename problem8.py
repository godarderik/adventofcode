import ast


def problema():  
    f = open("input8.txt")

    codeCount = 0
    outCount = 0

    for line in f:
        line = line.strip("\n")
        codeCount += len(line)
        outCount += len(ast.literal_eval(line))
    f.close()
    return codeCount - outCount
        
def problemb():
    f = open("input8.txt")

    outCount = 0

    for line in f:
        line = line.strip("\n")
        outCount += line.count('\\') + line.count('"') + 2
    f.close()
    return outCount
print problema(), problemb()

