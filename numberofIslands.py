# 200. Number of Islands
# Medium
# 18.5K
# 410
# Companies
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # get the num of rows and columns in the grid
        m = len(grid)
        n = len(grid[0])


        def mark(r, c):
            # create a stack initialized with [r,c] = [0,0]
            stack = [(r, c)]
            # while there are things in the stack
            while stack:
                # pop the last element(tuple inside)
                r, c = stack.pop()
                # if there's a row above AND the coordinate is '1' AND the coordinate is not in the stack
                  # add that new coordiante to the stack
                if r - 1 >= 0 and grid[r - 1][c] == '1' and (r - 1, c) not in stack:
                    stack.append((r - 1, c))
                # if there's a row below AND the coordinate is '1' AND the coordinate is not in the stack
                  # add that new coordiante to the stack
                if r + 1 < m and grid[r + 1][c] == '1' and (r + 1, c) not in stack:
                    stack.append((r + 1, c))
                # if there's a row right AND the coordinate is '1' AND the coordinate is not in the stack
                  # add that new coordiante to the stack
                if c + 1 < n and grid[r][c + 1] == '1' and (r, c + 1) not in stack:
                    stack.append((r, c + 1))
                # if there's a row left AND the coordinate is '1' AND the coordinate is not in the stack
                  # add that new coordiante to the stack
                if c - 1 >= 0 and grid[r][c - 1] == '1' and (r, c - 1) not in stack:
                    stack.append((r, c - 1))
                # set the coordinate to equal 2, as it is visited
                grid[r][c] = 2
        
        # this will be 0 initially
        res = 0
        # go through each row, and column
        for i in range(m):
            for j in range(n):
                # if it equals '1', add it to the res count
                if grid[i][j] == '1':
                    res += 1
                    # call the mark func to mark all th enode that are visited
                    mark(i, j)
        # return the count of the islands
        return res
