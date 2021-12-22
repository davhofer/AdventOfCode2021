import math
import itertools
import aoc_util as util
import re
import numpy as np

day = 9

# get input
with open(f'{day}.txt', 'r') as f:
    input = f.read().strip().split('\n')  # f.readlines()


# transform the input, apply to every row
def apply_to_row(x):
    # do stuff
    return x


input = list(map(apply_to_row, input))


def inbound(i, j, m):
    return (i >= 0 and i < len(m) and j >= 0 and j < len(m[0]))


def basin(i, j, m, prev, visited):
    if (not inbound(i, j, m)) or m[i][j] == 9 or m[i][j] <= prev or visited[i][j]:
        return 0
    visited[i][j] = True
    x = m[i][j]
    s = 0
    for k in range(i-1, i+2):
        for l in range(j-1, j+2):
            if k == i and l == j:
                continue
            if not (l == j or i == k):
                continue
            s += basin(k, l, m, x, visited)
    return 1 + s


def is_lowpoint(i, j, m):
    x = m[i][j]
    ok = True
    if i > 0:
        ok = ok and m[i-1][j] > x
    if i < len(m)-1:
        ok = ok and m[i+1][j] > x
    if j > 0:
        ok = ok and m[i][j-1] > x
    if j < len(m[0])-1:
        ok = ok and m[i][j+1] > x
    b = 0
    if ok:
        v = [[False for b in range(len(input[0]))] for a in range(len(input))]
        b = basin(i, j, m, -1, v)
    return ok, b


input = util.parse_matrix(input, "", int)


# solve
ans = 0
basins = []
for j in range(len(input[0])):
    for i in range(len(input)):
        is_low, bas = is_lowpoint(i, j, input)
        if is_low:
            basins.append(bas)
            ans += input[i][j] + 1

n = 3
basins = np.array(basins)
idx = np.argpartition(basins, -n)[-n:]
indices = idx[np.argsort((-basins)[idx])]
ans = 1
for i in indices:
    ans *= basins[i]
print(ans)
