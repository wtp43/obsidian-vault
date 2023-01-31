Max heaps
To make a max heap, push -x for x in array onto a min heap.

# Heaps
- [ ] [[LC-23. Merge k Sorted Lists]]
- Put the head of each linked list on a heap
- Extend the resulting linked list
- If the extended tail has a next node, put it back on the heap

- [ ] [[LC-1851. Minimum Interval to Include Each Query]]
- Find the smallest interval that can include each query (array of nums)
- Sort queries and intervals
- Put all intervals ``[l,r]`` that include q onto the heap with key ``[l-r+1, r]``
- Pop all intervals where `r` < q
- Store results in dictionary because we sorted our input 

- [ ] https://leetcode.com/problems/the-skyline-problem/description/

- [ ] https://leetcode.com/problems/task-scheduler/description/

- [ ] https://leetcode.com/problems/trapping-rain-water-ii/description/
- [ ] https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/

