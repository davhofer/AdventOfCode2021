import math
import itertools
import aoc_util as util
import re
import numpy as np


day = 22

# get input
with open(f'{day}.txt', 'r') as f:
    input = f.read().strip().split('\n')  # f.readlines()


# transform the input, apply to every row
def apply_to_row(x):

    x = x.split(',')
    onoff = x[0].split(' ')[0]
    x = list(map(lambda y: y.split('=')[1], x))
    x = list(map(lambda y: y.split('..'), x))
    x = list(map(lambda y: [int(z) for z in y], x))

    return (onoff, x)


input = list(map(apply_to_row, input))


"""
idea:
take the intersection of 2 cuboids
calculate the difference from it
"""


def intersection(cuboid1, cuboid2):
    intersect = []

    for i in range(3):
        if cuboid1[i][0] > cuboid2[i][1] or cuboid1[i][1] < cuboid2[i][0]:
            return -1
        intersect.append([max(cuboid1[i][0], cuboid2[i][0]),
                          min(cuboid1[i][1], cuboid2[i][1])])
    return intersect


def diff(cuboid1, cuboid2):
    intersect = intersection(cuboid1, cuboid2)
    if intersect == -1:
        return [cuboid1]

    differences = []

    # below:
    if cuboid1[2][0] <= intersect[2][0]-1:
        differences.append(
            [cuboid1[0], cuboid1[1], [cuboid1[2][0], intersect[2][0]-1]])
    # above:
    if intersect[2][1]+1 <= cuboid1[2][1]:
        differences.append(
            [cuboid1[0], cuboid1[1], [intersect[2][1]+1, cuboid1[2][1]]])

    # left:
    if cuboid1[0][0] <= intersect[0][0]-1:
        differences.append(
            [[cuboid1[0][0], intersect[0][0]-1], cuboid1[1], intersect[2]])
    # right:
    if intersect[0][1]+1 <= cuboid1[0][1]:
        differences.append(
            [[intersect[0][1]+1, cuboid1[0][1]], cuboid1[1], intersect[2]])

    # in front
    if cuboid1[1][0] <= intersect[1][0]-1:
        differences.append(
            [intersect[0], [cuboid1[1][0], intersect[1][0]-1], intersect[2]])

    # behind
    if intersect[1][1]+1 <= cuboid1[1][1]:
        differences.append(
            [intersect[0], [intersect[1][1]+1, cuboid1[1][1]], intersect[2]])

    return differences


# solve
cuboids_on = []

for cmd in input:
    is_on = cmd[0] == "on"
    cuboid = cmd[1]

    next_cuboids = []
    for cuboid_on in cuboids_on:
        for c in diff(cuboid_on, cuboid):
            next_cuboids.append(c)
    if is_on:
        next_cuboids.append(cuboid)

    cuboids_on = next_cuboids

lights_on = 0
for cuboid in cuboids_on:
    vol = 1
    for i in range(3):
        vol *= (cuboid[i][1]-cuboid[i][0]+1)
    lights_on += vol

print(lights_on)
