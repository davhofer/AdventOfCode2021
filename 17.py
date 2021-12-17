import math
import itertools
import aoc_util as util
import re


day = 17

# get input
# with open(f'{day}.txt', 'r') as f:
#     input = f.read().strip().split('\n')  # f.readlines()


# testcase:
# target area: x=20..30, y=-10..-5

# submission:
# target area: x=175..227, y=-134..-79


def step(x, y, velocity):
    x += velocity[0]
    y += velocity[1]
    vx = velocity[0]
    vx = 0 if vx == 0 else vx-vx/abs(vx)
    new_v = (vx, velocity[1]-1)
    return x, y, new_v


#target = ((20, 30), (-10, -5))
target = ((175, 227), (-134, -79))
x = 0
y = 0

velos = set()


def try_velo(vx, vy):
    orig = (vx, vy)
    x = 0
    y = 0
    velocity = (vx, vy)
    max_y = 0
    while x <= target[0][1] and y >= target[1][0]:
        x, y, velocity = step(x, y, velocity)

        if x in range(target[0][0], target[0][1]+1) and y in range(target[1][0], target[1][1]+1):
            velos.add(orig)
            return 1
    return None


m = 0
for x in range(1, 350):
    for y in range(-200, 300):
        try_velo(x, y)


print(len(velos))


# DP = [[0 for i in range(target[0][1]+1)] for j in range(target[1][0], 500)]


# def dp(vx, vy, pos):
