---
tags:
- shortest-path
- greedy-algo
---
- Looks only to the immediate neighbors of a vertex (while Bellman Ford goes through each edge in every iteration)
- Dijkstra's algorithm is a [[Shortest and Longest Path on DAG#Single Source Shortest Path (1 root)|SSSP]] algorithm for graphs with **non-negative edge weights**. However, in the real word, many applications can be modelled as graphs with non-negative weights
- This constraint is imposed to ensure that once a node has been visited, its optimal distance cannot be improved
- Works on graphs with cycles SSSP using [[Topological Sort]]
- 

>[!Intuition]
>Greedy algorithms work because once the next 'node' has been visited, it's optimal distance cannot be improved

# Overview
1. Initialize `dist` array to `math.inf` with `dist[start]=0` 
2. Maintain priority queue (PQ) of key-value pairs `(node index, distance)`
3. Insert `(start,0)` into PQ and loop while PQ is not empty
4. Iterate over all edges outwards from current node and relax each edge appending 


# Implementation

**Complexity:** O(E log V)
- Iterate over all edges  = E
- Building a priority queue of all vertices = log V
# Lazy Dijkstra

- Contains duplicated key-value pairs in the PQ

```python
import heapq

def dijkstra(self, start):
	n = len(self.get_vertices())
	dist = defaultdict(lambda:math.inf)
	prev = defaultdict(lambda:None)
	dist[start] = 0
	seen = set()
	pq = [(start, 0)]
	heapq.heapify(pq)
	while pq:
		index, min_value = heapq.heappop(pq)
		if dist[index] < min_value:
			continue
		seen.add(index)
		for u,v,w in self.get_edges(index):
			new_dist = dist[index] + w
			if new_dist < dist[v]:
				dist[v] = new_dist
				prev[v] = u
				heapq.heappush(pq, (v, new_dist))
	return dist, prev

def find_shortest_path(self, start, end):
	dist, prev = self.dijkstra(start, end)
	path = []
	while end:
		path.append(end)
		end = prev[end]
	if path[-1] != start:
		return None
	path.reverse()
	return path

```

- Optimization: `if dist[index] < min_value: continue`
	- We do not need to check all out-edges from this key-value pair because a previous edge took us to this node faster
- It is possible to have duplicate node indices in the PQ. This is not ideal but inserting a new key-value pair is O(logn) which is faster than searching for the key in the PQ which takes O(n)
	- Ex: (0, 0) ->  (2,5), (1,10) -> (1,1), (1,10)
		- Start at 0. Append neighbors 1 and 2 with their respective weights
		- Continue at node 2 which has the smallest weight 5.
		- Append 2's neighbors which is 1 with weight 1
		- Thus, the PQ contains node 1 twice

# Finding the Optimal Path 

# Eager Dijkstra's Algorithm

# Optimizations
## Heap optimization with [[D-ary Heap]]