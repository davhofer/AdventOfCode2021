import math
import aoc_util as util
import copy

day = 18

# get input
with open(f'{day}.txt', 'r') as f:
    input = f.read().strip().split('\n') 

input = list(map(lambda x: util.parse_rec_list(x, 0)[0], input))


class Inorder:

    def __init__(self, to_replace):
        self.to_replace = to_replace
        self.elem_index = -1
        self.index = -1

    def find(self, tree):
        for i in range(2):
            if type(tree[i]) == int:
                self.index += 1
                if tree[i] == -1:
                    self.elem_index = self.index
                    return True
            elif type(tree[i]) == list:
                found = self.find(tree[i])
                if found:
                    return True
        return False

    def replace(self, tree):
        for i in range(2):
            if type(tree[i]) == int:
                self.index += 1
                if self.index == self.elem_index-1:
                    tree[i] += self.to_replace[0]
                if self.index == self.elem_index:
                    tree[i] = 0
                if self.index == self.elem_index+1:
                    tree[i] += self.to_replace[1]
                    return True
            elif type(tree[i]) == list:
                if self.replace(tree[i]):
                    return True
        return False

    def go(self, tree):
        self.find(tree)
        self.index = -1
        self.replace(tree)


def add(s1, s2):
    return(copy.deepcopy([s1, s2]))


def rec_red(node, depth: int, explosion: bool):

    for i, elem in enumerate(node):

        if not explosion and type(elem) == int and elem >= 10:
            node[i] = [math.floor(elem/2), math.ceil(elem/2)]
            return True, [-1, -1]
        if explosion and type(elem) == list and depth == 4:
            node[i] = -1
            return True, elem  # will return this to the top, then do 2x inorder traversal. first find global index, then change numbers
        if type(elem) == list and depth < 4:
            was_reduced, exploded = rec_red(elem, depth+1, explosion)
            if was_reduced:
                return was_reduced, exploded
    return False, [-1, -1]


def reduce(s):
    was_reduced, exploded = rec_red(s, 1, True)
    if not was_reduced:
        was_reduced, exploded = rec_red(s, 1, False)
    if was_reduced:
        if exploded != [-1, -1]:
            inorder = Inorder(exploded)
            inorder.go(s)
        return reduce(s)
    return s


def magnitude(elem):
    if type(elem) == list:
        return 3*magnitude(elem[0]) + 2 * magnitude(elem[1])
    return elem


current = input[0]
for l in input[1:]:
    current = reduce(add(current, l))


print("part 1:", magnitude(current))

m = 0
for i in input:
    for j in input:
        if i == j:
            continue
        x = magnitude(reduce(add(i, j)))
        y = magnitude(reduce(add(j, i)))
        m = max(m, x, y)

print("part 2:", m)
