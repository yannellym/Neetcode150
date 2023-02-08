# 695. Max Area of Island
# Medium
# 8.6K
# 192
# Companies
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

 

# Example 1:


# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # get the rows and cols' lengths
        rows = len(grid)
        cols = len(grid[0])
        # keeps track of the coordinates we have visited
        visited = set()

        # dfs helper function to check all surrounding squares
        def dfs(r,c):
            # if r < 0 -> we are out of bounds on the rows
            # if r == rows -> we are on the last row and cannot check further down
            # if c < 0 - > we are out of bounds on the cols
            # if c == cols -> we are on the last col and cannot check further to the right
            # if (r,c) in visited -> we have already visited this coordinate
            # if grid[r][c] == 0 -> this is not an island, just water
            if(r < 0 or r == rows or c < 0 or c == cols or (r,c) in visited or grid[r][c] == 0):
                # return 0 because none of these are valid towards our count of islands
                return 0
            # add the coordinate to the visited set
            visited.add((r,c))
            # recursively check is left, right, top, and bottom squares
            # add 1 to account for the island itself (The island you're looking at)
            return (1+ dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))
        # holds our max area
        area = 0
        # for each row in range of rows, and for each col in range of cols
        # have the area equal to the max between the area itself or the 
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r,c))
        # return the final calculation of area
        return area
