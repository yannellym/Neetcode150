# 1557. Minimum Number of Vertices to Reach All Nodes
# Medium
# 2.1K
# 77
# Companies
# Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

# Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

# Notice that you can return the vertices in any order.

 

# Example 1:



# Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
# Output: [0,3]
# Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].
# Example 2:



# Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
# Output: [0,2,3]
# Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them. Also any of these vertices can reach nodes 1 and 4.
 

# Constraints:

# 2 <= n <= 10^5
# 1 <= edges.length <= min(10^5, n * (n - 1) / 2)
# edges[i].length == 2
# 0 <= fromi, toi < n
# All pairs (fromi, toi) are distinct.
# Accepted
# 87.1K
# Submissions
# 109.6K
# Acceptance Rate
# 79.5%


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:


# Easy Python algorithm operating under the following principles:

# First, assume that you need a set B with all nodes to visit the graph.
# Loop through the connections in the matrix edges (or A here), and remove nodes which can be reached from other points. (These nodes are no longer essential).
# Return the set B converted into a list: list(B).
# The previous algorithm is enough to reach a speed rating of 99% in LeetCode. If we think deeply, the previous solution would break in the presence of cycles, since all nodes in the cycle have a parent, and thus our solution set B would be empty. However, since the problem statement guarantees a unique solution, cycles cannot exist because any node in the cycle would create a different answer. As a result, we're implicitly guaranteed that cycles don't exist and that our simple algorithm works.

# I hope the explanation was helpful. This is an interesting problem.
# Cheers,

        # {0, 1, 2, 3, 4, 5}
        B = set(range(n))
        # go through every x and y in coordinates
        for x,y in edges:
            # if the exists in our set, remove it from the set
            # this means that it has an edge that leads to it(it can be traveled to)
            if y in B:
                B.remove(y)
            # {0, 2, 3, 4, 5}
            # {0, 3, 4, 5}
            # {0, 3, 4}
            # {0, 3}
            # {0, 3}
        # at the end, we will have our to nodes that arent visited by anyone
        # return them as a list
        return list(B)
