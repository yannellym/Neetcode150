# 14. Longest Common Prefix
# Easy

# 11269

# 3518

# Add to List

# Share
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
# Accepted
# 1,995,416
# Submissions
# 4,890,764

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        origin = strs[0]
        
        for i in range(len(origin)):
            for word in strs:
              # this will evaluate the left first. Then, the right. 
              # the left statement is to catch if i goes out of bounds.
                if i == len(word) or word[i] != origin[i]:
                    return res
            res += origin[i]
        return res
            
