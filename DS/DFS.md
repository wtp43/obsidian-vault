---
tags:
- tree-traversal
---

## Pros vs BFS
- Space complexity O(depth) nodes compared to O(|V|) = O(n) for BFS


## Time Complexity

## Space Complexity


```python
seen = set()

def dfs(graph: Dict[int, List[int]], cur: int):
    if cur in seen: return
    seen.add(cur)
    for next in graph[cur]:
        dfs(graph, next)
```
- Alternatively, graph and seen can be set as global variables. 
- 'seen' does not need to be marked as `global` inside `dfs` to modify it because we are not reassigning its value using `=`

# Use Cases

## [[Connected Components]]
- Start DFS at every node (except if it's already been visited) and mark all reachable nodes as being part of the same component
- [[LC-200. Number of Islands]]

## Depth-First-Search Traversals

### Pre-order Traversal

### In-order Traversal

### Post-order Traversal