1314. Matrix Block Sum
Solved
Medium
Topics
Companies
Hint
Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.
 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, k <= 100
1 <= mat[i][j] <= 100
Accepted
81K
Submissions
107.3K
Acceptance Rate
75.5%

class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        # The goal is to compute the sum of each block of integers in the matrix, 
        # where each block is defined as a KxK submatrix.


        m, n = len(mat), len(mat[0])
        result = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                # top left corner
                r1, c1 = max(0, r - k), max(0, c - k)
                # lower right corner
                r2, c2 = min(m - 1, r + k), min(n - 1, c + k)
                
                # get all valujes within that range
                block_sum = 0
                for x in range(r1, r2 + 1):
                    for y in range(c1, c2 + 1):
                        block_sum += mat[x][y]
                
                result[r][c] = block_sum
        
        return result
