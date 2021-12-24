import math
import itertools
import aoc_util as util
import re
import copy


day = 20

# get input
with open(f'{day}.txt', 'r') as f:
    data = f.read().strip().split('\n')  # f.readlines()

data = util.parse_groups(data)
enhance = data[0][0]

data = util.parse_matrix(data[1], "")


def enlarge(grid):
    inf_tile = grid[0][0]
    for i in range(len(grid)):
        grid[i] = [inf_tile] + grid[i] + [inf_tile]

    tmp = [[inf_tile for i in range(len(grid[0]))]]
    for row in grid:
        tmp.append(row)

    tmp.append([inf_tile for i in range(len(grid[0]))])
    return tmp


def neighbors(x, y, size_x, size_y, grid):
    n = []
    for i in range(-1, 2):
        r = ""
        for j in range(-1, 2):
            if (x+j < 0 or y+i < 0 or j+x >= size_x or y+i >= size_y):
                r += grid[0][0]
            else:
                r += grid[y+i][x+j]
        n.append(r)
    return n


def get_pxl(i, j, grid):
    n = neighbors(i, j, len(grid[0]), len(grid), grid)
    b = f'{n[0]}{n[1]}{n[2]}'.replace(".", "0").replace("#", "1")
    idx = int(b, 2)
    return enhance[idx]


grid = enlarge(enlarge(enlarge(data)))


n = 50
for k in range(n):
    n = len(grid)
    temp = [["" for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = get_pxl(j, i, grid)
    grid = enlarge(temp)

count = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        count += grid[i][j] == "#"

print(count)
