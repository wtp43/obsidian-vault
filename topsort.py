from collections import deque

def topsort(edges, n):
	top_order = deque()
	indegree = [0] * n
	adj_list = [[] for _ in range(n)]
	for u,v in edges:
		adj_list[u].append(v)
		indegree[v] += 1

	# Store all the nodes with no incoming edges
	q = deque([i for i in range(n) if indegree[i] == 0])
	while q:
		# extract front of queue
		u = q.popleft()
		# add the current vertex to the tail of the ordering
		print(u, indegree)
		top_order.append(u)
		for v in adj_list[u]:
			print(v)
			indegree[v] -= 1
			if indegree[v] == 0:
				q.append(v)
				
	if len(top_order) != n:
		print('Cycle Exists')
	return top_order

edges = [(0,1), (1,2)]
print(topsort(edges, 3))

edges = [(0,1), (1,2), (2,1)]
print(topsort(edges, 3))