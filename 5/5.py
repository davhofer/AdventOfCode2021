import math
import itertools
import aoc_util as util
import re



day = 5

# get input
with open(f'{day}.txt', 'r') as f:
    input = f.read().strip().split('\n')  # f.readlines()


# transform the input, apply to every row
max_x = 0
max_y=0
edges = []


# solve
ans = 0
print(input)
for x in input:
    l = x.split(' -> ')
    x1,y1 = l[0].split(',')
    x2,y2 = l[1].split(',')
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    edges.append((x1,y1,x2,y2))
    if x1 > max_x:
        max_x = x1 
    if x2 > max_x:
        max_x = x2
    if y1 > max_y:
        max_y = y1 
    if y2 > max_y:
        max_y = y2


mat = [[0 for x in range(max_x+1)] for y in range(max_y+1)]



for e in edges:
    if e[2] == e[0]:
        start = min(e[1],e[3])
        end = max(e[1],e[3])
        for y in range(start,end+1):
            mat[e[0]][y] += 1


    elif e[1] == e[3]:
        start = min(e[0],e[2])
        end = max(e[0],e[2])
        for x in range(start,end+1):
            mat[x][e[1]] += 1
    else:
        if e[0] < e[2]:
            fx = 1
        else:
            fx = -1
        if e[1] < e[3]:
            fy = 1
        else:
            fy = -1
        for d in range(abs(e[2]-e[0])+1):
            mat[e[0]+d*fx][e[1]+d*fy] += 1
    
    



for row in mat:
    print(row)

s = 0
for x in range(len(mat[0])):
    for y in range(len(mat)):
        if mat[x][y] > 1:
            s += 1
print(s)



