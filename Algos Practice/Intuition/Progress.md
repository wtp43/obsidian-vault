---
todo
---
# More Questions
https://seanprashad.com/leetcode-patterns
https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/
 - cyclic sort
 - two heaps
 - subsets
 - top k
 - k way merge
 - 0/1 knap sack
 - kth smallest number
	 - quick select

# To do
```dataview 
TABLE 
filter(file.tasks, (t) => !t.completed).text AS "Uncompleted tasks　　　　　　　　　　　　　　　　　", length(filter(file.tasks, (t) => !t.completed).text) as Remaining, 
"<progress value='" + (length(filter(file.tasks.completed, (t) => t = true)) / length(file.tasks.text)) * 100 + "' max='100'></progress>" 
AS Progress 
FROM "Algos Practice/Intuition"
WHERE file.tasks 
SORT file.name
```

# Completed

```dataview 
TABLE 
filter(file.tasks, (t) => t.completed).text AS "Completed tasks　　　　　　　　　　　", length(filter(file.tasks, (t) => t.completed).text) as Completed, 
"<progress value='" + (length(filter(file.tasks.completed, (t) => t = true)) / length(file.tasks.text)) * 100 + "' max='100'></progress>" 
AS Progress 
FROM "Algos Practice/Intuition"
WHERE file.tasks 
SORT file.name
```
