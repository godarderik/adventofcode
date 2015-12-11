f = open("input11.txt")

def increment(char):
    return(chr(ord(char)+1))

def incrementString(string):
    string = list(string)
    last = string[-1]
    ind = -1
    while increment(last) == "{":
        string[ind] = "a"
        ind -= 1
        last = string[ind]
    string[ind] = increment(last)
    return "".join(string)
        
def testString(string):
    run1 = 0
    char2 = -1
    run2 = False
    for k,char in enumerate(string):
        if char == "i" or char == "o" or char == "l":
            return False
        try:
            if char == string[k+1] and k != char2:
                char2 = k+1
                run1 += 1
        except:
            pass
        try: 
            if increment(char) == string[k+1] and increment(string[k+1]) == string[k+2]:
                run2 = True
        except:
            pass
    return run1 > 1 and run2


inpt = "cqjxxzaa"
count = 0
while not testString(inpt):
    inpt = incrementString(inpt)
print inpt