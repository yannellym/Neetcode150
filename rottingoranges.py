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

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        fresh, rotten = set(), deque()

        # iterate through the grid to get all the fresh and rotten oranges
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # if we see a fresh orange, put its position in fresh
                if grid[row][col] == 1:
                    fresh.add((row, col))

                # if we see a rotten orange, put its position in rotten
                elif grid[row][col] == 2:
                    rotten.append((row, col))

        minutes = 0
        while fresh and rotten:

            minutes += 1

            # iterate through rotten, popping off the (row, col) that's currently in rotten
            # we don't touch the newly added (row, col) that are added during the loop until the next loop
            for rot in range(len(rotten)):
                row, col = rotten.popleft()

                for direction in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if direction in fresh:
                        # if the (row, col) is in fresh, remove it then add it to rotten
                        fresh.remove(direction)
                        # we will perform 4-directional checks on each (row, col)
                        rotten.append(direction)

        # if fresh is not empty, then there is an orange we were not able to reach 4-directionally    
        return -1 if fresh else minutes

        # Time Compelxity: O(m * n)
        # Space Complexity: O(m * n)
