# solution for 1: last two variables in last line should be a
# solution for 2: last two variables in last line should be b
l = list
a = l(map(int, open('1').readlines()))
b = l(map(lambda x, y, z: x+y+z, a, a[1:], a[2:]))
x = b
print(sum(map(lambda x, y: 1 if x < y else 0, x, x[1:])))


# for task 2, change l = a to l = b
a = [*map(int, open('1').readlines())]
b = [*map(lambda x, y, z: x+y+z, a, a[1:], a[2:])]
l = b
print(sum(x < y for x, y in zip(l, l[1:])))
