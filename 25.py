import math
import itertools
import aoc_util as util
import re


day = 25

# get input
with open(f'{day}.txt', 'r') as f:
    data = f.read().strip().split('\n')  # f.readlines()


matrix = util.parse_matrix(data,'')

def target_empty(x,y):
    if matrix[y][x] == ">":
        if x < len(matrix[0])-1:
            return matrix[y][x+1] == '.'
        else:
            return matrix[y][0] == '.'
    elif matrix[y][x] == 'v':
        if y < len(matrix)-1:
            return matrix[y+1][x] == '.'
        else:
            return matrix[0][x] == '.'
    else:
        return False

def target(x,y):
    if matrix[y][x] == ">":
        if x < len(matrix[0])-1:
            return x+1,y
        else:
            return 0,y
    elif matrix[y][x] == 'v':
        if y < len(matrix)-1:
            return x,y+1
        else:
            return x,0
    else:
        return x,y

i = 0
has_moved = True
while has_moved:
    print(i)
    has_moved = False
    for group in ['>','v']:
        new_mat = util.map_matrix(matrix,lambda x: x)
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == group and target_empty(x,y):
                    nx,ny = target(x,y)
                    new_mat[ny][nx] = group 
                    new_mat[y][x] = '.'
                    has_moved = True
        matrix = new_mat
        #util.print_matrix(matrix)
        #input()
    i += 1
    print(i)
print("Done.",i)
