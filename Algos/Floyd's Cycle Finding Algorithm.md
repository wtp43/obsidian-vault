---
title:  "Floyd's Cycle Finding Algorithm"
tags:
- algo
- fast-slow-pointer
- cycle-detection
- linked-list
created: 2023-02-02
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```


# Floyd's Cycle Finding Algorithm

# Implementation

```python
def detectLoop(head):
    slowPointer = head
    fastPointer = head
 
    while (slowPointer 
           and fastPointer 
           and fastPointer.next):
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
        if (slowPointer == fastPointer):
            return 1
    return 0
```

# Finding where the Cycle Starts
X = Distance between the head(starting) to the loop starting point.

Y = Distance between the loop starting point and the first meeting point of both the pointers.

C = The distance of the loop

Before the two pointers meet.
The slow pointer has traveled $X + Y + s * C$ distance, where s is any positive constant number.
The fast pointer has traveled $X + Y + f * C$ distance, where f is any positive constant number.


Since the fast pointer is moving twice as fast as the slow pointer, we can say that the fast pointer covered twice the distance the slow pointer covered. Therefore:
$$X + Y + f * C = 2 * (X + Y + s * C)$$
Rearrange to get:
We can say that,

f * C – 2 * s * C = (some integer) * C

                         = K * C

Thus,

X + Y = K * C       – ( 1 )

X = K * C – Y        – ( 2 )

Where K is some positive constant.    We can say that,

f * C – 2 * s * C = (some integer) * C

                         = K * C

Thus,

X + Y = K * C       **– ( 1 )**

X = K * C – Y        **– ( 2 )**

Where K is some positive constant.We can say that,

f * C – 2 * s * C = (some integer) * C

                         = K * C

Thus,

X + Y = K * C       – ( 1 )

X = K * C – Y        – ( 2 )

Where K is some positive constant.    

# Related
