def qsort(nums: list[int]) -> None:
    def qsort_helper(nums: list[int], l: int, r: int) -> None:
	    # Stop the partitioning when the array contains only 1 element
        if l >= r: 
	        return

        p = partition(nums, l, r)
        qsort_helper(nums, l, p - 1)
        qsort_helper(nums, p + 1, r)

    def partition(nums: list[int], l: int, r: int) -> int:
        p_ind = l
        pivot = nums[r]
        for i in range(l, r):
            if nums[i] < pivot: 
                nums[i], nums[p_ind] = nums[p_ind], nums[i]
                p_ind += 1
        nums[p_ind], nums[r] = nums[r], nums[p_ind]
        return p_ind
        
    qsort_helper(nums, 0, len(nums) - 1)

nums = [4,3,2,9,3,1]
qsort(nums)
print(nums)