import math
import itertools
import aoc_util as util
import re

import numpy as np
from copy import deepcopy


day = 13

# get input
with open(f'{day}.txt', 'r') as f:
    input = f.read().strip().split('\n')  # f.readlines()


input = util.parse_groups(input)
coords = input[0]
input = input[1]

# transform the input, apply to every row
max_x, max_y = 0, 0
def apply_to_row(x):
    global max_x, max_y
    x = x.split(',')
    x = (int(x[0]),int(x[1]))
    if x[0] > max_x:
        max_x = x[0]
    if x[1] > max_y:
        max_y = x[1]
    return x
coords = list(map(apply_to_row,coords))


matrix = [[0 for j in range(max_x+1)] for i in range(max_y+1)]

inst = []
for i in input:
    ins = i.split(' ')[2].split('=')
    ins = (ins[0],int(ins[1]))
    inst.append(ins)



for (x,y) in coords:
    matrix[y][x] = 1


for (axis,idx) in inst:
    
    
    m1, m2 = util.split_matrix_at(idx,axis,matrix)
    m2 = util.flip_matrix(axis,m2)


    if len(m1[0])<len(m2[0]) or len(m1)<len(m2):
        small = m1 
        big = m2 
        x = len(m1[0])
        y = len(m1)
    else:
        small = m2 
        big = m1 
        x = len(m2[0])
        y = len(m2)
    
    for i in range(x):
        for j in range(y):
            if small[len(small)-j-1][len(small[0])-i-1] == 1:
                big[len(big)-j-1][len(big[0])-i-1] = 1
    
    matrix = big



    

    
    

for row in matrix:
    for x in row:
        if x > 0:
            print("X",end='')
        else:
            print(" ",end='')
    print()

