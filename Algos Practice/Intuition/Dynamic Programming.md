
# Dynamic Programming
- [ ] https://leetcode.com/problems/minimum-cost-to-split-an-array/description/
https://leetcode.com/problems/minimum-cost-to-split-an-array/solutions/3083850/python3-dp/

- [ ] [[LC-472. Concatenated Words]]
- https://leetcode.com/problems/concatenated-words/solutions/2822170/concatenated-words/?orderBy=most_votes
Why sliding window wouldn't work here:
- There is no window of k for our solution
	- The size of k will not encompass all the substrings that a word may contain
	- we need to do more comparisons
- Sorting does not allow us to find the answer in O(1)
	- we realize that we have to check more than just the word at the start of the window

- [ ] [[LC-115. Distinct Subsequences]]

- [ ] https://leetcode.com/problems/longest-increasing-subsequence/
- [ ] [[LC-2218. Maximum Value of K Coins From Piles]]

- [ ] [[LC-139. Word Break]]
	- Can the string be built using words that exist in the dictionary
	- We want dp to store the states from 0 to n+1 because a 
	- Iterate for each start index of the string
		- Iterate for all words in the dictionary
	- State[i] = whether the string up to index i can be constructed using words form the dictionary
	- State[i] = s[i-len(w):i] == w and dp[i-len(w)]
- [ ] [[LC-5. Longest Palindromic Substring]]
	- State`[i][j]` = 1 if the str from i to j is a palindrome
	- State`[i][j]` = s`[i] == s[j] and state[i+1][j-1]
	- Using a bottom up approach, we have to have already calculated state`[i+1][j-1]
	- So the loop structure should be 
```python
for i in reversed(range(n)):
	for j in (i+1, n):
```

- [x] [[LC-322. Coin Change]]


- [ ] [[LC-152. Maximum Product Subarray]]
- Can contain negative numbers
- Maintain the cur_max and cur_min
- When there is a negative number, they will swap
- If the number is 0, we restart our product
- Update the max_so_far after each iteration

- [ ] [[LC-300. Longest Increasing Subsequence]]
	- Recurrent relation: `dp[i] = max(dp[i], dp[j] + 1)` for j = 0..i-1

[[LC-416. Partition Equal Subset Sum]]
- Subset sum (01 knapsack)
[[LC-474. Ones and Zeroes]]
- Iterating each word will allow us to save space so we don't have to recount the number of 0's and 1's in each word
- Consider only the possible indices we have to check
- In this case # of 0s...m, # of 1s...n
- We also want to iterate backwards, range(n,`A[0]`-1,-1), because we do not want to rewrite previous calculations by including the previous string. Doing this bottom up may result in duplicated count of the current word

# Pattern Recognition
Generally we want to find some kind of pattern that holds true in every subset.
Then prove it (by induction).
- ie: We notice that all the elements used to build our window are the maximum in the last k elements
# Memoization
[[0-1 Knapsack#Memoization]] 
- Bottom up dynamic programming that only uses O(n) space

Always consider the state of each `dp[i][j]`
- Like in [[LC-474. Ones and Zeroes]]
- `dp[i][j]` is a different state for every new word
- To avoid duplicates, we have to iterate backwards when updating max subsets
- Otherwise, if we do it bottom up, we may end up using the same word twice

Usually, if we want the reuse the 

