import math
import itertools
import aoc_util as util
import re


day = 14

seq = "VOKKVSKKPSBVOOKVCFOV"

letters = {
    "V": 0,
    "O": 0,
    "K": 0,
    "S": 0,
    "P": 0,
    "B": 0,
    "F": 0,
    "C": 0,
    "N": 0,
    "H": 0
}

seq_tst = "NNCB"

# get input
with open(f'{day}test.txt', 'r') as f:
    input = f.read().strip().split('\n')  # f.readlines(


# transform the input, apply to every row
rules = {}


def apply_to_row(x):
    x = x.split(" -> ")
    rules[x[0]] = x[1]
    return x


input = list(map(apply_to_row, input))


occ = {}

sequence = seq_tst


for k in rules.keys():
    occ[k] = 0
for i in range(len(sequence)-1):
    occ[sequence[i:i+2]] += 1

for i in range(40):
    next_occ = {k: 0 for k in occ.keys()}
    for o in occ.keys():

        n = occ[o]
        if n == 0:
            continue

        l = rules[o]
        next_occ[o[0]+l] += n
        next_occ[l+o[1]] += n
    occ = next_occ

l0 = sequence[0]
l1 = sequence[-1]
letters[l0] += 1
letters[l1] += 1

for l in occ.keys():
    print(l, occ[l])
    for x in letters.keys():
        if x == l[0]:
            letters[x] += occ[l]
        if x == l[1]:
            letters[x] += occ[l]

for l in letters.keys():
    letters[l] = letters[l]/2
    print(l, letters[l])

print(letters)

maxl = 0
minl = 1000000000000000000
for l in letters.keys():
    if letters[l] > maxl:
        maxl = letters[l]
    if letters[l] > 0 and letters[l] < minl:
        minl = letters[l]


print("done")
print(maxl - minl)
