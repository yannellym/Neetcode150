1277. Count Square Submatrices with All Ones
Solved
Medium
Topics
Companies
Hint
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
Accepted
205.8K
Submissions
275.1K
Acceptance Rate
74.8%

class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])
        count = 0
        copymatrix = [[0] * cols for _ in range(rows)]


        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0:
                        copymatrix[r][c] = 1
                    else:
                        copymatrix[r][c] = min(copymatrix[r][c-1], copymatrix[r-1][c], copymatrix[r-1][c-1]) + 1
                    count += copymatrix[r][c]
        return count


        '''dp[i-1][j]:

This represents the side length of the largest square submatrix that ends at cell (i-1, j) and extends downward. It is essentially checking the cell directly above the current cell (i, j).
dp[i][j-1]:

This represents the side length of the largest square submatrix that ends at cell (i, j-1) and extends to the right. It is essentially checking the cell directly to the left of the current cell (i, j).
dp[i-1][j-1]:

This represents the side length of the largest square submatrix that ends at cell (i-1, j-1) and extends diagonally downward and to the right. It is essentially checking the cell diagonally up and to the left of the current cell (i, j).
'''

# it checks like this
# | 0 | 0 |< 0 | 0 |
# -----------
# | 1 | 1 | <1 | 1 |
# -^^^^^^^^^^----------
# | 0 | 0 | 0 | 0 |
# -----------
