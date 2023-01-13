# 2500. Delete Greatest Value in Each Row
# Easy
# 219
# 14
# Companies
# You are given an m x n matrix grid consisting of positive integers.

# Perform the following operation until grid becomes empty:

# Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
# Add the maximum of deleted elements to the answer.
# Note that the number of columns decreases by one after each operation.

# Return the answer after performing the operations described above.

 

# Example 1:


# Input: grid = [[1,2,4],[3,3,1]]
# Output: 8
# Explanation: The diagram above shows the removed values in each step.
# - In the first operation, we remove 4 from the first row and 3 from the second row (notice that, there are two cells with value 3 and we can remove any of them). We add 4 to the answer.
# - In the second operation, we remove 2 from the first row and 3 from the second row. We add 3 to the answer.
# - In the third operation, we remove 1 from the first row and 1 from the second row. We add 1 to the answer.
# The final answer = 4 + 3 + 1 = 8.
# Example 2:


# Input: grid = [[10]]
# Output: 10
# Explanation: The diagram above shows the removed values in each step.
# - In the first operation, we remove 10 from the first row. We add 10 to the answer.
# The final answer = 10.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j] <= 100
# Accepted
# 21.7K
# Submissions
# 26.2K
# Acceptance Rate
# 82.9%


class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # save the length of the first subarray in a variable. This will tell you how many rows
        rows = len(grid[0])
        # this will hold our final result
        res = 0

        # check through every row
        for _ in range(rows):
            # this will hold a temporary maxvalue variable, which is initially 0
            maxval = 0
            # check through each subarray in the grid
            for j in grid:
                # obtain the max of each subarray
                maxi = max(j)
                # update our maxval variable above to equal the max between
                 # our maxval and this new max value
                 # this will continue to get the max of each row
                maxval = max(maxi, maxval)
                # remove the max from number you got from each subarray
                j.remove(maxi)
            # update our res variable to include this max value of all the rows we visited
            res += maxval
        # return the final max value after we visit all the rows
        return res
