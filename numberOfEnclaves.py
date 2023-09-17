1020. Number of Enclaves
Medium
Topics
Companies
Hint
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:


Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
Accepted
182.4K
Submissions
265.3K
Acceptance Rate
68.8%
 class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        res = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return

            grid[r][c] = 0  # Mark as visited

            # Explore adjacent cells
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Mark land cells on the left and right boundaries as visited
        for r in range(rows):
            if grid[r][0] == 1:
                dfs(r, 0)  # Start DFS from the left boundary if it's land
            if grid[r][cols - 1] == 1:
                dfs(r, cols - 1)  # Start DFS from the right boundary if it's land

        # Mark land cells on the top and bottom boundaries as visited
        for c in range(cols):
            if grid[0][c] == 1:
                dfs(0, c)  # Start DFS from the top boundary if it's land
            if grid[rows - 1][c] == 1:
                dfs(rows - 1, c)  # Start DFS from the bottom boundary if it's land

        # Count the remaining unvisited land cells
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res += 1

                dfs(rows - 1, c)

        # Count the remaining unvisited land cells
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res += 1

        return res
