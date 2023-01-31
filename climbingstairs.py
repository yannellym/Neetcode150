# 70. Climbing Stairs
# Easy

# 14589

# 430

# Add to List

# Share
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45
# Accepted
# 1,889,922
# Submissions
# 3,656,588

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a
# alternative

def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        for _ in range(n-1):
            tmp = a
            a = a+b
            b = tmp
        return a
