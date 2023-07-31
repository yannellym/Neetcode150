# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.

class Solution:
    def orangesRotting(self, grid):
        fresh_oranges = set()
        rotten_oranges = []

        # Find all fresh and rotten oranges
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:  # If the cell contains a fresh orange
                    fresh_oranges.add((i, j))  # Add its coordinates to the 'fresh_oranges' set
                elif grid[i][j] == 2:  # If the cell contains a rotten orange
                    rotten_oranges.append((i, j))  # Add its coordinates to the 'rotten_oranges' list

        minutes = 0
        while fresh_oranges and rotten_oranges:
            new_rotten = []
            for i, j in rotten_oranges:  # For each rotten orange
                # Check all four neighbors
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if (x, y) in fresh_oranges:  # If the neighbor is a fresh orange
                        fresh_oranges.remove((x, y))  # Convert it to rotten by removing it from 'fresh_oranges'
                        new_rotten.append((x, y))  # Add the converted rotten orange coordinates to 'new_rotten'
            rotten_oranges = new_rotten  # Update 'rotten_oranges' with the new rotten oranges
            minutes += 1  # Increment the minutes elapsed

        # Check if there are any fresh oranges left and return accordingly
        return -1 if fresh_oranges else minutes


        # Time Compelxity: O(m * n)
        # Space Complexity: O(m * n)
