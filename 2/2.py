import math 
import itertools 

# TODO: adjust day
#input("HAVE YOU ADJUSTED THE DAY?")

day = 2

# get input
with open(f'{day}.txt','r') as f:
    input = f.readlines()


print(input[-1])

ans = 0
x = 0
depth = 0
aim = 0

# process input
for l in input:
    dir = l.split(' ')[0]
    dist = int(l.split(' ')[1])
    if dir == 'forward':
         x += dist
         depth += aim*dist
    elif dir == 'down':
         aim += dist
    if dir == 'up':
        aim -= dist


# solve problem






print(x*depth)