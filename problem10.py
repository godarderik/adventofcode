f = open("input10.txt")

def nextnumber(number):
    out = ""


    number += " "
    currChar = number[0]
    currLen = 1
    for k,v in enumerate(number[:-1]):
        if v == number[k+1]:
            currLen += 1
        else:
            out += str(currLen) + str(currChar) 
            currChar = number[k+1]
            currLen = 1
    return out


inpt = "3113322113"

for x in range(50):
    inpt = nextnumber(inpt)
print len(inpt)