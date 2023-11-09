---
dg-publish: true
---
---
title:  "Revision 1"
tags:

created: 2023-11-08
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```

Week 2 of november
# Arrays 

- hashmaps are generally useful for storing some kind of ordering

- longest consecutive subsequence in unsorted array
	- ie: 3, 100, 200, 2, 1, 4
	- o(n): store all numbers into a set
	- build subsequence by checking if the number to the left exists
	- optimization: only start building at numbers that could be a starting point
		- ie: no numbers to the left of it
	- start building sequence if the number to the left doesn't exist
		- search for next number (n+length) in set 
	- update max length

- longest common prefix
	- 

# Union- find
- Path compression find: O(log(logn))
- Merge parents


# Dynamic Programming

Iterative DP
- Construct array such that first row/base case aids in computation
- Constructing recursive relation will help in loop ordering
### LC-1230. Toss Strange Coins
- Return the probability that the number of coins facing heads equals `target` if you toss every coin exactly once.
- The `i`-th coin has a probability `prob[i]` of facing heads when tossed.

- outer loop: prob length
- inner loop: target

- Recursive relation:
	- let i = current coin
	- let j = current target
	- roll heads 
		- p(i) x p(j-1 heads in the first i-1 coins)
	- don't roll heads
		- 1-(p(i)) x p(j heads in first i-1 coins )
**Notice that the recursive relation relies on coin array size**
- this is a hint that you need the answers for i-1 coins must be computed first

The optimal substructure here is that once you have solution for first `i` coins, you can extend it for `i+1` coins.
But when you flip the order of execution of loops, this substructure property does not hold. In this case, you are first calculating the number of ways to form amount `i` using all the coins and extending it to find the number of ways to form amount `i+1`, for which the optimal substructure property does not hold true.


# Related
