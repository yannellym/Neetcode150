# 118. Pascal's Triangle
# Easy
# 9K
# 299
# Companies
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30


class Solution(object):
    def generate(self, numRows):
        res = [[1]]

        # we already added the first row so we need to do -1
        for i in range(numRows-1):
            temp = [0] + res[-1] + [0] 
            row = []
            # we are looping through the range of the last subarray in res + 1
            for j in range(len(res[-1]) + 1):
                # add the result of point j and j+1 to the row
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res
