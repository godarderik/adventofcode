from collections import *
from itertools import *


height = 6
width = 50
arr = [[0]*width for x in range(height)]

def set_arr(a,b):
    global arr
    for x in range(a):
        for y in range(b):
            arr[y][x] = 1
def rotate_row(a,b):
    global arr
    b = b % 50
    new = arr[a][-1 * b:] + arr[a][:-1 * b]
    arr[a] = new

def rotate_col(a,b):
    global arr
    new = []
    b = b % 6
    for x in range(height):
        new.append(arr[x][a])
    new = new[-1 * b:] + new[:-1 * b]
    for x in range(height):
        arr[x][a] = new[x]


with open("input8.txt") as f:
    for line in f:
        line = line.strip().split()
        if line[0] == "rect":
            y = line[1].split("x")
            set_arr(int(y[0]), int(y[1]))
        elif line[1] == "row":
            rotate_row(int(line[2][2:]),int(line[-1]))
        else:
            rotate_col(int(line[2][2:]),int(line[-1]))

#123
#AFBUPZBJPS
count = 0
for x in arr:
    string = ""
    for y in x:
        if len(string)%6 == 0:
            string += " "
        string += str(y)
        
        if y == 1:   
            count += 1
    print string
print count