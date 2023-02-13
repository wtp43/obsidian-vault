# Mathematics

To get the number of items in a range ``[l,r]``: 
- size = r-l+1

- [x] [[LC-367. Valid Perfect Square]] 
- The sqrt of a num is always <= num/2

Combining two numbers without using string concatenation
- [32, 45] -> 3245
```python
def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = 0
        i,j = 0,len(nums)-1
        while i <= j:
            if i < j:
                res += nums[i] * pow(10, floor(log10(nums[j]))+1) + nums[j]
            else:
                res += nums[i]
            i += 1
            j -= 1
        return res
            
```