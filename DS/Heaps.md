>[!Complexity]
>O(n) to build using sift_down starting from the last parent

Parent::[[Table of Contents]]
Category::[[DS]]

```python
class min_heap:

	def __init__(self):
		self.heap = [0]
		self.size = 0
		
	def insert(self, x):
		self.heap.append(x)
		self.size += 1
		self.sift_up(self.size)
		
	def sift_up(self, i):
		while i//2 > 0:
			if self.heap[i] < self.heap[i//2]:
				self.swap(i, i//2)
			i = i//2
			
	def sift_down(self, i):
		while i*2 > self.size:
			mc = self.get_minchild():
			if self.heap[i] > self.heap[mc]:
				self.swap(i, mc)
			i = mc
			
	def min_child(self, i):
		if i*2+1 > self.size or self.heap[i*2] < self.heap[i*2+1]:
			return i*2
		return i*2+1
		
	def del_min(self):
		min_val = self.heap[1]
		self.heap[1] = self.heap[-1]
		self.heap.pop()
		self.size -= 1
		self.sift_down(1)
		return min_val
			
	def swap(self, x, y):
		self.heap[x], self.heap[y] = self.heap[y], self.heap[x]
		
	def make_heap(self, arr):
		self.size = len(arr)
		i = self.size//2
		self.heap = [0] + arr
		while i > 0:
			self.sift_down(i)
			i -= 1


h = min_heap()
h.insert(1)
h.insert(2)
min_val = h.del_min()

```



>[!Applications]
>Build priority queue with get_min and insert in O(logn)

