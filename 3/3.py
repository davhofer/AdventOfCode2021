import math
import itertools
from graphs import *


day = 3

# get input
with open(f'{day}.txt', 'r') as f:
    input = f.read().strip().split('\n')  # f.readlines()


# gammas = [0 for i in range(len(input[0])-1)]
# deltas = [0 for i in range(len(input[0])-1)]
# # process input
# for l in input:
#     for i in range(len(l)-1):
#         if l[i] == '1':
#             gammas[i] += 1
#         else:
#             deltas[i] += 1


# n = len(input)

# g = ''
# d = ''

# for i in gammas:
#     if i > n/2:
#         g += '1'
#         d += '0'
#     else:
#         g += '0'
#         d += '1'


# most_common = int(g, 2)
# least_common = int(d, 2)


# def check_g(i):
#     def check_bit(word):
#         return word[i] == g[i]
#     return check_bit


# def check_d(i):
#     def check_bit(word):
#         return word[i] == d[i]
#     return check_bit


def get_most_common(list, idx):
    c = 0
    for i in list:
        if i[idx] == '1':
            c += 1
    if c >= len(list)/2:
        return '1'
    return '0'


def get_least_common(list, idx):
    c = 0
    for i in list:
        if i[idx] == '1':
            c += 1
    if c >= len(list)/2:
        return '0'
    return '1'


input2 = input.copy()
for i in range(len(input[0])-1):

    mc = get_most_common(input, i)
    mc2 = get_least_common(input2, i)
    if len(input) > 1:
        new = []
        for x in input:
            if x[i] == mc:
                new.append(x)
        input = new
    if len(input2) > 1:
        new2 = []
        for x in input2:
            if x[i] == mc2:
                new2.append(x)

        input2 = new2

g = int(input[0], 2)*int(input2[0], 2)


# print(g*d)

# solve problem

print(g)
