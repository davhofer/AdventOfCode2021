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


def parse_rec_list(line, idx):
    if line[idx] != '[':
        return ''
    idx += 1

    items = []
    open = 0
    while idx < len(line):
        if line[idx] == '[':

            item, idx = parse_rec_list(line, idx)
            items.append(item)
        elif line[idx] in list("1234567890"):
            num = line[idx]
            idx += 1
            while line[idx] in list("1234567890"):
                num += line[idx]
                idx += 1
            num = int(num)
            items.append(num)
        elif line[idx] == ',':
            idx += 1
        elif line[idx] == ']':
            idx += 1
            return items, idx
        else:
            print("Bad character encountered:", line[idx])
    idx += 1
    return items, idx


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


def parse_matrix(input, separator, apply_to_items=lambda x: x):
    if separator == '':
        def split(l): return list(l)
    else:
        def split(l): return filter(non_empty, l.split(separator))
    return list(map(lambda l: list(map(apply_to_items, split(l))), input))


def map_matrix(matrix, f):
    return list(map(lambda row: list(map(f, row)), matrix))


def print_matrix(matrix):
    for row in matrix:
        print(row)


def neighbors(x, y, size_x, size_y, corners=True):
    n = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            # to exclude self:
            if i == 0 and j == 0:
                continue
            # out of bounds checking
            if x+i < 0 or y+j < 0 or i+x >= size_x or y+j >= size_y:
                continue
            # to excude corners:
            if not corners and abs(i+j) != 1:
                continue
            n.append((x+i, y+j))
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
    for (x, y) in points:
        X = max(X, x)
        Y = max(Y, y)
    m = [[0 for i in range(X)] for j in range(Y)]
    for (x, y) in points:
        m[y][x] = 1
    return m


def matrix_to_points(matrix):
    points = set([])
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if matrix[y][x] == 1:
                points.add((x, y))
    return points


def flip_matrix(axis, matrix):
    n = len(matrix)
    m = []
    if axis == 'y':
        for i in range(n):
            m.append(matrix[n-i-1])
        return m

    if axis == 'x':
        for row in matrix:
            m.append(list(reversed(row)))
    return m


def split_matrix_at(idx, axis, matrix, include_idx=False):
    m1 = []
    m2 = []
    middle = idx if include_idx else idx+1
    if axis == 'y':
        m1 = matrix[:idx]
        m2 = matrix[middle:]

    if axis == 'x':
        for row in matrix:
            m1.append(row[:idx])
            m2.append(row[middle:])

    return (m1, m2)


# run dijkstra given a matrix of the weights for going to node i,j
def dijkstra_matrix(matrix, start, end, diagonal_edges=False):
    import heapq
    n = len(matrix)
    m = len(matrix[0])
    edges = {}
    weights = {}
    for y in range(n):
        for x in range(m):
            weights[x, y] = matrix[y][x]
            if (x, y) not in edges:
                edges[x, y] = set()
            for i, j in neighbors(x, y, m, n, diagonal_edges):
                edges[x, y].add((i, j))

    dist = {u: 1000000 for u in edges}
    dist[start] = 0

    Q = [(0, start)]

    while Q:
        d, u = heapq.heappop(Q)

        for v in edges[u]:
            new_d = dist[u] + weights[v]
            if new_d < dist[v]:
                dist[v] = new_d
                heapq.heappush(Q, (new_d, v))
            if end != None and dist[end] < 1000000:
                return dist[end]
    if end != None:
        return dist[end]
    return dist

# dynamic programming


class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = {}
        for i in range(n):
            self.edges[i] = []

        self.weights = {}

    def addEdge(self, u, v, directed=True, weight=None):
        # add edge
        if u not in self.edges.keys():
            self.edges[u] = []
        self.edges[u].append(v)
        # if there is a weight for the edge, add it to the weights dict
        if weight is not None:
            self.weights[u, v] = weight

        # if edges are not directed, do the same in the other direction
        if not directed:
            if v not in self.edges.keys():
                self.edges[v] = []
            self.edges[v].append(u)
            if weight is not None:
                self.weights[v, u] = weight

    # takes a graph, starting node, and a function to execute on every node
    def basic_dfs(self, start: int, function_on_node=None):
        # setup
        self.visited = [False for i in range(self.n)]

        # recursive dfs function
        def rec_dfs(u):
            self.visited[u] = True

            # execute some function on the node
            if function_on_node is not None:
                function_on_node(u, self)

            # call on outgoing connections
            for v in self.edges[u]:
                if not self.visited[v]:
                    rec_dfs(v)

        # actually run it
        rec_dfs(start)

        for v in self.visited:
            if not v:
                return False
        return True

    def basic_bfs(self, start: int, function_on_node=None):
        # setup
        self.visited = [False for i in range(self.n)]

        # prepare queue
        queue = []

        queue.append(start)
        self.visited[start] = True

        # while queue is not empty
        while queue:

            # get first item
            u = queue.pop(0)

            # execute some function on the node
            if function_on_node is not None:
                function_on_node(u, self)

            # add all neighbors that haven't been visited to queue
            for v in self.edges[u]:
                if not self.visited[v]:
                    queue.append(v)
                    self.visited[v] = True

    def dijkstra(self, start, end):
        import heapq

        dist = {u: 1000000 for u in range(self.n)}
        dist[start] = 0

        Q = [(0, start)]

        while Q:
            d, u = heapq.heappop(Q)

            for v in self.edges[u]:
                new_d = dist[u] + self.weights[u, v]
                if new_d < dist[v]:
                    dist[v] = new_d
                    heapq.heappush(Q, (new_d, v))
                if end != None and dist[end] < 1000000:
                    return dist[end]
        if end != None:
            return dist[end]

        return dist

    def ford_fulkerson(self, source, sink):
        parent = [-1]*self.n

        max_flow = 0


if __name__ == '__main__':

    l = "[[[[1,2],[3,4]],[[5,6],[7,8]]],9]"
    print(parse_list(l, 0)[0])
    # with open('test.txt') as f:
    #     input = f.read().strip().split('\n')

    # l = ['1 1 1 2 2', '0 1 0  1 0', '1  1 0 0 0', '1 0 0  1  1', ' 1 2 3  4  5']
    # m = parse_matrix(l, ' ')
    # mapped = map_matrix(m, int)
    # print_matrix(mapped)

    # print()
    # print()
    # print_matrix(flip_matrix('x', mapped))

    # print()
    # print()
    # print_matrix(flip_matrix('y', mapped))

    # print()
    # print()
    # print_matrix(split_matrix_at(2, 'x', mapped)[0])
    # print()
    # print_matrix(split_matrix_at(2, 'x', mapped)[1])

    # print()
    # print()
    # print("Neighbors")
    # print(neighbors(1, 1, 4, 4, False))
