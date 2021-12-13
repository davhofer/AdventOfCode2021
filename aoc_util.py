"""

PARSING SPECIAL INFORMATION
if there is specific information in the first lines, consider copying it by hand
e.g. first three lines are:
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

=> then do it by hand =>
class = [0,1] + list(range(4,20))
row = list(range(6)) + list(range(8,20))
...


UTIL/PARSING
use util to process the input
groups = util.parse_groups(input)
matrices = list(map(lambda x: util.parse_matrix(x,',',int),groups))
matrices = util.map_matrix(matrices,lambda x: x+1)

REGEX
use regex to find a pattern in a string:
s = "Advent of Code. list[4] is the 5th item of list!"
re.findall(r'[a-z]+\[[0-9]+\]',s)
returns: ['list[4]']

BINARY
bin to int:
i = int('100110',2)
int to bin:
b = bin(256)
or
b = format(256,'b') 

HEX
hex to int
i = int('100',16)
int to hex
h = hex(256)



DYNAMIC PROGRAMMING
what are the problem variables? which variables model a current state?
what is the recursion/recurrence relation? how do we get from one state to its neighboring states?
what are the base cases
implement recursively or iteratively
add memoization


"""

def parse_groups(input):
    # takes a list of lines as input, returns a list of lists of lines,
    # grouped by/separated by empty lines
    l = []
    ll = [input[0]]
    for x in input[1:]:
        if x == '':
            l.append(ll)
            ll = []
        else:
            ll.append(x)
    l.append(ll)
    return l

def non_empty(s):
    return s != ''

def parse_matrix(input,separator,apply_to_items=lambda x: x):
    if separator == '':
        split = lambda l: list(l)
    else:
        split = lambda l: filter(non_empty,l.split(separator))
    return list(map(lambda l: list(map(apply_to_items,split(l))),input))


def map_matrix(matrix,f):
    return list(map(lambda row: list(map(f,row)),matrix))

def print_matrix(matrix):
    for row in matrix:
        print(row)

def neighbors(x,y,size_x,size_y,corners = True):
    n = []
    for i in range(-1,2):
        for j in range(-1,2):
            # to exclude self:
            if i == 0 and j == 0:
                continue
            # out of bounds checking
            if x+i < 0 or y+j < 0 or i+x>= size_x or y+j >= size_y:
                continue
            # to excude corners:
            if not corners and abs(i+j) != 1:
                continue
            n.append((x+i,y+j))
    return n

# conways game of live?

# matrix functionality:
# count neighbors, apply function to neighbors
# specifiy whether neighbors include diagonals
# specify function/return value based on nSeighbors, 
# i.e. check condition, or count smth



# TODO:
# flip, rotate, transpose matrices


def points_to_matrix(points):
    X = 0
    Y = 0
    for (x,y) in points:
        X = max(X,x)
        Y = max(Y,y)
    m = [[0 for i in range(X)] for j in range(Y)]
    for (x,y) in points:
        m[y][x] = 1
    return m

def matrix_to_points(matrix):
    points = set([])
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if matrix[y][x] == 1:
                points.add((x,y))
    return points

def flip_matrix(axis,matrix):
    n = len(matrix)
    m = []    
    if axis=='y':
        for i in range(n):
            m.append(matrix[n-i-1])
        return m

    if axis=='x':
        for row in matrix:
            m.append(list(reversed(row)))
    return m

def split_matrix_at(idx,axis,matrix,include_idx=False):
    m1 = []
    m2 = []
    middle = idx if include_idx else idx+1
    if axis=='y':
        m1 = matrix[:idx]
        m2 = matrix[middle:]
        

    if axis=='x':
        for row in matrix:
            m1.append(row[:idx])
            m2.append(row[middle:])

    return (m1,m2)



# dynamic programming







if __name__ == '__main__':

    with open('test.txt') as f:
        input = f.read().strip().split('\n')

    l = ['1 1 1 2 2', '0 1 0  1 0', '1  1 0 0 0', '1 0 0  1  1', ' 1 2 3  4  5']
    m = parse_matrix(l,' ')
    mapped = map_matrix(m,int)
    print_matrix(mapped)

    print()
    print()
    print_matrix(flip_matrix('x',mapped))
    
    print()
    print()
    print_matrix(flip_matrix('y',mapped))

    print()
    print()
    print_matrix(split_matrix_at(2,'x',mapped)[0])
    print()
    print_matrix(split_matrix_at(2,'x',mapped)[1])

    print()
    print()
    print("Neighbors")
    print(neighbors(1,1,4,4,False))

 