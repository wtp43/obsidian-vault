---
dg-publish: true
---
# Basic

- [ ] [[LC-108. Convert Sorted Array to Binary Search Tree]]
	- Height-balanced BST
	- Pick the middle as the root (l+r)//2
	- Recursively build the left and right child while omitting the middle
	- Base case: l > r

- [ ] [[LC-572. Subtree of Another Tree]]
	- Check the subtree for every node in the other tree
	- O(mn)
- [ ] [[LC-543. Diameter of Binary Tree]]
	- Precompute the maximum depth from the left and right child (# of nodes)
		- number of nodes = 1 + max(l,r)
	- res = max(res, l+r)
		- longest path = number of nodes in l - 1 + number of nodes in r + 1 + 2(for the edges connecting l and r through the root)
	- Store the result of the max diameter at each recursion because it may not pass through the root
```python
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            res = max(res, l + r)
            return 1 + max(l, r)

        dfs(root)
        return res
```

- [ ] [[LC-112. Path Sum]]
	- Find if there is a path from root-to-leaf, leaf = node with no children
```python
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.right and not root.left:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum-root.val) or \
            self.hasPathSum(root.right, targetSum-root.val)
```


**Leaf-Similar Trees**
https://leetcode.com/problems/leaf-similar-trees/description/
```python
def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node: 
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))
```

**Iterative Traversals**
```python
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur, stack = root, []
        res = []
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            cur = stack.pop()
        return res
 def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        cur = root
        res = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

#post order traversal iteratively is very convoluted

	Append right, then left because of FILO
	Process node if it is a leaf or if it's left or right child has been visited
	Keep track of last processed nodey

def postorderTraversal(self, root: 'TreeNode'):
        if not root:
            return []
        stack, res = [root], []
        # used to record whether left or right child has been visited
        last = None

        while stack:
            root = stack[-1]
            # if current node has no left right child, or left child or right child has been visited, then process and pop it
            if not root.left and not root.right or last and (root.left == last or root.right == last):

                res.append(root.val)

                stack.pop()
                last = root
            # if not, push right and left child in stack
            else:
                # push right first because of FILO
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return res

            

```
**Level Order Traversal**
- Use queue
- `while len(queue)>0`

# Segment Trees
https://www.reddit.com/r/leetcode/comments/wrrrq0/when_to_use_monotonic_queue/

# BST Traversals
https://leetcode.com/problems/inorder-successor-in-bst/solutions/1104016/inorder-successor-in-bst/


# AVL Trees
https://www.youtube.com/watch?v=g4y2h70D6Nk