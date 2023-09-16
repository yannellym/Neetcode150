2428. Maximum Sum of an Hourglass
Solved
Medium
Topics
Companies
Hint
You are given an m x n integer matrix grid.

We define an hourglass as a part of the matrix with the following form:


Return the maximum sum of the elements of an hourglass.

Note that an hourglass cannot be rotated and must be entirely contained within the matrix.

 

Example 1:


Input: grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
Output: 30
Explanation: The cells shown above represent the hourglass with the maximum sum: 6 + 2 + 1 + 2 + 9 + 2 + 8 = 30.
Example 2:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: 35
Explanation: There is only one hourglass in the matrix, with the sum: 1 + 2 + 3 + 5 + 7 + 8 + 9 = 35.
 

Constraints:

m == grid.length
n == grid[i].length
3 <= m, n <= 150
0 <= grid[i][j] <= 106
Accepted
32K
Submissions
42.8K
Acceptance Rate
74.7% \


class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        maxtotal = float('-inf')  # Initialize maxtotal with negative infinity

        def check(r, c):
            if r + 2 >= rows or c + 2 >= cols:
                return 0
            toprow = sum(grid[r][c:c+3])
            bottomrow = sum(grid[r+2][c:c+3])
            mid = grid[r+1][c+1]
            return toprow + bottomrow + mid

        for r in range(rows-2):
            for c in range(cols-2):
                maxtotal = max(maxtotal, check(r, c))

        return maxtotal
