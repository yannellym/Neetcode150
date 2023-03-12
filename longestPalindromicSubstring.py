#  Longest Palindromic Substring
# Medium
# 23.8K
# 1.4K
# Companies
# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# Accepted
# 2.3M
# Submissions
# 7.1M
# Acceptance Rate
32.4%


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        size = len(s)
        # while size > 0 
        while(size>0):
            # loop length of s - (size + 1) times
            for i in range(len(s) - size + 1):
                # x will equal the substring of s from i to i plus size
                x = s[i:i+size]
                # if x equals the reverse of x return x
                # this returns the first palindromic substring it sees.
                # since're we starting with the entire array, it will automatically return the longest one
                if x == x[::-1]:
                    return x
            # decrement size
            size -= 1

        
   # ex babad -> 0 - 5
        #   baba  -> 0 - 4
        #   abad -> 1 - 4
        #   bab -> 0 - 3
