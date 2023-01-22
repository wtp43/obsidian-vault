---
title:  "Cyclic Sort"
tags:
- algo
- sort
created: 2023-01-06
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```


# Cyclic Sort
Swap numbers of array until they are in the correct place.
Iterate until you find missing/duplicate number.

## Applications:
Dealing with numbers in a given range and asking to find the duplicates/missing ones etc.

When the problem involving arrays containing numbers in a given range, you should think about cyclic sort pattern.

# Implementation

```python
def missingNumber(self, nums: List[int]) -> int:
        start = 0

        while start < len(nums):
            num = nums[start]
            if num < len(nums) and num != start:
                nums[start], nums[num] = nums[num], nums[start]
            else:
                start += 1,

        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)
```

## Optimizations

## Optimized Complexity

>[!Time Complexity]+

>[!Space Complexity]+



# Related
