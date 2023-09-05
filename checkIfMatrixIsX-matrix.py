# 2319. Check if Matrix Is X-Matrix
# Solved
# Easy
# Topics
# Hint
# A square matrix is said to be an X-Matrix if both of the following conditions hold:

# All the elements in the diagonals of the matrix are non-zero.
# All other elements are 0.
# Given a 2D integer array grid of size n x n representing a square matrix, return true if grid is an X-Matrix. Otherwise, return false.

 

# Example 1:


# Input: grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
# Output: true
# Explanation: Refer to the diagram above. 
# An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
# Thus, grid is an X-Matrix.
# Example 2:


# Input: grid = [[5,7,0],[0,3,1],[0,5,0]]
# Output: false
# Explanation: Refer to the diagram above.
# An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
# Thus, grid is not an X-Matrix.
 

# Constraints:

# n == grid.length == grid[i].length
# 3 <= n <= 100
# 0 <= grid[i][j] <= 105
# Accepted
# 43.5K
# Submissions
# 66.3K
# Acceptance Rate
# 65.6% 



class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        diagonals = []
        for c in range(cols):
            diagonals.append(grid[0+c][c])
            visited.add((0+c,c))

        for c in range(cols-1, -1, -1):
            diagonals.append(grid[cols - 1 - c][c])
            visited.add((cols - 1 - c,c))
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in visited:
                    continue
                if grid[r][c] != 0:
                    return False
        return all(x for x in diagonals)
