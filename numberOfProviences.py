# 547. Number of Provinces
# Medium
# 7.7K
# 293
# company
# Amazon
# company
# Bloomberg
# company
# DoorDash
# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 

# Example 1:


# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:


# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
 

# Constraints:

# 1 <= n <= 200
# n == isConnected.length

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        
        n = len(isConnected)  # Get the number of cities
        numProvinces = 0  # Initialize the number of provinces to 0
        visited = [False] * n  # Initialize an array to keep track of visited cities

        def dfs(city, isConnected, visited):
            visited[city] = True  # Mark the current city as visited
            for neighbor in range(n):  # Iterate over neighboring cities
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    # If the neighbor is connected to the current city and not visited,
                    # recursively call dfs on the neighbor
                    dfs(neighbor, isConnected, visited)

        for i in range(n):  # Iterate over each city
            if not visited[i]:  # If the city hasn't been visited, it is part of a new province
                numProvinces += 1  # Increment the number of provinces
                dfs(i, isConnected, visited)  # Call dfs to visit all connected cities in the province

        return numProvinces  # Return the total number of provinces

# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]
# Accepted
# 632.8K
# Submissions
# 988.2K
# Acceptance Rate
# 64.0%
