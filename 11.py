import math
import itertools
import aoc_util as util
import re



day = 11

# get input
with open(f'{day}.txt', 'r') as f:
    input = f.read().strip().split('\n')  # f.readlines()


# transform the input, apply to every row
def apply_to_row(x):
    # do stuff
    return x
input = list(map(apply_to_row,input))

input = util.parse_matrix(input,"",int)

def rec_flash(x,y,input, flashed):
    s = 0
    for (i,j) in util.neighbors(x,y,len(input),len(input)):
        if flashed[i][j]:
            continue
        input[i][j] += 1
    
        if input[i][j] > 9:
            flashed [i][j] = True 
            input[i][j] = 0
            s += 1
            s += rec_flash(i,j,input,flashed)
    return s

# solve
flashes = 0
all_flashed = False
iterations = 0

while not all_flashed:
    input = util.map_matrix(input,lambda x: x+1)
    flashed = util.map_matrix(input,lambda x: False)
    for x in range(len(input)):
        for y in range(len(input)):
            if flashed[x][y]:
                continue
            if input[x][y] > 9:
                flashed[x][y] = True 
                flashes += 1
                input[x][y] = 0
                flashes += rec_flash(x,y,input,flashed)
    
    all_flashed = True
    iterations += 1
    for row in flashed:
        for elem in row:
            if not elem:
                all_flashed = False
                break
        if not all_flashed:
            break

 
print(iterations)





