# 62. Unique Paths
# Medium
# 12.9K
# 370
# Companies
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
 

# Constraints:

# 1 <= m, n <= 100
# Accepted
# 1.3M
# Submissions
# 2.1M
# Acceptance Rate
# 62.5%

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # create a row the length of n as it is as wide as the grid
        # ex n=7 [1,1,1,1,1,1,1]
        row = [1] * n 

        # this will check through each row(3 rows in total)
        for i in range(m-1):
            # create a temporary new row. Have it equal the length of n again
            # ex n=7 [1,1,1,1,1,1,1]
            newRow = [1] * n
            # this time, start from the 5th position in the row(0 indexed array)
            # you'll have a value to the right to compare
            # ex [1,1,1,1,1,(1),1]
            for j in range(n-2,-1,-1):
                # have the current row position equal the value to the right(newRow[j+1])
                # plus the value down row[j]
                newRow[j] = newRow[j+1] + row[j]
            # set row to equal the newRow
            row = newRow
        # the sum of the computed values will be in row 0 since its the last index checked
        return row[0]
