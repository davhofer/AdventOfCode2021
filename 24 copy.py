import math
import itertools
import aoc_util as util
import re


day = 24

# get input
with open(f'{day}.txt', 'r') as f:
    input = f.read().strip().split('\n')  # f.readlines()


mem = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
# transform the input, apply to every row


def apply_to_row(x):

    return x.split(" ")


correct = []

prog = list(map(apply_to_row, input))
# range(99999999554187, 11111111111111, -1):
for i in range(11111111111111, 99999999999999):
    inp = str(i)
    if '0' in inp:
        continue
    idx = 0
    # solve
    mem = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for ins in prog:
        if ins[0] == "inp":
            mem[ins[1]] = int(inp[idx])
            idx += 1
            continue
        b = mem[ins[2]] if ins[2] in mem.keys() else int(ins[2])
        if ins[0] == "add":
            mem[ins[1]] += b
        elif ins[0] == "mul":
            mem[ins[1]] *= b
        elif ins[0] == "div":
            if b == 0:
                break
            mem[ins[1]] //= b
        elif ins[0] == "mod":
            if mem[ins[1]] < 0 or b <= 0:
                break
            mem[ins[1]] %= b
        elif ins[0] == "eql":
            mem[ins[1]] = int(mem[ins[1]] == b)
    if mem['z'] == 0:
        print(i)
        break
