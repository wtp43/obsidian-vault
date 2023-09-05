---
title:  "Newton's Method"
tags:
created: 2023-01-26
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```


# Newton's Method
Problem: Find the root of 
$$f(x) = x^2 - num = 0$$
1. Set a seed(initial guess) $x_k$
2. To compute $x_{k+1}$, approximate $f(x_k)$ by its tangent
$$x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$$
# Implementation

```python
class Solution {
  public boolean isPerfectSquare(int num) {
    if (num < 2) return true;

    long x = num / 2;
    while (x * x > num) {
      x = (x + num / x) / 2;
    }
    return (x * x == num);
  }
}
```

## Optimizations

## Optimized Complexity

>[!Time Complexity]+

>[!Space Complexity]+



# Related
