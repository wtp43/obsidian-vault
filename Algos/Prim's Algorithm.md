---
tags: 
- greedy
- mst
- graph
---

>[!Note]
>Greedy Algorithm: Start from one vertex and keep adding edges with the lowest weight until we get a minimum spanning tree
>Complexity: O(E log V)
# Pseudocode
1. Initialize minimum spanning tree with a any vertex
2. Find all edges that connect the tree to new vertices. Add the minimum edge to the tree
3. Repeat step 2 by adding all new edges from the newly connected vertex until we get a minimum spanning tree

# Proof of Optimality (using contradiction)

Suppose there exists a graph G in which Prim's algorithm doesn't return a minimum spanning tree. Then there must have been some particular instant where we went wrong. Before we inserted edge $(x,y)$, $T_{prim}$ consisted of a set of edges that was a subtree of some minimum spanning tree $T_{min}$. Choosing $(x,y)$ took us away from any possible minimum spanning tree.

Then there must be a path $p$ from $x$ to $y$ in $T_{min}$ like in figure *b)*. $p$ must use an edge $(v_1,v_2)$ where $v_1$ is in $T_{prim}$ but $v_2$ is not. $(v_1,v_2)$ must have weight at least that of $(x,y)$ or else Prim's algorithm would have selected it before $(x,y)$. Inserting $(x,y)$ and deleting $(v_1, v_2)$ from $T_{min}$ leaves a spanning tree no larger than before, meaning that Prim's algorithm could not have made a fatal mistake in selecting edge $(x,y)$. Therefore, by contradiction, Prim's algorithm must construct a minimum spanning tree.

# Implementation

## Approach #1: Adjacency Matrix
Complexity O($V^2$) instead of O(VE) since we don't iterate all edges
- dist stores the cost of adding the vertex to the tree
- Keep track of cheapest edge linking very non-tree vertex in the tree
- The cheapest such edge over all remaining no-tree vertices gets added in the next iteration

```python
def prim(graph, start):
	n_vertices = len(graph.get_vertices())
	dist = [math.inf for _ in range(n_vertices)]
	seen = [0 for _ in range(n_vertices)]
	parent = [-1 for _ in range(n_vertices)]
	dist[start] = 0

	u = start
	while (not seen[u]):
		seen[u] = 1
		# update all weights from u to its neighbors (v)
		for v in graph.get_neighbors(u):
			weight = graph.get_weight(u,v)
			if not seen[v] and weight < dist[v]:
				dist[v] = weight
				parent[v] = u

		# find the unvisited vertex with the smallest weighted edge 
		# to iterate from 
		cur_dist = math.inf
		for i in range(n_vertices):
			if not seen[i] and dist[i] < cur_dist:
				cur_dist = dist[i]
				u = i
	
	return parent, dist
```


## Approach #2: Adjacency List + Priority Queue (Heap)
Complexity O(E log V)

1. Start from an arbitrary vertex
2. Heapify all the outgoing edges from the starting vertex
3. Get 

```python
from collections import default dict
import heapq

def prim(graph, start):
	mst = defaultdict(set)
	seen = set([start])
	edges = [(cost, v1, v2) for v1, v2, cost in graph.get_edges(start)]
	total_cost = 0
	
	heapq.heapify(edges)

	while edges:
		cost, v1, v2 = heapq.heappop(edges)
		if v2 not in seen:
			seen.add(v2)
			mst[v1].add(v2)
			total_cost += cost
			for v3, cost in graph.get_neighbors(v2):
				if v3 not in visited:
					heapq.heappush(edges,[v2,v3,cost])
	return mst, total_cost
	
```

>[!example]
>```python
>graph = Graph(directed=False)
>graph.add_edge('A', 'B', 2)
>graph.add_edge('A', 'C', 3)
>graph.add_edge('B', 'C', 1)
>graph.add_edge('B', 'D', 1)
>graph.add_edge('B', 'E', 4)
>graph.add_edge('C', 'F', 5)
>graph.add_edge('D', 'E', 1)
>graph.add_edge('E', 'F', 1)
>graph.add_edge('F', 'G', 1)
>mst, total_cost = prim(graph, 'A')
>
>assert(total_cost==29)
>assert(mst == {'A': set(['B']), 'B': set(['C', 'D']), 
> 				'D': set(['E']), 'E': set(['F']), 
> 				'F': set(['G'])})


![[Pasted image 20221208044247.png]]

## Optimizations
- Suppose we know that the cost for every edge is bounded by U
- Instead of using a priority queue (heap), a bucket sort can be implemented in 


### References
https://bradfieldcs.com/algos/graphs/prims-spanning-tree-algorithm/


