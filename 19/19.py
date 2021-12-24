import math
import itertools
import aoc_util as util
import re
import numpy as np
from collections import deque
from collections import Counter


phi =  np.pi/2
rotX = np.array([[1,0,0],[0,np.cos(phi),-np.sin(phi)],[0,np.sin(phi),np.cos(phi)]])
rotY = np.array([[np.cos(phi),0,np.sin(phi)],[0,1,0],[-np.sin(phi),0,np.cos(phi)]])
rotZ = np.array([[np.cos(phi),-np.sin(phi),0],[np.sin(phi),np.cos(phi),0],[0,0,1]])
dirs = [rotX,rotY,rotZ]

def rotate(v,n):
    z = n%4
    step = n//4
    if step > 0:
        v = dirs[0].dot(v)
    if step > 1:
        v = dirs[0].dot(v)
    if step > 2:
        v = dirs[0].dot(v)
    if step > 3:
        v = dirs[1].dot(v)
    if step > 4:
        v = dirs[1].dot(v)
        v = dirs[1].dot(v)

    for i in range(z):
        v = dirs[2].dot(v)

    return v

def from_str(s):
    return np.array(list(map(int,s[1:-1].split(' '))))

class Scanner:
    def __init__(self):
        self.beacons = {}


    def add_beacon(self,pos_rel_to_scanner: np.array):
        s = set()
        for b_str in self.beacons:
            b = from_str(b_str)
            diff = (b[0]-pos_rel_to_scanner[0], b[1] - pos_rel_to_scanner[1], b[2]-pos_rel_to_scanner[2])
            s.add(str(np.array(diff)))
            self.beacons[b_str].add(str(-np.array(diff)))
        
        s.add('[0 0 0]')
        self.beacons[str(pos_rel_to_scanner)] = s
    
        
def compare_scanners(sc1,sc2):
    for orientation in range(24):
        count = 0
        for b_as_str1 in sc1.beacons:
            for b_as_str2 in sc2.beacons: 
                for beacon_offset_as_str in sc2.beacons[b_as_str2]:
                    if rotate(from_str(beacon_offset_as_str),orientation) in sc1.beacons[b_as_str1]:
                        count += 1
                        if count == 12:
                            return True, orientation
    return False, -1

        # start -> 3*z, then 4th and
        # 1*x
        # 1*x
        # 1*x
        # 1*y
        # 2*y


def rotate_all(v):
    step = 5
    orients = []
    for i in range(4):
        v = dirs[2].dot(v)
        orients.append(v)
    if step > 0:
        v = dirs[0].dot(v)
        for i in range(4):
            v = dirs[2].dot(v)
            orients.append(v)
    if step > 1:
        v = dirs[0].dot(v)
        for i in range(4):
            v = dirs[2].dot(v)
            orients.append(v)
    if step > 2:
        v = dirs[0].dot(v)
        for i in range(4):
            v = dirs[2].dot(v)
            orients.append(v)
    if step > 3:
        v = dirs[1].dot(v)
        for i in range(4):
            v = dirs[2].dot(v)
            orients.append(v)
    if step > 4:
        v = dirs[1].dot(v)
        v = dirs[1].dot(v)
        for i in range(4):
            v = dirs[2].dot(v)
            orients.append(v)

    return orients

    

# for i in range(24):
#     print(rotate([1,2,3],i))

# print(rotate_all([1,2,3]))

day = 19

# get input
with open(f'{day}/{day}.txt', 'r') as f:
    data = f.read().strip().split('\n')  # f.readlines()


# transform the input, apply to every row



data = util.parse_groups(data)

scanners = {}
for i,s in enumerate(data):
    
    beacons = np.array(list(map(lambda l:np.array(list(map(int,l.split(',')))), s[1:])))
    scanners[i] = beacons

beacons = set(tuple(x) for x in scanners[0])
print(beacons)

input()
# solve

remaining = deque(v for k,v in scanners.items() if k != 0)
scanner_poss = list(np.array([0,0,0]))

while len(remaining):
    curr = remaining.pop()
    for orientation in range(24):
        for b in beacons:
            if 

"""
maintain a list of beacons
for scanner in scanners:


"""


"""
for beacon in scanner1:
    for beacon2 in scanner2:
        for orientation in orientations:
            count = 0
            for rel_pos in beacon2.positions:
                if orientation(rel_pos) in beacon.positions:
                    count += 1
                    if count == 11:
                        return True, orientation
"""


