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
	ordering.appendleft(node)```
