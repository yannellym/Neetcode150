# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
 

# Follow up: Suppose there are lots of incoming s, say s1, s2, ...,
# sk where k >= 109, and you want to check one by one to see if t has its 
# subsequence. In this scenario, how would you change your code?

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0 
        
        # loops while i is less than the length of s and j is less than the length of t
        while i < len(s) and j < len(t):
            # if they are equal, increment the two pointers
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
            # if they are not equal, just increment j
            # this will allow you to keep comparing the current char in s 
            # and to not go out of bounds
                j += 1
        # at the end, compare if i is equal to the length of s. 
        # This will mean we went through the entire s string and are ready
        # to find our answer.
        # if i equals the length of s, it means there is a substring
        # if i != the length of s, it means we never increased i because it never matched to j.
        if i == len(s):
            return True
        return False
       
       # better solution
       
       class Solution(object):
         def isSubsequence(self, s, t):
             """
             :type s: str
             :type t: str
             :rtype: bool
             """
             if len(s) == 0:
                 return True

             if len(s) > len(t):
                 return False

             i = 0

             for char in t:
                 if char == s[i]:
                     i+=1
                 if i == len(s):
                     return True
             return False

