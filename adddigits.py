# 258. Add Digits
# Easy
# 3.2K
# 1.8K
# Companies
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

# Example 1:

# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.
# Example 2:

# Input: num = 0
# Output: 0
 

# Constraints:

# 0 <= num <= 231 - 1
 

# Follow up: Could you do it without any loop/recursion in O(1) runtime?

# Accepted
# 546.6K
# Submissions
# 856K
# Acceptance Rate

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
    # approach #1
        # res = str(num)

        # while len(res) > 1:
        #     str_num = list(res)
        #     total = 0
        #     for i in str_num:
        #         total += int(i)
        #     res = str(total)
        # return int(res)
        
        # approach #2
#         while num >= 10:
#             num_str = str(num)
#             digit_sum = 0
#             for digit in num_str:
#                 digit_sum += int(digit)
#             num = digit_sum
#         return num

        # approach #3
        if num == 0 : return 0
        if num % 9 == 0 : return 9
        else : return (num % 9)

        #https://leetcode.com/problems/add-digits/solutions/1754046/java-c-python-solution-with-math-s-explained/
