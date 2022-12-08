>[!Note]
>Binary Search should be equal to Bisect_left in the case of no duplicates

## Bisect Left
- Returns the index of the first num $\leq$ x
- Repeatedly move right border towards the left if there are duplicates

```python
def bisect_left(arr, x):
	i = 0
	j = len(arr)-1
	while i <= j:
		mid = i + (j - i)//2
		if arr[mid] >= x:
			j = mid - 1
		else:
			i = mid + 1
	return i
```

## Bisect Right
- Returns the index + 1 of the first num > x

```python
def bisect_right(arr, x):
	i = 0
	j = len(arr)-1
	while i <= j:
		mid = i + (j - i)//2
		if arr[mid] <= x:
			i = mid + 1
		else:
			j = mid - 1
	return i
