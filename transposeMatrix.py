# 867. Transpose Matrix
# Solved
# Easy
# Topics
# Companies
# Hint
# Given a 2D integer array matrix, return the transpose of matrix.

# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.



 

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:

# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 105

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        rows = len(matrix)
        cols = len(matrix[0])
        res = []

        for c in range(cols):
            temp = []
            for r in range(rows):
                temp.append( matrix[r][c] )
            res.append(temp)
        return res
# -109 <= matrix[i][j] <= 109
# Accepted
# 262.8K
# Submissions
# 401.3K
# Acceptance Rate
# 65.5%
