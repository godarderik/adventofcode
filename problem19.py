import re
from collections import defaultdict

vals = defaultdict(list)
keys = {}
inpt = ""

with open("input19.txt") as f:
    for line in f:
        line = line.strip("\n").split(" ")
        try:
            vals[line[0]].append(line[2])
            keys[line[2]] = line[0]
        except:
            inpt = line[0]
class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0

class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0


order = sorted(keys.keys(), key = len)[::-1]

def problema():
    stored = set()

    for k,v in vals.iteritems():
        for z in v:
            for x in re.finditer(k, inpt):
                newStr = inpt[:x.start()] + z + inpt[x.start() + len(k):]
                stored.add(newStr)
    print len(stored)

def generateSuccessors(state):
    for k,v in vals.iteritems():
        for z in v:
            for x in re.finditer(k, state[0]):
                newStr = state[0][:x.start()] + z + state[0][x.start() + len(k):]
                yield [newStr, state[1] + 1]
def generateSuccessors2(state):
    out = []
    for k in order:
        for z in reversed([y for y in re.finditer(k, state[0])]):
            newStr = state[0][:z.start()] + keys[k] + state[0][z.start() + len(k):]
            newNum = state[1] + 1
            out.append([newStr, newNum, z.start()])
    for x in sorted(out, key = lambda x: x[2], reverse = False):
        yield x[:2]

def isGoalState(state):
    return state[0] == "e"


def problemb():

    queue = Stack()
    queue.push([inpt, 0])
    minLen = 999

    while not queue.isEmpty():
        state = queue.pop()
        if len(state[0]) < minLen:
            minLen = len(state[0])
        if isGoalState(state):
            print state[1]
            return
        lst = [x for x in generateSuccessors2(state)]
        for x in sorted(lst, key = len):
            queue.push(x)



problema()
problemb()