# 1743. Restore the Array From Adjacent Pairs
# Medium
# 926
# 22
# company
# Uber
# company
# Quora
# company
# Capital One
# There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

# You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

# It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

# Return the original array nums. If there are multiple solutions, return any of them.

 

# Example 1:

# Input: adjacentPairs = [[2,1],[3,4],[3,2]]
# Output: [1,2,3,4]
# Explanation: This array has all its adjacent pairs in adjacentPairs.
# Notice that adjacentPairs[i] may not be in left-to-right order.
# Example 2:

# Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
# Output: [-2,4,1,-3]
# Explanation: There can be negative numbers.
# Another solution is [-3,1,4,-2], which would also be accepted.
# Example 3:

# Input: adjacentPairs = [[100000,-100000]]
# Output: [100000,-100000]
 

# Constraints:

# nums.length == n
# adjacentPairs.length == n - 1
# adjacentPairs[i].length == 2
# 2 <= n <= 105
# -105 <= nums[i], ui, vi <= 105
# There exists some nums that has adjacentPairs as its pairs.
# Accepted
# 35.5K
# Submissions
# 51.6K
# Acceptance Rate
# 68.7%

class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """

        graph = defaultdict(list)


        # Build the adjacency list representation of the graph
        for pair in adjacentPairs:
            u, v = pair[0], pair[1]
            graph[u].append(v)
            graph[v].append(u)

        '''
        2 -> [1,3]
        1 -> [2]
        3 -> [4,2]
        4 -> [3]
        '''
        
        # Find the start node of the array (a node with only one adjacent node)
        start_node = None
        for node in graph:
            if len(graph[node]) == 1:
                start_node = node
                print(node) # for example one, the first node with one adjacent node only is 1
                break
        
        # Traverse the graph to reconstruct the original array
        result = []
        visited = set()
        self.dfs(graph, start_node, visited, result)
        
        return result

    def dfs(self,graph, node, visited, result):
        # add the node to visited and to the result 
        visited.add(node)
        result.append(node)
        
        # for every digit in the graphs[node]'s array
        for neighbor in graph[node]:
            # if its not in visited
            if neighbor not in visited:
                # call dfs again, passs in the graph, the neighbor, visited and result.
                self.dfs(graph, neighbor, visited, result)
