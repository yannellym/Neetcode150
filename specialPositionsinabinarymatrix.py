# 1582. Special Positions in a Binary Matrix
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an m x n binary matrix mat, return the number of special positions in mat.

# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

# Example 1:


# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
# Example 2:


# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# mat[i][j] is either 0 or 1.
# Accepted
# 44K
# Submissions
# 67.5K
# Acceptance Rate
# 65.1%
  
  class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        row_sums = [0] * m  # Initialize a list to store the sum of each row
        col_sums = [0] * n  # Initialize a list to store the sum of each column
        special_count = 0  # Initialize a counter for special positions

        # Calculate the sums of rows and columns
        for r in range(m):
            for c in range(n):
                row_sums[r] += mat[r][c]
                col_sums[c] += mat[r][c]

        # Check each cell to see if it's a special position
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1 and row_sums[r] == 1 and col_sums[c] == 1:
                    special_count += 1

        return special_count
