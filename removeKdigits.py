# 402. Remove K Digits
# Medium
# 7.5K
# 317
# Companies
# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:

# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

# Constraints:

# 1 <= k <= num.length <= 105
# num consists of only digits.
# num does not have any leading zeros except for the zero itself.
# Accepted
# 308.8K
# Submissions
# 1M
# Acceptance Rate
# 30.6%

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        stack = []
        if len(num) == 1: return "0"

        for digit in num:
            while stack and stack[-1] > digit and k :
                stack.pop()
                k -=1
            
            stack.append(digit)
        # this could be a stack like this "0112" k=1
        # we need to make sure that if we still have a k, we take out the kth digit
        stack = stack[: len(stack)-k] 
        # the stack might be empty, if so, return a "0"
        return str(int(''.join(stack if stack else "0")))

