840. Magic Squares In Grid
Solved
Medium
Topics
Companies
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

 

Example 1:


Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:

while this one is not:

In total, there is only one magic square inside the given grid.
Example 2:

Input: grid = [[8]]
Output: 0
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15
Seen this question in a real interview before?
1/5
Yes
No
Accepted
128.5K
Submissions

class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nrows = len(grid)
        ncols = len(grid[0])
        total_c = 0

        def is_magic(r, c):
            # Get all the values in the 3x3 subgrid
            values = [
                grid[r][c], grid[r][c+1], grid[r][c+2],
                grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]
            ]

            # Check if values contain all numbers from 1 to 9
            if sorted(values) != list(range(1, 10)):
                return False

            # Calculate the sum of rows, columns, and diagonals
            row1 = grid[r][c] + grid[r][c+1] + grid[r][c+2]
            row2 = grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2]
            row3 = grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2]
            col1 = grid[r][c] + grid[r+1][c] + grid[r+2][c]
            col2 = grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1]
            col3 = grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2]
            diag1 = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]
            diag2 = grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c]

            # All rows, columns, and diagonals should sum to 15
            return row1 == row2 == row3 == col1 == col2 == col3 == diag1 == diag2 == 15

        # Traverse the grid to check each 3x3 subgrid
        for r in range(nrows - 2):
            for c in range(ncols - 2):
                if is_magic(r, c):
                    total_c += 1 

        return total_c
