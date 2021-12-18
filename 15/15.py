from typing import Dict, Set, Tuple, List
from queue import PriorityQueue
import math
import itertools
import aoc_util as util
import re

import heapq

day = 15

# get input
with open(f'{day}.txt', 'r') as f:
    input = f.read().strip().split('\n')  # f.readlines()

input = util.parse_matrix(input, '', int)

n = len(input)
m = len(input[0])

for row in input:
    for i in range(4):
        for x in row[m*i:]:
            row.append(1 if x == 9 else x+1)

for i in range(4):
    for row in input[n*i:]:
        new_row = []
        for x in row:
            new_row.append(1 if x == 9 else x+1)
        input.append(new_row)

N = n*5
M = m*5


# Graph solution:
g = util.Graph(N*M)

for i in range(N):
    for j in range(M):
        idx = i*M+j
        for x, y in util.neighbors(j, i, M, N, False):
            idx2 = y*M+x
            g.addEdge(idx, idx2, directed=True, weight=input[y][x])

print(g.dijkstra(0, N*M-1))


# matrix solution
print(util.dijkstra_matrix(input, (0, 0), (M-1, N-1), False))
