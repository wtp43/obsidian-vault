---
title:  "Subset Sum"
tags:
- algo
- dp
created: 2023-01-13
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```


# Subset Sum
Given a set of positive integers and an integer `k`, check if there is any non-empty subset that sums to `k`.
Backtracking would take O($n * 2^n$)

Special case of 0-1 Knapsack Problem. 
At each step we can either:
1. Include the current item
2. Exclude the current item
Return true if we get a subset by including or excluding the current item.

Using dynamic programming

# Implementation

```python
def subsetSum(A, k):
    n = len(A)
    # `T[i][j]` stores true if subset with sum `j` can be attained
    # using items up to first `i` items
    T = [[False for x in range(k + 1)] for y in range(n + 1)]
 
    # if the sum is zero
    for i in range(n + 1):
        T[i][0] = True
 
    # do for i'th item
    for i in range(1, n + 1):
        # consider all sum from 1 to sum
        for j in range(1, k + 1):
            # don't include the i'th element if `j-A[i-1]` is negative
            if A[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                # find the subset with sum `j` by excluding or including the i'th item
                T[i][j] = T[i - 1][j] or T[i - 1][j - A[i - 1]]
 
    # return maximum value
    return T[n][k]
```

## Optimizations

## Optimized Complexity

>[!Time Complexity]+

>[!Space Complexity]+



# Related
