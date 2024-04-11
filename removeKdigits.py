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

        # for every digit in num
        for digit in num:
            # while we have a stack and we have k AND 
            # the top of the stack is GREATER than the current digit
            # pop the number from the top of the stack and minimize K
            while stack and k and digit < stack[-1]:
                stack.pop()
                k -=1
            # append the digit to the stack
            stack.append(digit)

        # there's a possibility that we might have a number like:
        # '00112' and our method above didnt work. So we would need to:
        # cut (k) numbers from the stack
        stack = stack[:len(stack)-k]
        # now, there might be the possibility that we have '00200'
        # we cant have leading zeros so we need to:
        # get the stack if we have a stack,if not just put "0"
        # then join the numbers in the stack or just "0"
        # convert to an int so it removes the leading zeroes (if any)
        # then convert to a string because our answer should be a STR
        return  str(int(''.join(stack if stack else "0")))


