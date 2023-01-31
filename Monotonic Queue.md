## Monotonic Queue

- [ ] [[LC-862. Shortest Subarray with Sum at Least K]] (MONOQUEUE + PREFIX SUM)
- subarray is contiguous
- contains negative numbers
- maintain the (index, prefixsum from 0 to index) in a monoqueue
- when the prefix sum is smaller than the last prefix sum in the monoqueue, pop the last element
- what we are checking every time is the current prefix sum - prefix sum ending at i
- so in the second while loop, the subarray with the smaller prefix sum is preferred because it has a larger index (resulting in a smaller window in the future) and a smaller prefix sum (resulting in a larger sum in the future)
- we need to keep a monotonically increasing sequence of prefix sums 
- we cannot keep individual elems in the queue because there exists negative numbers
- (2,-1,3) will not work if we just extend the start after finding a sum that's at least k
- we have to keep prefix sums instead to get pass negative numbers
**Why do we have a prefix array and not just the initial array like in sliding window :**  
Because in the sliding window when we move `start` (typically when we increment it) we can just substract `nums[start-1]` from the current sum and we get the sum of the new subarray. Here the value of the `start` is `jumping` and one way to compute the sum of the current subarray in a `constant` time is to have the prefix array.
```python
 def shortestSubarray(self, A, K):
        d = collections.deque([[0, 0]])
        res, cur = float('inf'), 0
        for i, a in enumerate(A):
		    # prefix sum
            cur += a
            # d[0][1] is the prefix sum that ends at 
            while d and cur - d[0][1] >= K:
                res = min(res, i + 1 - d.popleft()[0])
            # we must have encountered a negative number
            # we are considering the start 
            while d and cur <= d[-1][1]:
                d.pop()
            d.append([i + 1, cur])
        return res if res < float('inf') else -1
```


https://medium.com/algorithms-and-leetcode/monotonic-queue-explained-with-leetcode-problems-7db7c530c1d6
https://iq.opengenus.org/monotonic-queue/
https://labuladong.gitbook.io/algo-en/ii.-data-structure/monotonic_queue
https://algo.monster/problems/mono_stack_intro
https://1e9.medium.com/monotonic-queue-notes-980a019d5793
https://leetcode.com/problems/constrained-subsequence-sum/solutions/597751/java-c-python-o-n-decreasing-deque/
- [ ] https://leetcode.com/problems/constrained-subsequence-sum/description/