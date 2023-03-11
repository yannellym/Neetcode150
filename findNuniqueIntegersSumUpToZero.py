# 1304. Find N Unique Integers Sum up to Zero
# Easy
# 1.6K
# 546
# Companies
# Given an integer n, return any array containing n unique integers such that they add up to 0.

 

# Example 1:

# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
# Example 2:

# Input: n = 3
# Output: [-1,0,1]
# Example 3:

# Input: n = 1
# Output: [0]
 

# Constraints:

# 1 <= n <= 1000
# Accepted
# 180K
# Submissions
# 233.9K
# Acceptance Rate
# 77.0%

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        result = []
        # iterate over half of the array (from 1 to n//2) 
        for i in range(1, n // 2 + 1):
            # assigns each positive integer i to the ith element of result 
            # the negative integer -i to the (n-i)th element of result.
            result.extend([i, -i])
        if n % 2 != 0:
            result.append(0)
        return result

        # Ex.for n = 5
        # i in range 1-2
          # first, res[1] = 1 and res[-1] = -1
        # [1,-1]
           # second, res[2] = 2 and res[-2] = -2
        # [ 1, -1, 2, -2]
        #  add the 0 if its odd
        # [ 1, -1, 2, -2, 0]
