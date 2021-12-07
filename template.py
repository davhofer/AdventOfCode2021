import math
import itertools
import aoc_util as util
import re


# TODO: adjust day
input("HAVE YOU ADJUSTED THE DAY?")

day = 1

# get input
with open(f'{day}.txt', 'r') as f:
    input = f.read().strip().split('\n')  # f.readlines()


# transform the input, apply to every row
def apply_to_row(x):
    # do stuff
    return x
input = list(map(apply_to_row,input))

# solve
ans = 0
for l in input:
    pass




print(ans)
