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




# conways game of live?

# matrix functionality:
# count neighbors, apply function to neighbors
# specifiy whether neighbors include diagonals
# specify function/return value based on neighbors, 
# i.e. check condition, or count smth


# flip, rotate, transpose matrices?


# dynamic programming







if __name__ == '__main__':

    with open('test.txt') as f:
        input = f.read().strip().split('\n')

    l = ['14 21 17 24  4', '10 16 15  9 19', '18  8 23 26 20', '22 11 13  6  5', ' 2  0 12  3  7']
    m = parse_matrix(l,' ')
    mapped = map_matrix(m,int)
    print(mapped)