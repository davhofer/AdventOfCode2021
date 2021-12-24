import math
import itertools
import aoc_util as util
import re


day = 21

# get input
# with open(f'{day}.txt', 'r') as f:
#     input = f.read().strip().split('\n')  # f.readlines()
p1 = 4
p2 = 8

moves = 0
DP = {}
# entry: field 1, field 2, pts 1, pts 2 move nr


# DP [p1][p2][m] = if m%2 == 0: DP[p1-1][p2][m-1] + DP[p1-2][m-1] + DP[]

M = {}


def f(n1, n2, p1, p2):
    x = 0
    y = 0
    for i in range(3, 10):
        m = [0, 0, 0, 1, 3, 6, 7, 6, 3, 1][i]
        p3 = [(p1+i) % 10, 10][(p1+i) % 10 == 0]
        if p3 >= n1:
            x += m
        else:
            if (n2, n1-p3, p2, p3) in M:
                z = M[(n2, n1-p3, p2, p3)]
            else:
                z = f(n2, n1-p3, p2, p3)
            x, y = x+z[1]*m, y+z[0]*m
    M[(n1, n2, p1, p2)] = (x, y)
    return (x, y)


print(max(f(21, 21, 8, 10)))


def dp(p1, p2, f1, f2, m, r):
    if (p1, p2, f1, f2, m, r) in DP:
        return DP[p1, p2, f1, f2, m, r]

    x = 1 + dp(p1-1, p2, m-1) + 2 + dp(p1-2, p2, m-1) + 3 + dp(p1-3, p2, m -
                                                               1) if m % 2 == 0 else 1 + dp(p1, p2-1, m-1) + 2 + dp(p1, p2-2, m-1) + 3 + dp(p1, p2-3, m-1)
    DP[p1][p2][m] = x
    return x


s1 = 0
s2 = 0
