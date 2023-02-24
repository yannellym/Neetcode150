# 326. Power of Three
# Easy
# 2.5K
# 237
# Companies
# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

 

# Example 1:

# Input: n = 27
# Output: true
# Explanation: 27 = 33
# Example 2:

# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.
# Example 3:

# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).
 

# Constraints:

# -231 <= n <= 231 - 1
 

# Follow up: Could you solve it without loops/recursion?
# Accepted
# 654.8K
# Submissions
# 1.4M
# Acceptance Rate
# 45.4%

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        # while the number modulo 3 == 0 (number is product of 3)
        while(n%3 == 0):
            # have n equal to the number / 3
            # this will get you down to the smallest divisor
            n = n//3
        # at the end, if n == 1, it means that we have a power of 3
        # the last number n will equal to would be 3 and 3 % 3 = 1
        return n == 1
