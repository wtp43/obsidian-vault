---
title:  "Fibonacci Heap"
tags:
- heap
- priority-heap
- ds
created: 2022-12-13
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```


# Fibonacci Heap
A fibonacci heap consists of a collection of trees which follow min heap or max heap property. In a fibonacci heap, a node can have more than two children or no children at all. The trees are constructed in a way such that a tree of order `n` has at least $F_{n+2}$ nodes in it, where $F_{n+2}$ is the $(n+2)^{th}$ Fibonacci number
![Fibonacci Heap](https://www.programiz.com/sites/tutorial2program/files/fibonacci-heap.png "Fibonacci Heap")

The roots of all the trees are linked together for faster access. 
The child nodes of a parent node are connected to each other through a circular doubly linked list. A circular doubly linked list is used because deleting a node from the tree takes O(1) time. The concatenation of two such lists takes O(1) time.

![Fibonacci Heap Structure](https://www.programiz.com/sites/tutorial2program/files/fibonacci-heap-structure.png "Fibonacci Heap Structure")

# Properties of a Fibonacci Heap
1. It is a set of min heap-ordered trees (I.e. the parent is always smaller than the children)
2. A pointer is maintained at the minimum element node
3. It consists of a set of marked nodes (Decrease key operation)
4. The trees within a Fibonacci heap are unordered but rooted

# Operations
Degree of node = # of children it has (not including grand children)
## Extract Min
1. Delete min node
2. Set the min-pointer to the next root in the root list
3. Create an array of size equal to the maximum degree of trees in the heap before deletion
4. Repeate (steps 5-7) until there are no multiple roots with the same degree
5. Map the degree of current root (min-pointer) to the degree in the array
6. Map the degree of next root to the degree in array
7. If there are more than two mappings for the same degree, then apply union operation to those roots such that the min-heap property is maintained


> [!danger]+ Intuition
> To minimize the heights of trees after unions, we have to merge in a way such that the degree of the last tree is at most "max degree". We should then merge trees with similar degrees which guarantees that the maximum degree will be the max degree pre-merge + 1

# Max Degree
A binomial tree with degree d has $2^d$ nodes. 
A binomial tree with k nodes means the max degree is $log_2(k)$
# Implementation

```python

```

## Optimizations

## Optimized Complexity

>[!Time Complexity]+

>[!Space Complexity]+




# Related
- [[Heaps]]
- [[Indexed D-ary Heap]]
- [[Indexed Priority Queue (IPQ)]]