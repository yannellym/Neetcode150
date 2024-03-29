# 459. Repeated Substring Pattern
# Easy
# 4.6K
# 420
# company
# Apple
# company
# Google
# company
# Amazon
# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: s = "aba"
# Output: false
# Example 3:

# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.
# Accepted
# 312.2K
# Submissions
# 714.2K
# Acceptance Rate
# 43.7%

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s + s)[1:-1]
        # if the original string is present in this modified concatenated string, it indicates that the original string can be obtained by repeating a substring.
