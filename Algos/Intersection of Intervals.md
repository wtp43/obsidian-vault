---
title:  "Intersection of Intervals"
tags:
- sweep-line
created: 2023-01-05
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```


# Intersection of Intervals
Given n intervals $[li,ri)$ for $i = 0,...,n − 1,$ we wish to find a value x included in a maximum number of intervals. Here is a solution in time O(nlogn). 

We sort the endpoints, and then sweep them from left to right with an imaginary pointer x. 
A counter c keeps track of the number of intervals whose beginning has been seen, but not yet the end, hence it counts the number of intervals containing x.

Note that the order of processing of the elements of B guarantees that the right endpoints of the intervals are handled before the left endpoints of the intervals, which is necessary when dealing with intervals that are half-open to the right.
# Implementation

```python
def max_interval_intersec(S):
	B = ([(left, +1) for left, right in S] +
	[(right, -1) for left, right in S]) 
	B.sort()
	c = 0
	best = (c, None) 
	for x, d in B:
		c += d
		if best[0] < c:
			best = (c, x) 
	return best
```

## Optimizations

## Optimized Complexity

>[!Time Complexity]+

>[!Space Complexity]+



# Related
[[Sweep Line]]