import math
import itertools
import aoc_util as util
import re

"""
#############
#...........#
###C#A#B#D###
  #D#C#A#B#
  #########

"""

day = 23


nrg = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000
}
home = {
    "A": (11, 12),
    "B": (13, 14),
    "C": (15, 16),
    "D": (17, 18)
}
room_nothome = {
    "A": (13, 14, 15, 16, 17, 18),
    "B": (11, 12, 15, 16, 17, 18),
    "C": (11, 12, 13, 14, 17, 18),
    "D": (11, 12, 13, 14, 15, 16)
}


def n(a, b, dist):
    neighbors[a].add((b, dist))
    neighbors[b].add((a, dist))


nodes = ["" for i in range(19)]
neighbors = {}
for i in range(19):
    neighbors[i] = set()

for i in range(10):
    n(i, i+1, 1)

neighbors[1].add((11, 2))
neighbors[3].add((11, 2))
neighbors[11].add((2, 1))
n(11, 12, 1)

neighbors[3].add((13, 2))
neighbors[5].add((13, 2))
neighbors[13].add((4, 1))
n(13, 14, 1)
neighbors[5].add((15, 2))
neighbors[7].add((15, 2))
neighbors[15].add((6, 1))
n(15, 16, 1)
neighbors[7].add((17, 2))
neighbors[9].add((17, 2))
neighbors[17].add((8, 1))
n(17, 18, 1)


# DP["","","","A","B","","",...] = "the least amount of energy it took to reach this situation"
DP = {}


def is_hallway(i):
    return i in range(11)


def is_home(i, amph):
    return i in home[amph]


def outside(orig, dest):
    return (orig in (11, 12) and dest == 2) or (orig in (13, 14) and dest == 4) or (orig in (15, 16) and dest == 6) or (orig in (17, 18) and dest == 8)


def dp(nodes: tuple):
    if nodes in DP:
        return DP[nodes]
    can_happen = False
    scores = []
    for i in range(len(nodes)):
        amph = nodes[i]
        if amph != "":
            for j, dist in neighbors[i]:
                if nodes[j] != "" or outside(j, i) or (i in room_nothome[amph] and not j == i+1) or ((i in [11, 13, 15, 17]) and is_home(i, amph) and nodes[i+1] != "" and nodes[i+1] != amph) or (is_hallway(i) and is_hallway(j)):
                    continue
                orig_state = [nodes[i] for i in range(len(nodes))]
                orig_state[j] = amph
                orig_state[j] = ""
                orig_state = tuple(orig_state)
                can_happen = True
                score = dp(orig_state) + dist * nrg[amph]
                scores.append(score)

    if not can_happen:
        DP[nodes] = 100000000000000
        return 100000000000000

    DP[nodes] = min(scores)
    return DP[nodes]


"""
#############
#...........#
###C#A#B#D###
  #D#C#A#B#
  #########

A: 
"""
# test
DP["", "", "", "", "", "", "", "", "", "", "",
    "B", "A", "C", "D", "B", "C", "D", "A"] = 0

# prod
# DP["", "", "", "", "", "", "", "", "", "", "",
#     "C", "D", "A", "C", "B", "A", "D", "B"]


final = ("", "", "", "", "", "", "", "", "", "",
         "", "A", "A", "B", "B", "C", "C", "D", "D")


print(dp(final))
