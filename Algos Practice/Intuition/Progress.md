---
todo
---
# To do
```dataview 
TABLE 
filter(file.tasks, (t) => !t.completed).text AS "Uncompleted tasks", length(filter(file.tasks, (t) => !t.completed).text) as Remaining, 
"<progress value='" + (length(filter(file.tasks.completed, (t) => t = true)) / length(file.tasks.text)) * 100 + "' max='100'></progress>" 
AS Progress 
FROM "Algos Practice/Intuition"
WHERE file.tasks 
SORT file.name
```

# Completed

```dataview 
TABLE 
filter(file.tasks, (t) => t.completed).text AS "Uncompleted tasks", length(filter(file.tasks, (t) => t.completed).text) as Completed, 
"<progress value='" + (length(filter(file.tasks.completed, (t) => t = true)) / length(file.tasks.text)) * 100 + "' max='100'></progress>" 
AS Progress 
FROM "Leetcode Questions/Todo"
WHERE file.tasks 
SORT file.name
```
