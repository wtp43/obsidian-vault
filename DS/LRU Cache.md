---
title:  "LRU Cache"
tags:
- ds
created: 2022-12-16
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```


# LRU Cache
Least recently used (LRU) cache. Discard the least recently used items first from the cache to make room for new elements when cache is full.

Retrieving data from a computer's memory is an expensive task. 
High-speed memory known as cache memory is used to avoid accessing data from memory repeatedly.
# Implementation (Brute force: Using a simple array)
Initialize an array of size equal to that of our cache. Each data element stores extra information (timestamp). Use timestamp to find the least recently used element in the LRU cache

```python
from datetime import datetime
class Data_element:
	def __init__(self):
		self.key = key
		self.val = val
		self.time_stamp = datetime.now
	
```

## Optimizations

## Optimized Complexity

>[!Time Complexity]+
>Lookup: O(1)

>[!Space Complexity]+
>O(n)



# Related
