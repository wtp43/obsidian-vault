---
tags:
- shortest-path
- tree-traversal
---

## Pros vs DFS
- Able to find shortest path in an undirected graph

## Time Complexity
O($b^d$) where $b$ is the branching factor, $d$ is the depth of the tree

## Space Complexity

```python
def bfs(graph: Dict[int, List[int]], start: int):
	
    q = deque([node])
    seen = [0]*n
    seen[start] = 1
	prev = [-1]*n
	
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if next in seen: 
                continue
            q.append(next)
            seen[next] = 1
            prev[next] = cur
    return prev

def reconstruct_path(start, end, prev):
	path = []
	while end != start:
		path.append(end)
		end = prev[end]
	path.reverse()

	# if traversing backwards starting from end gives 
	# us the starting node, there exists a path
	if path[0] == s:
		return path
	return []
```
- the prev array allows us to reconstruct the shortest path


# Related Problems

## [[Matrix Traversals|Using BFS to find the shortest path on a grid]]



## BFS Traversals

### Level-order Traversal

