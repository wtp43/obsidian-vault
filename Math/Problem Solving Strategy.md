Question: How can an idea be helpful?
Process: Convince Correctness at each step
Review: Shorten solution (Try to see whole sol. at a glance)

Discover and solve simpler analogous problems 

1. Understand the Problem
	- What is given by the problem? 
	- Can we group different data points from some unique characteristic?
	- What actions can we take?
	- **What are the possible outcomes?**
		- Visualize them by writing them out as commented code
1. Devise a plan
	- Eliminate possibilities
	- Use symmetry
	- Consider edge cases
	- Look for patterns
	- Solve a simpler problem
	- Draw picture
2. Carry out a plan
	- Discard quick if it doesn't work and restart
3. Reflect/Extend
	- What worked, what didn't
	- Where else can this solution be used
	- Learn to predict what strategy to use to solve future problems
	- Look for more elegant solutions

# Understanding the Question
## Enumerate all the possibilities
Can we determine a function for the valid actions?
x: f(x) -> ?


## Base cases
What are the base cases?
- Check that the array is nonempty
if not nums:
	return 0



# DS/Algo Strategy
## Can we use a data structure?
1. Set
2. Dictionary
3. Stack
4. Priority Queue
5. Tree
6. Graph

## What type of search are we doing?

Is the type of data we are searching on a graph?
- DFS/BFS

Can the data be rearranged?
- Sort then binary search
If not, 
- Two pointer approach
	- If `x[i] < x[j]` 
		- i += 1 else j -= 1



## Is there an obvious greedy algorithm?
- We emphasize obvious because it is hard to know we've tried all the possible greedy ideas
	- It may be that we did not consider some other attribute of the data, ordered the data some other way, transformed the data, or attempted some reduction to a problem before solving it
- Greedy Choice Property
	- The globally optimal solution can be obtained by making a locally optimal solution
	- The choice made by a greedy algorithm may depend on earlier choices but not on the future

## If no greedy algorithm is obvious, we need to resort to more brute force approaches
Exhaust all possibilities
Exhaust all comparisons

1. Backtracking/Recursion
2. Dynamic Programming
		Dynamic Programming is mainly an optimization over plain [recursion](https://www.geeksforgeeks.org/recursion/). Wherever we see a recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming. The idea is to simply store the results of subproblems, so that we do not have to re-compute them when needed later.
	


# Approaches
## Sorting
Can we assume that we can sort the data?
- That it can be copied without memory constraints
Can we sort the data and use a greedy approach?
- Intervals/Scheduling
If sorted, we can also use binary search

## Two Pointer
- Can we first sort the array
- Compare two pointers i and j and the target
- Where should the pointers start

## Heap/Priority Queue
Is our list of data going to be non-static?
Do we need to keep an updated sorted list?

## Stack




