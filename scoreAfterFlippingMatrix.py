861. Score After Flipping Matrix
Solved
Medium
Topics
Companies
You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).

 

Example 1:


Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
Example 2:

Input: grid = [[0]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid[i][j] is either 0 or 1.
Accepted
44.2K
Submissions
59.1K
Acceptance Rate
74.9%

class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        # Step 1: Ensure the leftmost column has all  by changing the value in each row
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]
        print(grid)

        # Step 2: Ensure each column has more 1s than 0s
        for j in range(1, n):
            # counts all 1s in the column j
            ones_count = sum(grid[i][j] for i in range(m))
            # compare this count to half the number of rows plus one. (m + 1) // 2 
            # calculates the integer division of m + 1 by 2. This value represents the minimum 
            # number of 1s required to ensure that there are more 1s than 0s in a column.
            if ones_count < (m + 1) // 2:
                # if the count is less than the required amount, iterate through row i
                for i in range(m):
                    # change the value of cell[i][j] (from 0 to 1 and 1 to 0)
                    grid[i][j] = 1 - grid[i][j]

        # Step 3: Calculate the score
        score = 0
        for i in range(m):
            # join the row of numbers into a string
            binary_row = ''.join(map(str, grid[i]))
            decimal_value = int(binary_row, 2)
            score += decimal_value

        return score
