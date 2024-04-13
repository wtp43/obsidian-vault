---
dg-publish: true
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
### Replacing DP
#### Minimize Maximum Difference of Pairs
- we don't need dp here because the minimum difference between two pairs occur next to each in a sorted array
- DP solution:
- Binary search
	- Sort (differences will be minimized)
	- Binary search the maximum difference on range (0, max difference of all pairs)
```python
def minimizeMax(self, nums: List[int], p: int) -> int:
	nums.sort()
	lo = 0
	hi = nums[-1]-nums[0]
	n = len(nums)
	while lo <= hi:
		mid = lo + (hi-lo)//2
		cnt = i = 0
		while i < n-1:   
			if nums[i+1] - nums[i] <= mid:
				cnt += 1
				## skip the 2nd num used in the pair
				i += 1
			i += 1
		if cnt < p:
			lo = mid+1
		else:
			hi = mid-1
	return lo 
	# nLogV + nlogn, V = maximum difference in array,
	# in each step of the binary search (total logV steps)
	# we have to determine how many pairs are valid (n steps)
```


### Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
- O(m+n): Merge both arrays and then binary search
- O(log(m + n)): smart binary search
	https://leetcode.com/problems/median-of-two-sorted-arrays/editorial/
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
#### Closest BST Value to Target
- Specify key for min function
- Traverse to left child if target is smaller than root.val, else go right
```python
def closestValue(self, root: TreeNode, target: float) -> int:
	closest = root.val
	while root:
		closest = min(root.val, closest, key = lambda x: abs(target - x))
		root = root.left if target < root.val else root.right
	return closes
```
### Width Type Questions
- ie: check for completeness
- level traversal with BFS

### Traversals
#### In Order Traversal to Balance BST
- Create sorted array with in order traversal
- Add middle node recursively
```python
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sortedArr = []
        def inorderTraversal(root):
            if not root:
                return None
            inorderTraversal(root.left)
            sortedArr.append(root)
            inorderTraversal(root.right)

        def sortedArrToBST(left, right):
            if left > right:
                return None
            
            mid = (right+left)//2 ## ceil of this also returns another valid balanced tree
            new_root = sortedArr[mid] 
            new_root.left =  sortedArrToBST(left, mid-1)
            new_root.right = sortedArrToBST(mid+1, right) 
            return new_root
        inorderTraversal(root)
        return sortedArrToBST(0, len(sortedArr)-1)
```
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
#### N-ary Tree Level Order
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        traversal = []
        q = [root]
        while q:
            current_layer = []
            traversal.append([])
            for node in q:
                traversal[-1].append(node.val)
                current_layer.extend(node.children)
            q = current_layer
        return traversal
```

### Verify Preorder
https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/editorial/?envType=weekly-question&envId=2024-04-08
- Mono dec. stack
- We can add a smaller number to the stack if we are the left side of the subtree
- Once we reach the right side of the subtree (number is greater than last one on the stack), we need to keep track of the value of the parent
	- New nodes on the right side of the subtree of cannot be smaller than the parent (since we are on the right side)
```python
def verifyPreorder(self, preorder: List[int]) -> bool:
	min_limit = -inf
	stack = []
	
	for num in preorder:
		while stack and stack[-1] < num:
			min_limit = stack.pop()
			
		if num <= min_limit:
			return False
		
		stack.append(num)
	
	return True
```
- Verifying in order is easy: list must be sorted
- Verifying post order: iterate list in reverse
	- pop from stack if we encounter a smaller number than top of stack
		- This means we are now on the left side of the tree, new nodes cannot be greater than this parent value
	- add to stack if we encounter numbers greater than the current (we are in the right side of the tree)
## Data Structures
- LFU/LRU cache
## Dynamic Programming

- Subsequence (the answer contains non adjacent elements) almost always requires DP
```python
def longestPalindromeSubseq(self, s: str) -> int:
	# current letter + longest palindrome subsequence of array of size 1 smaller
	# how to make a palindrome with the current letter:
	# find letter equal to current letter in a[0:i] 
	# dp will be 2 + a[start+1:end-1] or max of subproblems(prefix and suffix with length of 1 smaller)

	n = len(s) 

	dp = [[0]*n for _ in range(n)]

	for end in range(n):
		dp[end][end] = 1
		for start in range(end-1, -1, -1):
			if s[start] == s[end]:
				dp[start][end] =  2 + dp[start+1][end-1]
			else:
				dp[start][end] =max(dp[start][end-1], dp[start+1][end])

	return dp[0][-1]
```

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
	pq = [(0, start)]
	heapq.heapify(pq)
	while pq:
		min_value, index = heapq.heappop(pq)
		if dist[index] < min_value:
			continue
		dist[index] = min_value
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
##### Minimum Time to Visit Disappearing Nodes
https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/
```python
def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
	ans = [math.inf]*n
	pq = [(0,0)]
	graph = defaultdict(list)

	for u,v,w in edges:
		graph[u].append((v,w))
		graph[v].append((u,w))
	while pq:
		u,time = heappop(pq)
		if time >= ans[u]:
			continue
		ans[u] = time
		for v,w in graph[u]:
			if ans[v] < time+w or disappear[v] <= time+w:
				continue
			heappush(pq,(v,time+w))
	for i,x in enumerate(ans):
		if x == math.inf:
			ans[i] = -1
	return ans
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
		if self.rank[px] == self.rank[py]:gg
			self.parent[px] = pygg
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
1. Sort intervals/pairs in increasing order of the start position.
2. Scan the sorted intervals, and maintain an "active set" for overlapping intervals. At most times, we do not need to use an explicit set to store them. Instead, we just need to maintain several key parameters, e.g. the number of overlapping intervals (count), the minimum ending point among all overlapping intervals (minEnd).
3. If the interval that we are currently checking overlaps with the active set, which can be characterized by cur.start > minEnd, we need to renew those key parameters or change some states.
4. If the current interval does not overlap with the active set, we just drop current active set, record some parameters, and create a new active set that contains the current interval.
> [!hint]+ Using Heaps
> Heaps may be helpful in keeping track of interval with earliest end

### Merge Intervals
- Sort by start
- Take the max of each end in the current overlapping interval
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
### Max Overlapping Intervals
https://leetcode.com/problems/meeting-rooms-ii/description/
- Sort by start
- Keep min heap of ending times in current overlapping range
- Pop one room (replace the meeting that is ending first, with the newest meeting, if it is ending),
	- otherwise a new room is needed
```python
def minMeetingRooms(self, intervals: List[List[int]]) -> int:
	intervals.sort()
	rooms = [intervals[0][1]]

	for start, end in intervals[1:]:
		if start >= rooms[0]:
			heappop(rooms)
		heappush(rooms, end)
	return len(rooms)
```

### Scheduling Max Activities/Maximum Number of Events that can be Attended
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/
- Sort by end and take the activity with the earliest end time
- Only add activity to the priority queue if day >= start_time 
	- Sort by start days
	- Take the activity ending on the earliest day from a pool of activities with the same start day
	- Increment day by one after each activity
```python
def maxEvents(self, events: List[List[int]]) -> int:
	sorted_events = deque(sorted(events))
	pq = []
	res = day = 0 

	while sorted_events or pq:
		if not pq: 
			day = sorted_events[0][0]
		while sorted_events and sorted_events[0][0] == day:
			heappush(pq, sorted_events.popleft()[1])
		heappop(pq)
		res += 1
		day += 1
		while pq and pq[0]<day:
			heappop(pq)
	return res
```

## Hashing
## Heaps

### Top K 
#### Top K Frequent Elements
## Linked List
### Deletion node (Recursive/Iterative)
### Reverse Linked List
```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
	prev, cur = None, head
	while cur:
		next_tmp = cur.next
		cur.next = prev
		prev = cur
		cur = next_tmp
	return prev
```
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
### Reverse Nodes in k-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/description/
- Reverse k nodes at a time 
- Count number of k groups first
	- Store the ptr for the last node of group 1
	- This is used to set the next node for the last node of the first group (original root), so that the linked list doesn't break after the first group
- Keep a ptr for the previous node of the group 
- Reverse k nodes
	- Point the previous of the group at the head of the k reversed nodes
	- Point the last node of the current group to the saved tmp(cur.next)
```python
def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
	cur = head
	groups = 0
	c = 0
	first_k = None
	# Find number of groups of size k
	while cur:
		c += 1
		if c == k:
			c = 0
			groups += 1
			if not first_k:
				first_k = cur.next

		cur = cur.next

	cur = head
	dummy =ListNode() 
	group_prev = dummy
	prev = first_k

	while groups > 0:
		c = k
		last_node = cur
		while c > 0:
			tmp = cur.next
			cur.next = prev
			prev = cur
			cur = tmp
			c -= 1
		groups -= 1
	
		group_prev.next = prev
		group_prev = last_node
		last_node.next = tmp
		cur = tmp
	return dummy.next
```
## Queue
### Circular Queue
## Sliding Window
## Sorts
### Bucket/Count Sort
### Cyclic Sort
### Quick Sort
### Quick Select
## Stacks/Monotonic Stacks
>Mono Increasing:
>`while stack and (i == n or arr[i] <) `
- Figure out if a larger or smaller `arr[i]` will invalidate the current sum
- If larger element invalidates stack:
	- mono dec. stack
- else:
	- mono inc. stack
### Monotonically Increasing Stack
- The area of the rectangle with height at `stack[-1]` cannot grow if the current bar is smaller
	- Thus, a mono. increasing stack is required
#### Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/description/
- Trick: Append index -1 to the start of the stack for the left border of the 0th bar
```python
 def largestRectangleArea(self, heights: List[int]) -> int:
	stack = [-1]
	area = 0
	n = len(heights)
	# monotonically increasing stack
	for i in range(n+1):
		# when the stack is empty (left boundary is -1), this means that every previous
		# bar was taller than this one
		while stack[-1] != -1 and (i == n or heights[i] <= heights[stack[-1]]):
			# height of the last bar in the stack
			h = heights[stack.pop()]
			# stack[-1] is the left boundary, the next highest bar in the stack
			# before the bar with height = h
			w = i-stack[-1] - 1
			area = max(area, h*w)
		if i < n:
			stack.append(i)
	return area
```
### Monotonically Decreasing Stack

#### Sliding Window Maximum
- Mono dec. stack while invalidating the max
- Invalidate the max (which is at `q[0]`) if it is not within the k sized window
- Invalidate elements on the stack smaller than the current element (since they will never be used)
```python
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
	q = deque([])

	# what would invalidate the ans
	# the maximum value is out of range
	# if the current number is not the max, 
	# it will never be used
	i = 0
	n = len(nums)
	ans = []
		
	for i in range(k-1):
		while q and nums[i] > nums[q[-1]]:
			q.pop()
		q.append(i)
	for i in range(k-1, n):
		# invalidate stack
		while q and nums[i] > nums[q[-1]]:
			q.pop()
		while q and i-k >= q[0]:
			q.popleft()
		q.append(i)
		ans.append(nums[q[0]])
	return ans
```

#### Number of Subarrays where Boundary Elements are Maximum
https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/
- Stack is invalidated if a greater element is encountered
```python
def numberOfSubarrays(self, nums: List[int]) -> int:
	ans = 0
	stack = []
	n = len(nums)
	d = defaultdict(int)
	for i in range(n):
		while stack and nums[i] > nums[stack[-1]]:
			d[nums[stack[-1]]] -= 1
			stack.pop()
		ans += d[nums[i]]
		stack.append(i)
		d[nums[i]] += 1
	return ans + n
```
## String
### Pattern Matching
#### Maximal Boundaries
- Maximal boundary is longest prefix that is also a suffix
- F is an array of maximal boundaries for every substring `s[0:i] for i in range(len(s))`
```python
def maximum_border_length(w):
	n = len(w)
	f = [0] * n # init f[0] = 0
	k = 0 # current longest border length
	for i in range(1, n): # compute f[i]
		while w[k] != w[i] and k > 0:
			k = f[k - 1] # mismatch: try the next border
		if w[k] == w[i]: # last characters match
			k += 1 # we can increment the border length
			f[i] = k # we found the maximal border of w[:i + 1]
	return f
```

#### KMP
- Search t in s
```python
def KMP(s, t):
	w = t + "#" + s
	n = len(w)
	f = [0] * n # init f[0] = 0
	k = 0 # current longest border length
	for i in range(1, n): # compute f[i]
		while w[k] != w[i] and k > 0:
			k = f[k - 1] # mismatch: try the next border
		if w[k] == w[i]: # last characters match
			k += 1 # we can increment the border length
			f[i] = k # we found the maximal border of w[:i + 1]
			if f[i] == n:
				return i - 2*n #2n accounts for the searched word, -1 omitted for the separator used
	return f
```
Space/Time Complexity: O(m + n)

### Isomorphic Strings (Mapping)
```python
def isIsomorphic(self, s: str, t: str) -> bool:
	map_s = {}
	map_t = {}
	for c1, c2 in zip(s,t):
		if c1 not in map_s and c2 not in map_t:
			map_s[c1] = c2
			map_t[c2] = c1
		elif map_s.get(c1) != c2 or map_t.get(c2) != c1:
			return False
	return True
```

## Sweep Line
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
