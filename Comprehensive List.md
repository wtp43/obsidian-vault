
# Implement and test 
- [ ] Prim's Algorithm
- [ ] Indexed Priority Queue
- [x] Cycle detection in DAG (3 coloring) with topological sort

# Topics

- [ ] Backtracking
	- [ ] N Queen
	- [ ] Maze Solving 
	- [ ] Knigh'ts Tour
	- [ ] Hamiltonian Paths
- [ ] Binary Search
	- [ ] https://leetcode.com/problems/search-a-2d-matrix-ii/description/
	- [ ] Ternary Search
	- [ ] Interpolation Search
- [ ] Binary Trees
	- [ ] Self Balancing Tree
	- [ ] AVL Tree
	- [ ] https://leetcode.com/problems/reachable-nodes-with-restrictions/description/
	- [ ] https://leetcode.com/problems/count-complete-tree-nodes/description/
	- [ ] https://leetcode.com/problems/closest-binary-search-tree-value-ii/description/
	- [ ] https://leetcode.com/problems/diameter-of-n-ary-tree/description/
	- [ ] https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/description/
	- [ ] https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
	- [ ] https://leetcode.com/problems/inorder-successor-in-bst-ii/description/
	- [ ] Fenwick tree
	- [ ] Redblack tree
- [ ] Dynamic Programming
	- [ ] https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/description/
	- [ ] https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/solutions/2808845/python3-dp-with-explanations-only-check-substrings-of-length-k-and-k-1/
	- [ ] https://leetcode.com/problems/longest-palindromic-substring/description/
	- [ ] https://leetcode.com/problems/palindromic-substrings/description/
	- [ ] https://leetcode.com/problems/house-robber-iii/description/
	- [ ] https://leetcode.com/problems/paint-fence/description/
	- [ ] https://leetcode.com/problems/paint-house/description/
- [ ] Graph Theory: https://www.freecodecamp.org/news/graph-algorithms-and-data-structures-explained-with-java-and-c-examples/
	- [ ] https://cp-algorithms.com/graph/breadth-first-search.html
	- [x] Topological Sort
		- [ ] Cycle Detection
	- [ ] Strongly Connected Components
	- [ ] https://emre.me/algorithms/tarjans-algorithm/
	- [ ] DFS (Valid path)
		- [ ] https://leetcode.com/problems/find-if-path-exists-in-graph/solutions/2715942/find-if-path-exists-in-graph/
		- [ ] def dfs(curr_node):
		            if curr_node == destination:
		                return True
		            if not seen[curr_node]:
		                seen[curr_node] = True
		                for next_node in graph[curr_node]:
		                    if dfs(next_node):
		                        return True
		            return False
	- [ ] Prims
	- [ ] Kruskals
	- [ ] Dijkstras
	- [ ] Topological Sort
	- [ ] Floyd Warshall
		- [ ] https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
		- [ ] https://leetcode.com/problems/evaluate-division/
		- [ ] https://leetcode.com/problems/cheapest-flights-within-k-stops/
		- [ ] https://leetcode.com/problems/course-schedule-iv/
		- [ ] https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/
	- [ ] Bellman Ford
	- [ ] Network Flow
	- [ ] Hierholzer's Algorithm for Eulerian Circuits
		- [ ] https://leetcode.com/problems/reconstruct-itinerary/
	- [ ] A* Search
		- [ ] https://leetcode.com/problems/sliding-puzzle/
	- [ ] Kosaraju's
	- [ ] Flood Fill Algo
	- [ ] Euler's and Hamilton's Algo
	- [ ] Ford Fulkerson
	- [ ] Kahn's
	- [ ] Max Flow, Min-Cut
		- [ ] https://leetcode.com/problems/maximum-students-taking-exam/
	- [ ] Articulation Points and Bridges
		- [ ] https://leetcode.com/problems/critical-connections-in-a-network/

- [ ] Greedy
	- [ ] https://leetcode.com/problems/increasing-triplet-subsequence/description/
	- [ ] https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/
		- [ ] How do we keep track of the balloon with the greatest time?
			- [ ] Greedily keep track of the balloon with greatest removal time
			- [ ] Since we need two consecutive balloons of the same color for the removal to trigger, we won't have to worry about adding the largest removal time.
	- [ ] - [ ] Knapsack problem
- [ ] Hashing (import for AI Algorithms)
	- [ ] https://leetcode.com/problems/number-of-distinct-islands/solutions/
	- [ ] https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1126/
- [ ] Kadane's Algorithm
	- [ ] https://leetcode.com/problems/longest-increasing-subsequence/description/
	- [ ] https://leetcode.com/problems/substring-with-largest-variance/solutions/2579146/weird-kadane-intuition-solution-explained/
- [ ] Linked List
	- [ ] Cycle Detection
	- [ ] In-place reversal
- [ ] Sets
	- [ ] https://leetcode.com/problems/find-smallest-common-element-in-all-rows/solutions/
- [ ] Sliding Window
	- [ ] https://emre.me/coding-patterns/sliding-window/
	- [ ] https://leetcode.com/problems/substring-with-concatenation-of-all-words/
	- [ ] https://leetcode.com/problems/longest-repeating-character-replacement/description/
	- [ ] https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
	- [ ] https://leetcode.com/problems/sliding-window-maximum/
- [ ] Sort
	- [ ] https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
	- [x] Count/Bucket/Radix Sorts
	- [x] Quick Sort
	- [ ] Cyclic sort
		- [ ] https://emre.me/coding-patterns/cyclic-sort/
		- [ ] https://leetcode.com/discuss/study-guide/1902662/cyclic-sort-very-important-and-less-known-pattern
	- [x] Merge Sort
- [ ] Sparse Table
	- [ ] https://cp-algorithms.com/data_structures/sparse-table.html
	- [ ] 
- [ ] String Matching
	- [ ] Prefix Function: KMP: https://www.scaler.com/topics/data-structures/kmp-algorithm/
	- [ ] https://leetcode.com/problems/palindrome-pairs/description/
	- [ ] Rabin Karp for String Matching: https://cp-algorithms.com/string/rabin-karp.html
	- [ ] Z Function: https://cp-algorithms.com/string/z-function.html#trivial-algorithm
	- [ ] Suffix Array
		- [ ] https://cp-algorithms.com/string/suffix-array.html#practice-problems
	- [ ] Aho-Corasick Algorithm (Similar to trie but with additional links that constrcuts a finite state machine in O(mk) time)
		- [ ] https://cp-algorithms.com/string/aho_corasick.html
	- [ ] Suffix Tree (Advanced)
- [ ] Tries
- [ ] Top K Problems
	- [ ] https://leetcode.com/discuss/general-discussion/1088565/top-k-problems-sort-heap-and-quickselect
	- [ ] K-Way Merge
	- [ ] [[Top K Frequent Elements]]
	- [ ] https://leetcode.com/problems/kth-largest-element-in-an-array/solutions/214469/kth-largest-element-in-an-array/ (Quick Select in Kth largest element)
		- [ ] https://www.youtube.com/watch?v=v-1EGgaTFuw
- [ ] Two Pointers
# Improving Intuition

- When there is no obvious solution, try brute forcing
	- How to determine if current word in path (word``[i:j]``) is a palindrome? Sol: Iterate the entirety of the word instead of determining the palindrome concurrently with DFS
	- Make Number of Distinct Characters Equal: Swap every character in each word with each other

LC-Hard
- [ ] https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
- [ ] https://leetcode.com/problems/number-of-islands-ii/description/
- [ ] https://leetcode.com/problems/word-search-ii/description/

LC-Medium
- [ ] https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

# Design (More Advanced Data structures)
- [ ] https://leetcode.com/problems/insert-delete-getrandom-o1/
- [ ] [[LRU Cache]]
- [ ] LFU Cache
- [ ] Trie Problems
# Recognizing NP-Hard Problems
Subset Sum if finding all subsets
- Reduced to O(sum$*$n) using DP if using just finding one
# Competitive Programming


# Review
- [ ] Linked list operations/traversals
- [ ] Binary heap deletion

# Low Priority/Other

- [ ] Bit manipulation
	- [ ] https://emre.me/computer-science/bit-manipulation-tricks/
	- [ ] https://emre.me/computer-science/binary-computation-and-bitwise-operators/
- [ ] Traveling salesman problem
- [ ] Combinatorics
	- [ ] https://cp-algorithms.com/algebra/factorial-divisors.html
- [ ] Numerical Methods
	- [ ] https://cp-algorithms.com/num_methods/binary_search.html
- [ ] Basic Number Theory
	- [ ] https://www.youtube.com/watch?v=KOzByAdxVZ8
	- [ ] https://cp-algorithms.com/algebra/binary-exp.html#implementation
- [ ] Knapsack problemGeometry
	- [ ] https://cp-algorithms.com/geometry/basic-geometry.html
	- [ ] Graham scan for convex hull
	- [ ] https://cp-algorithms.com/geometry/convex-hull.html
- [ ] Knapsack problemRoadmap Resources
	- [ ] https://docs.google.com/document/d/1-7Co93b504uyXyMjjE8bnLJP3d3QXvp_m1UjvbvdR2Y/edit

- [ ] **System and OO design Principles (sometimes)**
    - Some compaines ask Object Oriented questions. A great great resource for this is the book "Clean Architecture" by Robert C. Martin. I also highly recommend his book "Clean Code" but it won't help you for interviews (but will make you a better programmer)

# Problem Solving
## List all Possibilities we need to account for

# More Questions
https://seanprashad.com/leetcode-patterns/

```dataviewjs
dv.taskList(dv.pages('-"Templates"').file.tasks
.where(t => !t.completed && !t.text.includes("@frank") &&
!t.text.includes("#task")
))
```