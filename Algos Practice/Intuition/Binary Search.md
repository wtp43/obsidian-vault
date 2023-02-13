
- [ ] [[LC-1752. Check if Array Is Sorted and Rotated]] (Find the pivot if sorted array is rotated)
- Important to note that the first and last num are connected
- Check if the next number is bigger: This can only happen once if sorted and rotated
	- nums[i] > nums[(1+i)%n]


- [ ] [[LC-153. Find Minimum in Rotated Sorted Array]]
- Update the min every loop. The min will not always land on j or always on i
- `If nums[j] > nums[mid]: the min has to be on the left


- [ ] [[LC-33. Search in Rotated Sorted Array]]

>[!danger]+ Intuition
>   enumerate possibilities
> 
1. `we are in the left portion ([6789] 123)
	    - `target > nums[mid]: i=mid+1
	    - ``nums[i] <= target < nums[mid] j=mid-1
	    - `target < nums[i]: i=mid+1
2. `we are in right portion (78 [123])
		- `target < num[mid]: j=mid-1
		- `nums[mid] < target <= nums[j]: i=mid+1
		- `target > nums[j]: j=mid-1

- [ ] [[LC-74. Search a 2D Matrix]]

- [ ] [[LC-981. Time Based Key-Value Store]]
- We want to store multiple values with different timestamps for the same key
- We notice that since time is strictly increasing, our list of values will in sorted order
- Create a dictionary of lists and binary search on the list

- [ ] [[LC-34. Find First and Last Position of Element in Sorted Array]]
- Left and right bisect essentially move the same way when target != `nums[mid]
- The only difference is when the target == `nums[mid]
- Left bisect will set j = mid-1 and move left 
- Right bisect will set i = mid+1 and move right

- [ ] [[LC-1268. Search Suggestions System]]
- Suggest at most 3 words based on the prefix
- Sort strings then bisect left on the prefix 

- [ ] [[LC-2563. Count the Number of Fair Pairs]]
	- Find pairs (i,j) where lower <= nums[i] + nums[j] <= upper
	- Bisect_left and bisect_right on index i+1 with upper-nums[i] and lower-nums[i]
	- res += r-l
	- 