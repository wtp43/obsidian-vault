---
title:  "LC 2. Add Two Numbers"
tags:
- linked-list
- lc-medium
created: 2023-01-06
---

>[!summary]+ Contents
>```toc
>style: number
>min_depth:1
>max_depth:6
>```

# Description
You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

**Input:** l1 = \[2,4,3], l2 = \[5,6,4]
**Output:** [7,0,8]
**Explanation:** 342 + 465 = 807.

**Example 2:**

**Input:** l1 = [0], l2 = [0]
**Output:** [0]

**Example 3:**

**Input:** l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
**Output:** [8,9,9,9,0,0,0,1]

**Constraints:**

-   The number of nodes in each linked list is in the range `[1, 100]`.
-   `0 <= Node.val <= 9`
-   It is guaranteed that the list represents a number that does not have leading zeros.

# Intuition

>[!danger]+ Intuition
>Maintain a carry. 

# Implementation
```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
	s = ListNode()
	cur = s
	carry = 0
	while l1 or l2:
		val = carry
		if l1:
			val += l1.val
			l1 = l1.next
		if l2:
			val += l2.val
			l2 = l2.next
		if val >= 10:
			carry = 1
			val -= 10
		else:
			carry = 0
		cur.next = ListNode(val)
		cur = cur.next
	if carry:
		cur.next = ListNode(1)
	return s.next
```

>[!example]+ 

O(max(l1 + l2)) because we iterate at most max(l1 + l2) times while building the linked list.
 
O(max(l1 + l2)+1) Space complexity because that's how long the new linked list will be.
# Related
