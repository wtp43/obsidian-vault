---
dg-publish: true
tags:
- shortest-path
- longest-path
- dag
- topological-sort
---
# Single Source Shortest Path (1 root)
- Can be solved efficiently on a DAG in O(V + E) time 
	- Use [[Topological Sort]] then process sequentially
- Works for negative weights
# Implementation
```python
def sssp(self):
	ordering = self.top_sort()
	cost = [math.inf]*len(ordering)
	cost[ordering[0]] = 0
	for node in ordering:
		for u,v,w in self.get_edges(node):
			print(u,v,w)
			cost[v] = min(cost[v], cost[u] + w)
			print(cost[v])
	return cost	
```


# Longest Path on a DAG
- In general, this is NP-Hard, but on a DAG this problem is solvable in O(V+E)
>[!Trick]
>Multiply all edge values by -1 then find the shortest path and then multiply the edge values by -1 again

```python
def multiply_edges_by_neg1(self):
	for u in self.d:
		for v in self.d[u]:
			d[u][v] *= -1
def longest_path_dag(self):
	self.multiply_edges_by_neg1()
	self.sssp()
	self.multiply_edges_by_neg1()
```



# Related
[[Graph Theory#Directed Acyclic Graphs (DAG)]]