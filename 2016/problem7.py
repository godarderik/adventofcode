from itertools import *

count1 = 0
count2 = 0

def hasABBA(string):
    return any([string[k] == string[k+3] and string[k+1] == string[k+2] and not string[k] == string[k+1] for k,v in enumerate(string[:-3])])
def allABA(string):
    return [string[k:k+3] for k,v in enumerate(string[:-2]) if v == string[k+2] and not v == string[k+1]]
def match(str1, str2):
    return str1[0] == str2[1] and str1[1] == str2[0]

with open("input7.txt") as f:
    for line in f:
        line = line.strip("\n")
        line = line.split("[")

        seen_out = False
        seen_in = False
        outseq = []
        inseq = []
        for x in line:
            x = x.split("]")
            if len(x) == 1:
                seen_out = seen_out or hasABBA(x[0])
                outseq += allABA(x[0])
            elif len(x) == 2:
                inseq += allABA(x[0])
                outseq += allABA(x[1])

                seen_in = seen_in or hasABBA(x[0])
                seen_out = seen_out or hasABBA(x[1])
        count1 += seen_out and not seen_in
        count2 += any([match(x[0], x[1]) for x in product(outseq, inseq)])
print count1, count2


