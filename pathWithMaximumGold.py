1219. Path with Maximum Gold
Solved
Medium
Topics
Companies
Hint
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
201.3K
Submissions
296.4K


class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(row, col, path_sum):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0:
                return path_sum

            # Mark the cell as visited
            original_value = grid[row][col]
            grid[row][col] = 0

            # Explore all four directions
            max_gold = path_sum
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + dr, col + dc
                max_gold = max(max_gold, dfs(new_row, new_col, path_sum + original_value))

            # Backtrack by restoring the original value
            grid[row][col] = original_value
            return max_gold
            

        m, n = len(grid), len(grid[0])
        max_gold = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] != 0:
                    max_gold = max(max_gold, dfs(row, col, 0))

        return max_gold

