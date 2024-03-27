---
dg-publish: false
tags: 
created: ""
---
---
>[!summary]- Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```
Initial complete review of all studied concepts
# Structuring a Solution
### Find a starting point
- Where can I start building the solution
- Can I start from the minimum element?
	- Determine if this starting point passes edge cases
- What algorithms and data structures can I use?
	- 
## Intuition
- Find minimum chunk after k cuts/Minimum group size
	- Binary search on group size then greedily make cuts once group reaches threshold
- 

# Essentials

## Arrays
- If range (inclusive): j-i+1
- If index/position difference: j-i
### Kadane's 
https://leetcode.com/problems/substring-with-largest-variance/solutions/2579146/weird-kadane-intuition-solution-explained/
## Backtracking
### Including or not including
- No for loop needed in each backtrack because there is only two options
	- Take i or don't take i compared to take or don't take for each of remaining numbers
#### Power Set
```python
def subsets(self, nums: List[int]) -> List[List[int]]:
	res = []
	n = len(nums)
	subset = [] 
	def backtrack(i):
		if i == n:
			res.append(subset.copy()) 
			return
		subset.append(nums[i])
		backtrack(i+1)
		subset.pop()
		backtrack(i+1)
	backtrack(0)
	return res  
```
### Picking the element for the current position 
#### Permutations
- Swap first num with all nums after it and backtrack (equivalent to choosing a num for every single position)
```python
def permute(self, nums: List[int]) -> List[List[int]]:ķ        res = []
	n = len(nums) 
	def backtrack(i):
		if i == n-1:
			res.append(nums.copy())
			return
		for j in range(i, n):
			nums[i], nums[j] = nums[j], nums[i]
			backtrack(i+1)
			nums[i], nums[j] = nums[j], nums[i]
	backtrack(0) 
	return res
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
	res = []
	n = len(nums)
	def backtrack(i):
		if i == n-1:
			res.append(nums.copy())
			return
		starting_num = set()
		for j in range(i, n):
			if nums[j] in starting_num:
				continue
			nums[i], nums[j] = nums[j], nums[i]     
			backtrack(i+1)
			nums[i], nums[j] = nums[j], nums[i]     
			starting_num.add(nums[j])

	backtrack(0)
	return res
```
#### Combinations
- build combination by picking a number from (i,n)
- keep track of how many numbers are needed (only backtrack if available numbers is enough for remaining numbers needed)
```python
def combine(self, n: int, k: int) -> List[List[int]]:
	combination, res = [], []

	def backtrack(i, need):
		if need==0:
			res.append(combination.copy())
			return
		
		remain = (n+1) - i  
		available = remain-need

		for j in range(i, i + available + 1):
			combination.append(j)
	return res
```
#### n- queens
- Sets: col, row, neg diag, pos diag
```python
 def solveNQueens(self, n: int) -> List[List[str]]:
	res = []
	col = set()
	posDiag = set()  # (r + c)
	negDiag = set()  # (r - c)
	board = [['.']*n for i in range(n)]

	def backtrack(r):
		if r == n:
			copy = ["".join(row) for row in board]
			res.append(copy)
			return
		for c in range(n):
			if c in col or (r + c) in posDiag or (r - c) in negDiag:
					continue
			col.add(c)
			posDiag.add(r + c)
			negDiag.add(r - c)
			board[r][c] = "Q"

			backtrack(r + 1)

			col.remove(c)
			posDiag.remove(r + c)
			negDiag.remove(r - c)
			board[r][c] = "."

		
	backtrack(0)
	return res
```
### Paths
- Manhattan Distance: abs distance between start and destination 
```python
def uniquePathsIII(self, grid: List[List[int]]) -> int:
	m,n = len(grid), len(grid[0])
	squares = 0
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				start = (i,j)
			elif grid[i][j] == 2:
				end = (i,j)
			if grid[i][j] != -1:
				squares += 1
	visited = set([start])
	squares-= 2
	paths = 0
	def backtrack(pos, squares):
		nonlocal paths
		i,j = pos
		if pos == end:
			paths += 1
			return 
		for x,y in [[0,1], [0,-1], [1,0], [-1,0]]:
			new_x = j+x
			new_y = i+y
			new_pos = (new_y, new_x)
			if new_pos in visited or new_x < 0 or new_x >= n or new_y < 0 or new_y >= m or grid[new_y][new_x] == -1: 
				continue
			if new_pos == end and squares > 0:
				continue
			manhattan_distance = abs(end[0] - new_pos[0]) + abs(end[1] - new_pos[1])
			if squares < manhattan_distance - 1:
				continue
			visited.add(new_pos)
			backtrack(new_pos, squares-1)
			visited.remove(new_pos)
	backtrack(start, squares) 
	return paths
```
### 0-1 Knapsack

## Binary Search

> [!danger] Intuition
> Determine whether left or right bisect is needed. This is relevant for questions where more than one 'target' or 'x' can satisfy the conditions (but do we want the biggest 'target' or smallest 'target'). The 'target' to be searched is usually found on some range (which is sorted by default).

### Bisect Process
- What is the target?
- If the target is >= threshold, should we decrease or increase mid?
- Do we want to return hi or lo?
	- Depends on if we want rightmost x or leftmost x


### Bisect left/right
- Implementation differs only at the comparison
```python
#### MORE USEFUL IMPLEMENTATION than <= while
def bisect_left(arr, x):
	lo = 0
	hi = len(arr)-1
	while lo <= hi:
		mid = lo + (hi - lo)//2
		if arr[mid] < x:
			lo = mid + 1
		else:
			hi = mid - 1
	return lo 

lo = first position where arr[lo] > x
hi = position before lo
def bisect_right(arr, x):
	lo = 0
	hi = len(arr)-1
	while lo <= hi:
		mid = lo + (hi - lo)//2
		if arr[mid] <= x:
			lo = mid + 1
		else:
			hi = mid - 1
	return lo 
```

### Framework for using Binary Search to Find Minimum Group Size
#### 
## Binary Trees
### Basic Operations

#### Insert 
```python
def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
	if not root:
		return TreeNode(val)
	if val > root.val:
		root.right = self.insertIntoBST(root.right, val)
	else:
		root.left = self.insertIntoBST(root.left, val)
	return root
 ```
https://leetcode.com/problems/insert-into-a-binary-search-tree/
#### Delete
### Width Type Questions
- ie: check for completeness
- level traversal with BFS

### Traversals
#### Level Order Traversal
- The position of the child node can be calculated with 
	- left child: `pos*2 - 1`
		- right child: `pos*2`
https://leetcode.com/problems/maximum-width-of-binary-tree/description/

#### Zigzag Order Traversal
The ordering of nodes on alternating levels should be reversed
- Use delimiter (ie: None) to indicate end of current level
- Edge case: Empty tree, results in infinite loop
```python
 def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
	res = []
	level = deque([])
	if not root:
		return None
	q = deque([root, None])
	reverse = True
	while q:
		node = q.popleft()
		if node:
			if reverse:
				level.append(node.val)
			else:
				level.appendleft(node.val)
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)
		else:
			res.append(level)
			if q:
				q.append(None)
			level = deque()
			reverse = not reverse
	return res
```
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description
#### Vertical Order Traversal
![[Pasted image 20240304190355.png]]
res:`[[4],[9,5],[3,0,1],[8,2],[7]]` 
- BFS with root set to col 0
- Left child has parent col - 1, right child has parent col + 1
- Since there can't be null cols, we don't have to sort col indices and just 
```python
def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
	col = defaultdict(list)
	if not root:
		return []
	q = deque([(root,0)])
	min_col = max_col = 0

	while q:
		for i in range(len(q)):
			node, i = q.popleft()
			col[i].append(node.val)
			min_col = min(min_col, i)
			max_col = max(max_col, i)

			if node.left:
				q.append((node.left, i-1))
			if node.right:
				q.append((node.right, i+1))
	# Note there cannot be null cols because of the way 
	# col is built
	return [col[i] for i in range(min_col, max_col+1)]
```
#### Vertical Order Traversal Sorted
- A row value is used to determine order for nodes with duplicate values
- Two types of sorting:
	- Global Sorting: O(NlogN)
	- Partition Sorting (Sort each column): O(Nlog(N/k))
	
```python
def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
	if root is None:
		return []

	col = defaultdict(list)
	min_col= max_col= 0

	q = deque([(root, 0, 0)])

	while q:
		node, r, c = q.popleft()

		if node is not None:
			# sort by row first
			col[c].append((r, node.val))
			min_col= min(min_col, c)
			max_col= max(max_col, c)
			q.append((node.left, r+1, c-1))
			q.append((node.right, r+1, c+1))
	
	res = []
	for c in range(min_col, max_col+ 1):
		# partition sort
		res.append([val for row, val in sorted(col[c])])
	return res
```
## Data Structures
- LFU/LRU cache
## Dynamic Programming
### String Matching
#### Prefix Function KMP
#### Rabin Karp
## Graph Theory
- Be smart about where valid solutions can start
### Trees
**Theorem**: An undirected graph is a tree iff it is minimally connected.
The following are equivalent
- A tree is an undirected graph G = (V, E) that is connected and acyclic.
- All the following are equivalent:
- G is a tree.
- G is connected and acyclic.
- G is minimally connected (removing any edge from G disconnects it.)
- G is maximally acyclic (adding any edge creates a cycle)
- G is connected and |E| = |V| - 1.
### Representation
- Adjacency list: Dictionary, for sparse graphs
- Adjacency Matrix: for dense graphs
### BFS/DFS/IDS
- Level search
- Multi-source
### A* Search
> Requires a heuristic
https://leetcode.com/problems/shortest-path-in-binary-matrix/editorial/

### Island Type Questions
#### Closed Island
+ A closed island cannot have land on the edges of the grid
+ Invalidate the island if any of it's squares on on the edge of a grid
```python
def closedIsland(self, grid: List[List[int]]) -> int:
	seen=set()
	res=0
	m,n = len(grid), len(grid[0])
	def dfs(r,c):
		nonlocal water
		if grid[r][c] == 1:
			return True
		if r == 0 or c == 0 or c == n-1 or r ==m-1:
			return False
		grid[r][c] = 1
		for ro, co in [(0,1), (0,-1), (1,0), (-1,0)]:
			row = ro + r
			col = co + c
			#if (row,col) in seen:
			#    continue
			#seen.add((row,col))
			# can't exit early otherwise not all 0's are marked 
			#if not dfs(row,col):
			#    return False
			water &= dfs(row,col)
		return water 
	for r in range(1,len(grid)-1):
		for c in range(1,len(grid[0])-1):
			# be smart about where to start dfs, corner zeros cannot build a valid island
			if (r,c) not in seen and grid[r][c] == 0:
				water = True
				#seen.add((r,c))
				if dfs(r,c):
					res += 1
				
	return res
```
https://leetcode.com/problems/number-of-closed-islands/description/
### Shortest Path Algorithms
- BFS can be used if weights are the same
- Bellman Ford/Floyd Warshall can find negative cycles
#### Bellman Ford
- SSSP (single source shortest path)
- Works for negative weights
- Relax all edges V-1 times
```python
def bellman_ford(graph, start):
	num_vertices = len(graph.get_vertices())
	edges = graph.get_edges()

	dist = [math.inf for i in range(num_vertices)]
	prev = [None for i in range(num_vertices)]

	dist[start] = 0
	#relax edges |V| - 1 times
	for _ in range(num_vertices - 1):
		for u, v, w in edges:
			new_dist = dist[u] + w
			if new_dist < dist[v]:
				dist[v] = new_dist
				prev[v] = u

	#detect negative cycles
	for u,v,w in edges:
		if dist[u] + w < dist[v]:
			raise NegativeWeightCycleError()
	return dist, prev
```
#### Floyd Warshall
- Shortest path algorithm from any vertex to all other vertices
- Works for negative weights and cycles
```python
def floyd(G):
    dis = [[math.inf] * n for _ in range(n)]
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
        for i in range(n):
            dis[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
```
#### Dijkstra
- SSSP
- Finds the shortest path from the source node to all other nodes 
- The result (shortest path tree) is not guaranteed to be a MST 
- Works for both directed/undirected graphs
- Does not work for negative weights
- Works for graphs with cycles
- O(ElogV)
```python
import heapq

def lazy_dijkstra(self, start):
	n = len(self.get_vertices())
	dist = [math.inf] * n
	prev = [None] * n
	dist[start] = 0
	seen = [0] * n
	pq = [(start, 0)]
	heapq.heapify(pq)
	while pq:
		min_value, index = heapq.heappop(pq)
		if dist[index] < min_value:
			continue
		seen.add(index)
		for u,v,w in self.get_edges(index):
			if seen[v]: 
				continue
			new_dist = dist[index] + w
			if new_dist < dist[v]:
				dist[v] = new_dist
				prev[v] = u
				heapq.heappush(pq, (new_dist, v))
	return dist, prev
```
### Longest Path DAG
- In general, this is NP-Hard, but on a DAG this problem is solvable in O(V+E)
- Topological sort
- Process ordering sequentially
- Multiply edges values by -1 and find shortest path
### Minimum Spanning Tree Algorithms
- MST assumes graphs are inherently undirected
- A minimum cost tree that connects all nodes in the graph
- Does not guarantee the shortest path between two nodes in the original graph

**Theorem**: Let G be a connected, weighted graph. If all edge weights in G are distinct, G has exactly one MST
**Theorem (Cycle Property):** If (x, y) is an edge in G and is the heaviest edge on some cycle C, then (x, y) does not belong to any MST of G. 
**Theorem (Cut Property):** Let (S, V – S) be a nontrivial cut in G (i.e. S ≠ Ø and S ≠ V). If (u, v) is the lowest-cost edge crossing (S, V – S), then (u, v) is in every MST of G.
#### Prim's
Greedy Algorithm
- Start at any vertex
- Repeatedly add the minimum edge that connects the tree to a new vertex
	- If each vertex has at most one edge to another vertex, then we are bounded by V here 
- Complexity: O(E log V) with Priority Queue or  O(E + VlogV) with a Fibonacci Heap

 Implementation in python requires a modification of heapq since it does not provide a decrease-key function
- Typically, no decrease-key function is used and instead just append and invalidate entries later on in which case, the complexity is same as Kruskal's
```python
MST-PRIM(G, w, r)
1  for each u ∈ G.V
2       u.key ← ∞
3       u.π ← NIL
4   r.key ← 0
5   Q ← G.V
6   while Q ≠ Ø
7       u ← EXTRACT-MIN(Q)
8       for each v ∈ G.Adjacent[u]
9           if v ∈ Q and w(u, v) < v.key
10              v.π ← u
11              v.key ← w(u, v)
```
**Using a Binary Heap**
1. The time complexity required for one call to `EXTRACT-MIN(Q)` is `O(log V)` using a min priority queue. The while loop at line 6 is executing total V times.so `EXTRACT-MIN(Q)` is called `V` times. So the complexity of `EXTRACT-MIN(Q)` is `O(V logV)`.
2. The `for` loop at line 8 is executing total `2E` times as length of each adjacency lists is `2E` for an undirected graph. The time required to execute line 11 is `O(log v)` by using the `DECREASE_KEY` operation on the min heap. Line 11 also executes total `2E` times. So the total time required to execute line 11 is `O(2E logV) = O(E logV)`.
3. The `for` loop at line 1 will be executed `V` times. Using the procedure to perform lines 1 to 5 will require a complexity of `O(V)`.
Total time complexity of `MST-PRIM` is the sum of the time complexity required to execute steps 1 through 3 for a total of `O((VlogV) + (E logV) + (V)) = O(E logV)` since `|E| >= |V|`.
**Using a Fibonacci Heap**
1. Same as above.
2. Executing line 11 requires `O(1)` amortized time. Line 11 executes a total of `2E` times. So the total time complexity is `O(E)`.
3. Same as above
So the total time complexity of `MST-PRIM` is the sum of executing steps 1 through 3 for a total complexity of `O(V logV + E + V)=O(E + V logV)`.
**Source**: https://stackoverflow.com/questions/20430740/time-complexity-of-prims-algorithm
##### Implementations
- Adjacency Matrix
- Adjacency List + Priority Queue (Heap)

```python
from collections import default dict
import heapq

edges = [(cost, v1, v2)...]
def prim(edges, start):
	mst = defaultdict(set)
	seen = set([start])
	graph = defaultdict(list) 
	for u,v,cost in edges:
		graph[u].append([v,cost])
		graph[v].append([u,cost])

	total_cost = 0
	heapq.heapify(edges)

	while edges:
		cost, u, v = heapq.heappop(edges)
		# Important: There can be edges with visited nodes in the heap
		if v not in seen:
			seen.add(v)
			mst[u].add(v)
			
			total_cost += cost
			for w, ncost in graph[v]:
				# Update new reachable edges
				if w not in seen:
					heapq.heappush(edges,[ncost,v,w])
	return mst, total_cost
```
#### Kruskal's
- Greedy algorithm
- Repeatedly consider the minimum remaining edge
	- Only add it if the two vertices lie within different trees (to avoid cycles)
- Complexity: O(E log E) with Union-find and sorting edges
##### Implementations
- Union-find to store state of trees 
```python
def kruskal(graph):
	mst = []
	uf = Union_find(graph.get_vertices())
	edges = graph.get_edges()
	# sort edges by cost
	edges.sort(key = lambda x: x[2])
	for u,v,cost in edges:
		# Only add edges that don't create a cycle
		if uf.find(u) != uf.find(v):
			mst.append([u,v,cost])
			uf.union(u,v)
	return mst

mst_weight = sum(t[2] for t in mst)
```
- If we know the upper bound of the cost of edges C, using count sort will allow us to sort in O(E + C), reducing the time complexity to just union-find: O()

#### Prim's vs Kruskal's
- Kruskal's is more efficient on sparse graphs than Prim's algorithm 
- Kruskal's will not provide a valid MST mid algorithm unlike Prim
#### Enumerating all MST's 
- Generate one MST
- Then generate all spanning trees and then filter by cost
	- Generating all spanning trees can be done by setting all edges to cost = 0 and using a MST algorithm
### Tarjan's
### Topological Sort
- Detecting cycles with  DFS 
- Only exists for Directed Acyclic Graphs (DAG)
- An ordering such that for all edges(u,v) u comes before v
#### Modified DFS
- DFS and add nodes in reverse order (append left with deque)
- 3 color nodes: 0 = not visited, 1 = processing, 2 = processing complete
- If a node is visited during processing (not all of it's neighbors have completed processing), this means there is a cycle
```python
def topsort(self,graph):
	vis = defaultdict(lambda: 0)
	ordering = deque()
	for node in graph.get_vertices():
		self.dfs_topsort(graph, node, vis, ordering)
	return ordering

def dfs_topsort(self, graph, node, vis, ordering):
	if vis[node] == 2:
		return 
	if vis[node] == 1:
		raise CycleError
	vis[node] = 1
	for nbor in graph.get_neighbors(node):
		self.dfs_topsort(graph, nbor, vis, ordering)
	ordering.appendleft(node)
	vis[node] = 2
```
#### Kahn's Topological Sort
Find vertices with no incoming edges and removing all outgoing edges from these vertices.

Maintain in-degree information of all graph vertices.
Removing an edge from u to v will decrement ``indegree[u]`` by 1.

If a cycle exists, then not all vertices will be able to achieve an indegree of 0. If the top_order does not have a length of n, then we must have encountered a cycle.
```python
def topsort(edges, n):
	top_order = deque()
	indegree = [0] * n
	adj_list = [[] for _ in range(n)]
	for u,v in edges:
		adj_list[u].append(v)
		indegree[v] += 1

	# Store all the nodes with no incoming edges
	q = deque([i for i in range(n) if indegree[i] == 0])
	while q:
		# extract front of queue
		u = q.popleft()
		# add the current vertex to the tail of the ordering
		top_order.append(u)
		for v in adj_list[u]:
			indegree[v] -= 1
			if indegree[v] == 0:
				q.append(v)
				
	if len(top_order) != n:
		print('Cycle Exists')
	return top_order
```

### Determining Connectivity
 - Bfs/dfs/union find
#### Union Find
- Parameters: 
	- n: number of of elements 
	- parent: array indicating root of component i
		- The value stored here is the index position of the root in the element array, not the actual element itself
	- rank: depth of each component
- Union(x,y) succeeds if x and y are found to have different parents
- Append higher ranked tree to lower ranked tree 
- Optimization: Path compression when finding parents
- No operations are performed on the actual elements
```python
class Union_find:
	def __init__(self,n):
		self.n = n
		self.parent = list(range(n))
		self.rank = [1]*n

	#Path compression used to shorten path to parent O(loglogn)
	def find(self,x):
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	# Union modifies the parent array
	def union(self, x, y):
		px = self.find(x)
		py = self.find(y)
		
		if px == py:
			return
		# bigger parent stays the parent
		if self.rank[px] == self.rank[py]:
			self.parent[px] = py
			self.rank[py] += 1
		elif self.rank[px] < self.rank[py]:
			self.parent[px] = py 
		else:
			SElf.rank[py] = self.rank[px]
```
##### Union-find Applications
- Cycle detection for undirected graphs only
- Longest consecutive sequence: union consecutive numbers
	- Use index of nums for union-find
	- Keep track of seen numbers
	- Union current current component to existing components
```python
def longest_consecutive_sequence(nums):
	d = {}
	uf = union_find(len(nums))
	for i, num in enumerate(nums):
		if num in d:
			continue
		d[num] = i
		if num-1 in d:
			uf.union(i, d[num-1])
		if num+1 in d:
			uf.union(i, d[num+1])
	return max(uf.size) if nums else 0
```
### Strongly Connected Components

### Bridges Algorithm
### Network Flow: Max Flow Algorithms
### Graph Theory Intuition
## Greedy 
## Intervals
### Merge Intervals
```python
 def merge(self, intervals: List[List[int]]) -> List[List[int]]:
	#sort by start
	intervals.sort()
	merged = [intervals[0]]

	for start, end in intervals:
		prev_end = merged[-1][1]
		if start <= prev_end:
			merged[-1][1] = max(end, prev_end)
		else:
			merged.append([start, end])
	return merged
```

## Hashing
## Heaps

### Top K 
#### Top K Frequent Elements
## Linked List
### Deletion node (Recursive/Iterative)
### Reverse Linked List
###  Insert Into a Sorted Circular Linked List
- Step 1: Enumerate all cases (how can the node be inserted)
	- At the tail, in the middle
```python
def insert(self, head: 'Node', insertVal: int) -> 'Node':
	if head == None:
		newNode = Node(insertVal, None)
		newNode.next = newNode
		return newNode

	node = head
	while(node.next != head):
		if node.val <= node.next.val:
			if insertVal >= node.val and insertVal <= node.next.val:
				break
		else:
			if insertVal >= node.val or insertVal <= node.next.val:
				break
		node = node.next 
	
	node.next = Node(insertVal, node.next)
	return head
```

## Queue
### Circular Queue
## Sliding Window
## Sorts
### Bucket/Count Sort
### Cyclic Sort
### Quick Sort
### Quick Select
## Stacks
## Trees
## Trie
- Ex: `trie = {c: {a: {t:{WORD_KEY: 'cat' }}}}` 
- An alternative to class objects can be to set
	- `nodes[WORD_KEY] = word` to indicate a word 
```python

def trieDictionary(words):
	trie = {}
	for w in words:
		node = trie
		for ch in w:
			node = node.setdefault(ch,{})

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.nodes = {}
            
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Inserts a word into the trie.
    def insert(self, word: str) -> None:
        cur = self.root;
        
        for c in word:
            if c not in cur.nodes:
                cur.nodes[c] = TrieNode()
            cur = cur.nodes[c]
            
        cur.isWord = True;

    # Returns if the word is in the trie
    def search(self, word: str) -> bool:
        cur = self.root
        
        for c in word:
            if c not in cur.nodes:
                return False
            cur = cur.nodes[c]
            
        return cur.isWord
    # Returns if there is any word in the trie 
    # that starts with the given prefix. */
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for c in prefix:
            if c not in cur.nodes:
                return False
            cur = cur.nodes[c]
            
        return True
```
### Suffix Array/Tree

## Two Pointers

# Advanced
- Indexed priority queue

## Combinatorics
 
# Behavioural 

https://www.techinterviewhandbook.org/behavioral-interview/
