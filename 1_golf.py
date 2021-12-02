l=list
a=l(map(int,open('1').readlines()))
b=l(map(lambda x,y,z:x+y+z,a,a[1:],a[2:]))
print(sum(map(lambda x,y:1 if x<y else 0,a,a[1:])))

# solution for 1: last two variables in last line should be a
# solution for 2: last two variables in last line should be b


# for task 2, change l = inp to l = part2
input = list(map(int,open('1').readlines()))

part2 = list(map(lambda x,y,z: x+y+z, input, input[1:], input[2:]))

l = part2

print(sum(map(lambda x,y: x<y, l, l[1:])))



