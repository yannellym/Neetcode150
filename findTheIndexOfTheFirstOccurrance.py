# 28. Find the Index of the First Occurrence in a String
# Medium
# 2.6K
# 131
# Companies
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
# Accepted
# 1.6M
# Submissions
# 4.1M
# Acceptance Rate
# 38.6

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # iterate through i
        for i in range(len(haystack)):
            # if the letter at index i of haystack is equal to the first letter in needle
            if haystack[i] == needle[0]:
                # check if the haystack word starting at i and ending at i + length of needle equal the needle word
                if haystack[i:i+len(needle)] == needle:
                    # if it does, return i because its the first index
                    return i
        # if it doesnt exist, return -1
        return -1 
        
