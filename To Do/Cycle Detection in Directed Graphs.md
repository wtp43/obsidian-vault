
>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```

# Using Topological Search (3 Coloring)

Use the following approach: consider we have three colors, and each vertex should be painted with one of these colors. _"White color"_ means that the vertex hasn't been visited yet. _"Gray"_ means that we've visited the vertex but haven't visited all vertices in its subtree. _"Black"_ means we've visited all vertices in subtree and left the vertex. So, initially all vertices are white. When we visit the vertex, we should paint it gray. When we leave the vertex (that is we are at the end of the _dfs()_ function, after going throung all edges from the vertex), we should paint it black. If you use that approach, you just need to change _dfs()_ a little bit. Assume we are going to walk through the edge _v->u_. If _u_ is white, go there. If _u_ is black, don't do anything. If _u_ is gray, you've found the cycle because you haven't left _u_ yet (it's gray, not black), but you come there one more time after walking throung some path.

To keep vertices' colors replace boolean array with char or integer array and just use values in range [0..2].


# Union Find
- If two vertices that you are merging have the same parent, a cycle exists

# Related





