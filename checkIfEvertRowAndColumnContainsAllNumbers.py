2133. Check if Every Row and Column Contains All Numbers
Solved
Easy
Topics
Companies
Hint
An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

 

Example 1:


Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true
Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
Hence, we return true.
Example 2:


Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
Output: false
Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
Hence, we return false.
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
1 <= matrix[i][j] <= n
Accepted
59.3K
Submissions
114.8K
Acceptance Rate
51.7%


class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            row = matrix[r]
            column = [matrix[c][r] for c in range(cols)]
            
            row_set = set(row)
            column_set = set(column)
            
            if row_set != set(range(1, cols + 1)) or column_set != set(range(1, rows + 1)):
                return False

        return True
