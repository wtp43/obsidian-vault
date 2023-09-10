---
dg-publish: true
tags:
- graph
- dfs
- union-find
- connected-components
---
# Approach #1: [[DFS]]

```python
n = len(graph.get_vertices())
seen = [0]*n
components = [0]*n
count = 0

def findComponents(n):
	global count
	for i in range(n):
		if not seen[i]:
			count += 1
			dfs(graph, i)

def dfs(graph, at):
	seen.add(at)
	components[at] = count
	for next in graph[at]:
		if not seen[i]:
			dfs(graph, next)
```

- DFS is asymptotically faster than union-find but is best suited for static graphs where no new edges will added

# Approach #2: [[Union Find (Disjoint Sets)]]
- Union-find is more useful if the graph isn't in memory or the graph is dynamic