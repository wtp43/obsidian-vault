




# Dynamic Programming
- [ ] <mark style="background: #cc085d;">https://leetcode.com/problems/minimum-cost-to-split-an-array/description/</mark>
https://leetcode.com/problems/minimum-cost-to-split-an-array/solutions/3083850/python3-dp/

- [ ] 
- [ ] https://leetcode.com/problems/concatenated-words/solutions/2822170/concatenated-words/?orderBy=most_votes
Why sliding window wouldn't work here:
- There is no window of k for our solution
	- The size of k will not encompass all the substrings that a word may contain
	- we need to do more comparisons
- Sorting does not allow us to find the answer in O(1)
	- we realize that we have to check more than just the word at the start of the window

- [ ] <mark style="background: #cc085d;">[[LC-115. Distinct Subsequences]]</mark>