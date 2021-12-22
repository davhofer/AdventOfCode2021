import math 
import itertools 

day = 1

# get input
with open(f'{day}.txt','r') as f:
    input = f.readlines()

ans = 0
# process input
prev = int(input[0]) + int(input[1]) + int(input[2])
for i in range(4,len(input)+1):
    sum = int(input[i-3]) + int(input[i-2]) + int(input[i-1])
    if sum > prev:
        ans += 1
    prev = sum


# solve problem



print(ans)