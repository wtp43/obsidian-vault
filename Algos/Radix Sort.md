---
title:  "Radix Sort"
tags:
- algo
- sort
created: 2022-12-15
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```


# Radix Sort
Sorts by first grouping the individual digits of the same **place value**. 

# Most Significant Digit (MSD) vs Least Significant Digitt (LSD) Radix Sort
If we start with the most significant digits, a first pass would go a long way toward sorting the entire range. The idea of a MSD radix sort is to divide all the digits with an equal value into their own bucket and repeat. Naturally, this suggests a recursive algorithm, but this also means that we can now sort variable length items and we don't have to touch all of the digits to get a sorted array. However, a recursive implementation of MSD uses more space than LSD. LSD is faster than MSD when there is a fixed length. (https://stackoverflow.com/questions/11939656/radix-sort-lsd-versus-msd-versions)
# Implementation

```python

```

## Optimizations

## Optimized Complexity

>[!Time Complexity]+

>[!Space Complexity]+



# Related
