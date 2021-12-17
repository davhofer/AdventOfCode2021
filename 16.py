import math
import itertools
import aoc_util as util
import re
import numpy as np

day = 16

# get input
with open(f'{day}.txt', 'r') as f:
    input = f.read().strip().split('\n')  # f.readlines()


def decode(packet, start_idx):
    version_numbers = []
    value = 0
    # convert to binary
    if start_idx == 0:
        length = len(packet)*4
        packet = str(bin(int(packet, 16)))
        if packet[:2] == '0b':
            packet = packet[2:]
        l = len(packet)
        for i in range(length-l):
            packet = '0' + packet

    # then

    idx = start_idx
    version = int(packet[idx:idx+3], 2)
    version_numbers.append(version)
    idx += 3
    type_id = int(packet[idx:idx+3], 2)
    # tpye_id to int
    idx += 3

    if type_id == 4:
        nums = ''
        while packet[idx] == '1':
            num = packet[idx+1:idx+5]
            nums += num
            idx += 5
        last_num = packet[idx+1:idx+5]
        idx += 5
        nums += last_num
        value = int(nums, 2)

        return idx, version_numbers, value

    else:
        # operator
        values = []
        if packet[idx] == '0':
            idx += 1
            total_lenth = int(packet[idx:idx+15], 2)
            idx += 15
            end = idx + total_lenth
            # next 15 bits are a numer that represents the total lenght in bits of the subpacktes contained in this

            while idx < end:
                idx, new_versions, new_val = decode(packet, idx)
                version_numbers += new_versions
                values.append(new_val)

        else:

            # next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
            idx += 1
            num_packets = int(packet[idx:idx+11], 2)
            idx += 11
            for _ in range(num_packets):
                idx, new_versions, new_val = decode(packet, idx)
                version_numbers += new_versions
                values.append(new_val)

        if type_id == 0:
            value = sum(values)
        elif type_id == 1:
            value = np.prod(values)
        elif type_id == 2:
            value = min(values)
        elif type_id == 3:
            value = max(values)
        elif type_id == 5:
            value = 1 if values[0] > values[1] else 0
        elif type_id == 6:
            value = 1 if values[0] < values[1] else 0
        else:
            value = 1 if values[0] == values[1] else 0

        return idx, version_numbers, value


# solve
total_vn = 0
ans = 0
for l in input:
    _, version_numbers, value = decode(l, 0)
    #print("val = ", value)
    ans = value
    total_vn += sum(version_numbers)

print("task1:", total_vn)
print("task2:", ans)
