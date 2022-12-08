>[!note]
>Union Find stores the index of each element's parent 

## Union Find Optimizations

- Keep track of size to keep balanced trees
- Path compression when finding parents

## Disjoint Sets to find longest consecutive sequence in a set


```python
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
			self.parent[i] = self.parent[j]
			self.size[j] += self.size[i]
```

```python
def longest_consecutive_sequence(arr):
	seen = {}
	uf = union_find(len(nums))
	for i, num in enumerate(arr):
		if num in d:
			continue
		d[num] = i
		if num-1 in d:
			uf.union(i, d[num-1])
		if num+1 in d:
			uf.union(i, d[num+1])
	return max(uf.size) if nums else 0
```

## Cycle Detection for Undirected Graphs

- UF does not work for directed graphs
- Create UF for number of vertices
- Iterate through all edges and if two vertices have the same parent, there must be a cycle

```python
def isCyclic(edges,num_vertices):
    uf = union_find(num_vertices)
    for x,y in edges:
        if uf.find(x) == uf.find(y):
            return True
        uf.union(x,y)
	return False

```