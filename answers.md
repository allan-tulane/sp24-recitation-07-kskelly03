# CMPS 2200 Recitation 10## Answers

**Name:** Kevin Skelly

**Name:** Zach Goodman


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**

$W(n, m) = W(2m) + W(n) + 1 \in O(n+m)$

- **4)**

Reachable will only be called once for any case of graph, and will return true if the graph is connected, and false if not. Therefore, in the worst case it will only be called one single time.

- **5)**

$W(n, m) = W(2m) + W(n) + O(1) + 1 \in O(n+m)$

- **7)**

There are noticeable differences from changing the graph to an adjacency matrix. Finding all the neighbors of a node will become an $O(n)$ operation since all you have to do is go to the row of the node and check along the row. Total work for checking the neighbors of every node will thus be $O(n^2)$ because every entry in the matrix will be checked.
