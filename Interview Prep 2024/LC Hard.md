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
# LC Hard
## Backtrack
#### Build sentence by inserting spaces into string given dictionary of valid words
+ Approach #1: Check index of i,j to see if it is a word that belongs in dictionary while backtracking
+ Approach #2: Loop through every valid word. Check if i:i+len(word)+1 is equal to the word
```python
def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
	res = []
	n = len(s)
	cur = []
	start = set()
	for word in wordDict:
		start.add(word[0])
	word = ''
	def backtrack(i,j):
		nonlocal word, cur
		if i >= n:
			res.append(' '.join(cur))
			return
		if j >= n:
			return
		if s[i] not in start:
			return
		word += s[j]
		if word in wordDict:
			cur.append(word)
			tmp = word
			word = ''
			backtrack(j+1, j+1)
			word = tmp
			cur.pop()
		backtrack(i, j+1) 
	backtrack(0,0)
	return res
```
https://leetcode.com/problems/word-break-ii/description/

## Trie

```python
def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
	res = []
	m,n = len(board), len(board[0])
	trie = {} 
	WORD_KEY = '$$'
	VISITED = '=='

	def find(word):
		node = trie
		for c in word:
			if c in node:
				node = node[c]
			else:
				return False
		return node[WORD_KEY] == word 

	for word in words:
		node = trie
		for c in word:
			node = node.setdefault(c,{})
		node[WORD_KEY]= word
		
	def backtrack(row,col,parent):
		letter = board[row][col]
		cur = parent[letter]
		word_match = cur.pop(WORD_KEY, False)
		if word_match:
			res.append(word_match)

		# Set cell as visited
		board[row][col] = VISITED

		for y,x in [[0,1], [0,-1], [1,0], [-1,0]]:
			r = row+y
			c = col+x
			pos = (r, c)
			if  r< 0 or r >= m or c < 0 or c >= n: 
				continue 
			if not board[r][c] in cur:
				continue
			backtrack(r, c,cur) 
		# Restore cell	
		board[row][col] = letter
		# Prune visited leaf nodes
		if not cur:
			parent.pop(letter)

	# Be smart about where to start search, ie: only if starting letter is in trie
	for r in range(m):
		for c in range(n):
			if board[r][c] in trie:
				backtrack(r, c, trie)
	return res

```
**Complexity:** O(M(4x3)to the power of (L-1)) where M is number of cells in the grid, 4 for initial direction, 3 for possible directions to backtrack, and L is the length of the longest word in the trie
**Space:** O(Number of characters inside the dictionary) and x2 if we store the word inside too
https://leetcode.com/problems/word-search-ii/description

## Graphs

### MST
#### Critical and Pseudo-critical edges in MST
- Build MST to find min cost
- For every edge,
	- ignore it: if new mst built has higher cost, it is critical
	- force it: calculate a new mst starting with this edge. If new mst has the same cost, this edge is pseudo-critical
- Time Complexity: Building E MST's = O(EE Log E)
##### Alternative
https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/solutions/1478977/100-faster-o-ev-building-mst-once-is-enough/
- Build MST
##### Optimized
https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/solutions/698025/o-eloge-kruskal-tarjan/
- Use Kruskal and Tarjan's


https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/