class Graph:
    def __init__(self,n):
        self.n = n
        self.edges = {}
        for i in range(n):
            self.edges[i] = []

        self.weights = {}


    def addEdge(self,u,v,directed=True,weight=None):
        # add edge
        self.edges[u].append(v)
        # if there is a weight for the edge, add it to the weights dict
        if weight is not None:
            self.weights[u,v] = weight

        # if edges are not directed, do the same in the other direction
        if not directed:
            self.edges[v].append(u)
            if weight is not None:
                self.weights[v,u] = weight

    # takes a graph, starting node, and a function to execute on every node
    def basic_dfs(self,start:int,function_on_node=None):
        # setup
        self.visited = [False for i in range(self.n)]

        #recursive dfs function
        def rec_dfs(u):
            self.visited[u] = True

            # execute some function on the node
            if function_on_node is not None:
                function_on_node(u,self)

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



    def basic_bfs(self,start:int,function_on_node=None):
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
                function_on_node(u,self)

            # add all neighbors that haven't been visited to queue
            for v in self.edges[u]:
                if not self.visited[v]:
                    queue.append(v)
                    self.visited[v] = True

    def ford_fulkerson(self, source, sink):
        parent = [-1]*self.n

        max_flow = 0