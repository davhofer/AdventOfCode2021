# Day 19
day = 19

# get input
with open(f'{day}/{day}.txt', 'r') as f:
    data = f.read().strip()  # f.readlines()

import re
from collections import deque
from scipy.spatial.transform import Rotation as R
import itertools
import numpy as np
from collections import Counter

def rotation_gen(scanner_list):
    rots = [
        R.from_euler('ZX', [  0,   0], degrees=True),
        R.from_euler('ZX', [  0,  90], degrees=True),
        R.from_euler('ZX', [  0, 180], degrees=True),
        R.from_euler('ZX', [  0, 270], degrees=True),
        R.from_euler('ZX', [ 90,   0], degrees=True),
        R.from_euler('ZX', [ 90,  90], degrees=True),
        R.from_euler('ZX', [ 90, 180], degrees=True),
        R.from_euler('ZX', [ 90, 270], degrees=True),
        R.from_euler('ZX', [180,   0], degrees=True),
        R.from_euler('ZX', [180,  90], degrees=True),
        R.from_euler('ZX', [180, 180], degrees=True),
        R.from_euler('ZX', [180, 270], degrees=True),
        R.from_euler('ZX', [270,   0], degrees=True),
        R.from_euler('ZX', [270,  90], degrees=True),
        R.from_euler('ZX', [270, 180], degrees=True),
        R.from_euler('ZX', [270, 270], degrees=True),
        R.from_euler('YX', [ 90,   0], degrees=True),
        R.from_euler('YX', [ 90,  90], degrees=True),
        R.from_euler('YX', [ 90, 180], degrees=True),
        R.from_euler('YX', [ 90, 270], degrees=True),
        R.from_euler('YX', [270,   0], degrees=True),
        R.from_euler('YX', [270,  90], degrees=True),
        R.from_euler('YX', [270, 180], degrees=True),
        R.from_euler('YX', [270, 270], degrees=True),
    ]
    
    for r in rots:
        yield np.round(r.apply(scanner_list)).astype(int)

# Part 1
scanner_lines = [x.splitlines() for x in data.split('\n\n')]
scanners = {
    int(re.search(r'[0-9]+', x[0]).group(0)):
        np.array([np.array(list(map(int, y.split(','))), dtype=float) for y in x[1:]])
    for x in scanner_lines
}

beacons = set(tuple(x) for x in scanners[0].astype(int))
remaining = deque(v for k,v in scanners.items() if k != 0)
scanner_poss = list(np.array([0,0,0]))

while len(remaining):
    print(len(remaining))
    cur = remaining.pop()
    for rotd in rotation_gen(cur):
        c = Counter()
        for v in beacons:
            c.update(tuple(x) for x in rotd - np.array(v, dtype=int))
        [(diff,count)] = c.most_common(1)
        if count >= 12:
            beacons |= set(tuple(x) for x in rotd - np.array(diff, dtype=int))
            scanner_poss.append(np.array(diff, dtype=int))
            break
    else:
        remaining.appendleft(cur)
        
d19p1 = len(beacons)
print(f'Day 19 Part 1: {d19p1}')

# Part 2
dist = [np.abs(x-y).sum() for x in scanner_poss for y in scanner_poss]
print(max(dist))
d19p2 = max(np.abs(x - y).sum() for x in scanner_poss for y in scanner_poss)
print(f'Day 19 Part 2: {d19p2}')