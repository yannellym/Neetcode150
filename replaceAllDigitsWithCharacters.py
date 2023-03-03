# 1844. Replace All Digits with Characters
# Easy
# 619
# 58
# Companies
# You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.

# There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.

# For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
# For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).

# Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.

 

# Example 1:

# Input: s = "a1c1e1"
# Output: "abcdef"
# Explanation: The digits are replaced as follows:
# - s[1] -> shift('a',1) = 'b'
# - s[3] -> shift('c',1) = 'd'
# - s[5] -> shift('e',1) = 'f'
# Example 2:

# Input: s = "a1b2c3d4e"
# Output: "abbdcfdhe"
# Explanation: The digits are replaced as follows:
# - s[1] -> shift('a',1) = 'b'
# - s[3] -> shift('b',2) = 'd'
# - s[5] -> shift('c',3) = 'f'
# - s[7] -> shift('d',4) = 'h'
 

# Constraints:

# 1 <= s.length <= 100
# s consists only of lowercase English letters and digits.
# shift(s[i-1], s[i]) <= 'z' for all odd indices i.
# Accepted
# 58K
# Submissions
# 72.4K
# Acceptance Rate
# 80.1%

class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        
        ans = ""
        # for i in the range of the length of s
        for i in range(len(s)):
            # if the digit at index i is numeric
            if s[i].isnumeric():
                # to the ans str add:
                # the ord result of the char before PLUS the int version of the current char
                ans+= chr(ord(s[i-1])+int(s[i]))
            else:
                # if its not numeric, just add it to the answer
                ans+= s[i]
        return ans

        

