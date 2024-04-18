# 463. Island Perimeter
# Easy
# 5.3K
# 262
# Companies
# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example 1:


# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:

# Input: grid = [[1]]
# Output: 4
# Example 3:

# Input: grid = [[1,0]]
# Output: 4
 

# Constraints:

# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.
# Accepted
# 414.5K
# Submissions
# 595.6K
# Acceptance Rate

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # get the number of rows and columns
        rows = len(grid)
        cols = len(grid[0])
        # the perimeter will be initialized to 0
        perimeter = 0

        # for every row in the grid
        for i in range(rows):
            # for every colum in the grid
            for j in range(cols):
                # If it is an island (it equals 1), increment perimeter by 4
                if grid[i][j] == 1:
                    # lets automatically say that the perimeter is 4
                    perimeter += 4
                    # then, we check each neighbor and subtract 1 as needed.
                        # this will reduce the perimeter count if it is connected
                        # to any island (has a neighbor)
                    
                    # if its not the first row and the column at the row before that is 1:
                        # subtract from the perimeter ( its a neighbor )
                    if i>0 and grid[i-1][j] == 1: # check top 
                        perimeter -= 1
                    # if the row is within bounds and the column at the row below that is 1:
                        # subtract from the perimeter ( its a neighbor )
                    if i<rows-1 and grid[i+1][j] == 1: # check bottom
                        perimeter -= 1
                    # if the column is not the first column and the column at the row left to it is 1:
                    # subtract from the perimeter ( its a neighbor )  
                    if j>0 and grid[i][j-1] == 1: # check left
                        perimeter -= 1 
                    # if the column is within bounds and the column at the row right to it is 1:
                        # subtract from the perimeter ( its a neighbor )   
                    if j<cols-1 and grid[i][j+1] == 1:
                        perimeter -= 1
        # return the final count of the perimeter
        return perimeter


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
       

        """

        rows = len(grid)
        cols = len(grid[0])
        peri = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # check top
                    if r == 0 or grid[r-1][c] == 0:
                        peri += 1 
                    # check left
                    if c == 0 or grid[r][c-1] == 0:
                        peri += 1
                    # check right
                    if c == cols - 1 or grid[r][c+1] == 0:
                        peri += 1
                    # check bottom
                    if r == rows - 1 or grid[r+1][c] == 0:
                        peri += 1    

        # Perimeter value for all cells
        return peri
