---
dg-publish: true
tags: 
created: ""
---
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```

# All Topics

## Graph

- [ ] BFS
	- [ ] Multi-source BFS: iterating queue in chunks/layers using length of queue at the current step
- [ ] DFS
	- [ ] Connected components
- [ ] IDS
- [ ] Union-find
	- [ ] Connected components
- [ ] Backtracking
	- [ ] N-queens

- [ ] Topological Sort 

### Review 
- 


## Binary Search
- [ ] Bisect-right
- [ ] Bisect-left
- [ ] 

### Review
- [[LC-1752. Check if Array Is Sorted and Rotated]]  
	- Compare all neignbour elements `(a,b)` in `A`,  
		the case of `a > b` can happen at most once.
		
		Note that the first element and the last element are also connected.
		
		If all `a <= b`, `A` is already sorted.  
		If all `a <= b` but only one `a > b`,  
		we can rotate and make `b` the first element.  
		Else, return `false`.

- [[LC-153. Find Minimum in Rotated Sorted Array]]

