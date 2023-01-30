# Combinatorics
- [x] https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/description/
- There are n monkeys at pos i in an array. 
- Each monkey must move once
- If they move in opposite directions, a collision happens.
- Return the number of collisions
- Is it easier to count the number of collisions or no collisions?
- No collisions = 2 for any n, because monkeys can all move cw or ccw
- Situations with collisions = $2^n - 2$