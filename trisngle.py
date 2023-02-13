# 120. Triangle
# Medium
# 7.6K
# 461
# Companies
# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

# Example 1:

# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
# Example 2:

# Input: triangle = [[-10]]
# Output: -10
 

# Constraints:

# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104
 

# Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
# Accepted
# 564.7K
# Submissions
# 1M
# Acceptance Rate
# 54.3

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # create an array the length of triangle plus +1
        dp = [0] * (len(triangle)+1)
        # for each row in triangle, and starting at the last one
        for row in triangle[::-1]:
            # enumerate the row to get the index and the num itself
            for i, num in enumerate(row):
                # have dp[i] equal the num itself plus 
                # the minimum between dp[i] and dp[i+1]
                # this will be looking at each parent node and adding the min of its children
                dp[i] = num + min(dp[i], dp[i+1])
        # returns dp[0] because the answer will be store here by the end
        return dp[0]

        # this problem is basically a tree
        # it starts at the bottom and looks at the children of each node
        #  and chooses the one with the min value each time
