from collections import defaultdict, deque
import heapq
import math

class Graph:
    def __init__(self, directed=True):
        self.d = defaultdict(dict)
        self.vertices = set()
        self.directed = directed

    def add_vertex(self, v):
        self.vertices.add(v)

    def remove_vertex(self, v):
        self.vertices.remove(v)

    def add_edge(self, v1, v2, weight=1):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        self.d[v1][v2] = weight
        if not self.directed:
            self.d[v2][v1] = weight
        
    def remove_edge(self, v1, v2):
        self.d[v1].pop(v2)
        if not self.d[v1]:
            self.remove_vertex(v1)
        if not self.directed:
            self.d[v2].pop(v1)
            if not self.d[v2]:
                self.remove_vertex(v2)

    def get_weight(self, v1, v2):
        return self.d[v1][v2]

    def get_neighbors(self, v):
        return self.d[v].keys()
        
    def get_edges(self, start=None):
        edges = []
        if start:
            for v in self.d[start]:
                edges.append([start, v, self.d[start][v]])
        else:
            for u in self.d:
                for v in self.d[u]:
                    edges.append([u,v,self.d[u][v]])
        return edges
    
    def multiply_edges_by_neg1(self):
        for u in self.d:
            for v in self.d[u]:
                self.d[u][v] *= -1
    
    def get_vertices(self):
        return self.vertices

    def top_sort(self):
        seen = set([])
        ordering = deque()
        for node in self.get_vertices():
            self.dfs_topsort(node, seen, ordering)
        return ordering

    def dfs_topsort(self, node, seen, ordering):
        if node in seen:
            return 
        seen.add(node)
        for neighbor in self.get_neighbors(node):
            self.dfs_topsort(neighbor, seen, ordering)
        ordering.appendleft(node)
    def sssp(self):
        ordering = self.top_sort()
        cost = [math.inf]*len(ordering)
        cost[ordering[0]] = 0
        for node in ordering:
            for u,v,w in self.get_edges(node):
                cost[v] = min(cost[v], cost[u] + w)
        return cost   
    def dijkstra(self, start):
        n = len(self.get_vertices())
        dist = defaultdict(lambda:math.inf)
        dist[start] = 0
        seen = set()
        pq = [(0, start)]
        heapq.heapify(pq)
        while pq:
            min_value, index = heapq.heappop(pq)
            if dist[index] < min_value:
                continue
            seen.add(index)
            for u,v,w in self.get_edges(index):
                if v in seen:
                    continue
                new_dist = dist[index] + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
            print(pq)
        return dist     

def kruskal(graph):
    class Union_find:
        def __init__(self,n):
            self.n = n
            self.parent = list(range(n))
            self.size = [1]*n

        #Path compression used to shorten path to parent O(loglogn)
        def find(self,x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        #Observe that it is the parents of i,j that are being merged
        def union(self, x, y):
            i = self.find(x)
            j = self.find(y)
            
            if i == j:
                return

            if self.size[i] < self.size[j]:
                self.parent[j] = i
                self.size[i] += self.size[j]
            else:
                self.parent[i] = j
                self.size[j] += self.size[i]
    edges = graph.get_edges()
    n_vertices = len(graph.get_vertices())
    uf = Union_find(n_vertices)
    # sort edges by cost
    edges.sort(key = lambda x: x[2])
    mst = []
    for u,v,cost in edges:
        if uf.find(u) != uf.find(v):
            mst.append([u,v,cost])
            uf.union(u,v)
    return mst
    
example_graph = Graph()
example_graph.add_edge(0, 1, 4)
example_graph.add_edge(0, 2, 7)
example_graph.add_edge(1, 2, 11)
example_graph.add_edge(1, 3, 9)
example_graph.add_edge(1, 5, 20)
example_graph.add_edge(2, 5, 1)
example_graph.add_edge(3, 6, 6)
example_graph.add_edge(3, 4, 2)
example_graph.add_edge(4, 6, 10)
example_graph.add_edge(4, 8, 15)
example_graph.add_edge(4, 7, 5)
example_graph.add_edge(4, 5, 1)
example_graph.add_edge(5, 7, 3)
example_graph.add_edge(6, 8, 5)
example_graph.add_edge(7, 8, 12)
print(example_graph.get_edges())

# mst = kruskal(example_graph)
# weight = sum(t[2] for t in mst)
# mst.sort()
# print(mst, weight)

top_graph = Graph()
top_graph.add_edge(5, 2, 1)
top_graph.add_edge(5, 0, 15)
top_graph.add_edge(2, 0, 5)
# top_graph.add_edge(5, 1, 3)
# top_graph.add_edge(1, 0, 1)
# top_graph.add_edge(4, 1)
# top_graph.add_edge(2, 3)
# top_graph.add_edge(3, 1)

# ordering = top_graph.top_sort()
# print('top_sort ordering:', ordering)
# print('sssp:', top_graph.sssp())


# print(top_graph.get_edges())
# top_graph.multiply_edges_by_neg1()
# print(top_graph.get_edges())
# top_graph.multiply_edges_by_neg1()

print(top_graph.dijkstra(5))

#assert(weight == 29)