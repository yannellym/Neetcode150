# 119. Pascal's Triangle II
# Easy
# 3.5K
# 293
# Companies
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]
 

# Constraints:

# 0 <= rowIndex <= 33
 

# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

# Accepted
# 642.7K
# Submissions
# 1.1M
# Acceptance Rate
# 60.3%


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # the first row will always be 1
        res = [ [1] ]
        # loop rowIndex amount of times to make sure we get the last row we need,
        # we already added the first row.
        for i in range(rowIndex):
            level = []
            temp = [0] + res[-1] + [0]
            # loop the amount of time of the length of the last subarray, + 1 for a new level
            for j in range(len(res) + 1):
                # go through the temp and add the 1st and 2nd together, 2nd and 3rd..so on.
                level.append(temp[j]+temp[j+1])
            # append the level to the res
            res.append(level)
        # get the last row only
        return res[-1]
