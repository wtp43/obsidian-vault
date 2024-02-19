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


# Related
