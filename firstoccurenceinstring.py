# 28. Find the Index of the First Occurrence in a String
# Medium

# 922

# 73

# Add to List

# Share
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle:
            return 0
        res = -1
        for i in range(len(haystack)- len(needle)+1):
            print(haystack[i])
            word = ""
            word = haystack[i] + haystack[i+1:i+len(needle)]
            print(word)
            if word == needle:
                res = i
                break
        return res
        
