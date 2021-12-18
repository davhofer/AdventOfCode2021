import math
import itertools
import aoc_util as util
import re
import graphs

global reach_end
reach_end = 0
class Graph:
    def __init__(self):
        self.edges = {}


        self.weights = {}
        self.nodes = []


    def addEdge(self,u,v,directed=True,weight=None):
        if u not in self.nodes:
            self.nodes.append(u)
        if v not in self.nodes:
            self.nodes.append(v)
        # add edge
        if u not in self.edges.keys():
            self.edges[u] = []
        self.edges[u].append(v)
        # if there is a weight for the edge, add it to the weights dict
        if weight is not None:
            self.weights[u,v] = weight

        # if edges are not directed, do the same in the other direction
        if not directed:
            if v not in self.edges.keys():
                self.edges[v] = []
            self.edges[v].append(u)
            if weight is not None:
                self.weights[v,u] = weight

    # takes a graph, starting node, and a function to execute on every node
    def basic_dfs(self,start,function_on_node=None):
        # setup
        self.visited = {}
        for n in self.nodes:
            self.visited[n] = False
        self.double = ''


        

        #recursive dfs function
        def rec_dfs(u,depth):
            print(depth*'>'+u)
            depth += 1
            if depth == 9:
                return
            global reach_end

            if not u[0].isupper():
                self.visited[u] = True

            # call on outgoing connections
            for v in self.edges[u]:
                if v == 'end':
                    reach_end += 1
                    continue
                if v == 'start':
                    continue
                if not self.visited[v] or self.double == '':
                    self.double = v
                    rec_dfs(v,depth)
                    self.double = ''

            self.visited[u] = False
  
            

        # actually run it
        
        rec_dfs(start,0)

      


day = 12

# get input
with open(f'{day}.txt', 'r') as f:
    input = f.read().strip().split('\n')  # f.readlines()


# transform the input, apply to every row
def apply_to_row(x):

    return x
input = list(map(apply_to_row,input))

g = Graph()
for l in input:
    l=l.split("-")
    g.addEdge(l[0],l[1],False)

target = 'end'
start = 'start'
# solve
#g.basic_dfs('start')

def traverse(a,seen,can_twice):
    if a == 'end':
        return 1
    paths = 0
    for b in g.edges[a]:
        if b.islower():
            if b not in seen:
                paths += traverse(b,seen | {b}, can_twice)
            elif can_twice and b not in {'start', 'end'}:
                paths += traverse(b,seen | {b}, False)
        else:
            paths += traverse(b, seen, can_twice)
    return paths

print(traverse('start',{'start'},True))
#print(reach_end)
