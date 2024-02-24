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
# Essentials

## Arrays
- Kadane's Algorithm
### Array Manipulation
#### Ranges vs Counting
- If range: j-i+1
- else: j-1
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
			backtrack(j+1, need-1)
			combination.pop()
	backtrack(1, k)
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
### Bisect left/right
## Data Structures
- LFU/LRU cache
## Dynamic Programming
### String Matching
#### Prefix Function KMP
##### sdflkjsdf 
sdfsdf
#### Rabin Karp
## Graph Theory
- Be smart about where valid solutions can start
### Representation
- Adjacency list: Dictionary, for sparse graphs
- Adjacency Matrix: for dense graphs
### BFS/DFS/IDS
- Level search
- Multi-source
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
#### Bellman Ford/Floyd Warshall
#### Dijkstra

### Minimum Spanning Tree Algorithms
#### Prim/Kruskal

### Topological Sort
- Detecting cycles with  DFS 
#### Directed Acyclic Graphs (DAG)
- Topological sorting is the most important operation on DAG's
### Determining Connectivity
 - Bfs/dfs/union find
#### Union Find
### Strongly Connected Components

### Bridges Algorithm
### Network Flow: Max Flow Algorithms
### Graph Theory Intuition
## Greedy 
## Intervals
## Hashing
## Heaps

### Top K 
#### Top K Frequent Elements
## Linked List
### Deletion node (Recursive/Iterative)
### Reverse Linked List

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
## Tries

### Suffix Array/Tree

## Two Pointers

# Advanced
- Indexed priority queue
## Combinatorics
 
# Behavioural 

https://www.techinterviewhandbook.org/behavioral-interview/
