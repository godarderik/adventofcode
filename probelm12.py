import json
import re
f = open("input12.json").read()

line = json.loads(f)

out = []

def itera(item):
    if type(item) == int:
        yield item
    elif type(item) == type([]):
        for x in item:
            for a in itera(x):
                yield a
    elif type(item) == type({}):
        shouldYield = True
        #add this section for part 2
        for x,y in item.iteritems():
            if x == "red" or y == "red":
                shouldYield = False
        ###end part 2
        for x,y in item.iteritems():
            for z in itera(y):
                if shouldYield: 
                    yield z
                        
#original way of doing problem 1
#very bad
def problem1():
    count = 0
    for x in line:
        x = str(x).split(" ")
        for y in x:

            y = re.sub(r'[^a-zA-Z0-9-]', '', y)
            try:
                count += int(y)
            except:
                print y
    print count

def problem2():
    count = 0
    for y in itera(line):
        count += y
    print count
            
problem2()

