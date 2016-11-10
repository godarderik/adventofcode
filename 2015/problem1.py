def problema():
    f = open("input1.txt")
    inpt = f.read()
    return inpt.count("(") - inpt.count(")")

def problemb():
    count = 0
    f = open("input1.txt")
    string = f.read()

    for k,x in enumerate(string):
        if x == "(":
            count += 1
        else:   
            count -= 1
        if count < 0:
            return k+1 

print problema(), problemb() 