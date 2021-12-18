import math
import itertools
import aoc_util as util
import re


day = 10

# get input
with open(f'{day}.txt', 'r') as f:
    input = f.read().strip().split('\n')  # f.readlines()


# transform the input, apply to every row
def apply_to_row(x):
    # do stuff
    return x


input = list(map(apply_to_row, input))


def closing(x):
    return x == ']' or x == '}' or x == ')' or x == '>'


def match(o, c):
    return (o == '[' and c == ']') or (o == '(' and c == ')') or (o == '{' and c == '}') or (o == '<' and c == '>')


def parencheck(line):
    items = []
    for elem in line:
        if len(items) == 0:
            if closing(elem):
                return []
        if closing(elem):
            if match(items[-1], elem):
                items.pop()
            else:
                return []  # elem
        else:
            items.append(elem)
    if len(items) == 0:
        return []
    if len(items) > 0:
        items.reverse()
        s = 0
        for x in items:
            s = s * 5 + rev_score(x)

        return s


def score(x):
    if x == ')':
        return 3
    if x == ']':
        return 57
    if x == '}':
        return 1197
    if x == '>':
        return 25137
    return 0


def rev_score(x):
    if x == '(':
        return 1
    if x == '[':
        return 2
    if x == '{':
        return 3
    if x == '<':
        return 4
    return 0


# solve
ans = 0
scores = []
for l in input:
    #ans += score(parencheck(l))
    items = parencheck(l)
    if items == []:
        continue

    scores.append(items)

scores.sort()
print(scores)

ans = scores[len(scores)//2]


print(ans)
