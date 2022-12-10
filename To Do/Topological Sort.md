---
title:  "Topological Sort"
tags:

created: 2022-12-10
---

>[!attention]+ Contents
>```toc 
style: number 
min_depth: 1 
max_depth: 6







# Topological Sort
- Orders the vertices on a line such that all directed edges go from left to right
- Such an ordering cannot exist if the graph contains a directed cycle
- Each [[Graph Theory#Directed Acyclic Graphs (DAG)|DAG]] has at least one topological sort, they are not unique

>[!Purpose]
>Gives an ordering where each vertex can be processed before it's successors. This allows us to seek the shortest/longest path from x to y in a DAG

# Implementation

```python
def topsort(self,graph):
	seen = set([])
	ordering = deque()
	for node in graph.get_vertices():
		self.dfs_topsort(node, seen, ordering)
	return ordering

def dfs_topsort(self, graph, node, seen, ordering):
	if node in seen:
		return 
	seen.add(node)
	for neighbor in graph.get_neighbors(node):
		self.dfs_topsort(neighbor, seen, ordering)
	ordering.appendleft(node)
```

## Modified to detect cycles

```python
def topsort(self,graph):
	vis = defaultdict(lambda: 0)
	ordering = deque()
	for node in graph.get_vertices():
		self.dfs_topsort(node, vis, ordering)
	return ordering

def dfs_topsort(self, graph, node, vis, ordering):
	if vis[node] == 2:
		return 
	if vis[node] == 1:
		raise CycleError
	vis[node] = 1
	for neighbor in graph.get_neighbors(node):
		self.dfs_topsort(neighbor, seen, ordering)
	order.appendleft(node)
	vis[node] = 2
```

## Optimizations


## Optimized Complexity

>[!Time Complexity]
>O(V + E)

>[!Space Complexity]
>O(d)



# Related
- [[Cycle Detection in Directed Graphs]]
