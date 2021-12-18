import math
import itertools
import aoc_util as util
import re
import timeit


def main():
    day = 7

    # get input
    with open(f'{day}.txt', 'r') as f:
        input = f.read().strip().split('\n')  # f.readlines()
    input = input[0].split(',')

    # transform the input, apply to every row

    def apply_to_row(x):
        # do stuff
        return int(x)

    input = list(map(apply_to_row, input))

    range_min = 10000000000000000
    range_max = -100000

    for p in input:
        range_min = min(p, range_min)
        range_max = max(p, range_max)

    def calc_pos_val(positions, x):
        s = 0
        for p in positions:
            n = abs(x-p)
            s += n*(n+1)/2
        return s

    #print(calc_pos_val([0], 5))

    # solve
    ans = 1000000000000000
    for l in range(range_min, range_max+1):

        m = calc_pos_val(input, l)
        if m < ans:
            ans = m

    # print(ans)


main()
