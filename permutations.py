# 567. Permutation in String
# Medium

# 7443

# 250

# Add to List

# Share
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.


class Solution(object):

    def checkInclusion(self, s1, s2):
        # check if the length of s1 is greater, if so, return False.
        # if s1 is longer, it definitly doesnt exit in s2
        if len(s1) > len(s2):
            return False

        # create two arrays that will hold the index of our inserted values
        # * 26 for the amount of letters in the alphabet
        s1lookup = [0] * 26
        s2lookup = [0] * 26
        # will keep track of our leftmost index
        j = 0
        # add chars to the lookups until the length of s1
        for i in range(len(s1)):
            s1lookup[ord(s1[i]) - ord('a')] += 1
            s2lookup[ord(s2[i]) - ord('a')] += 1

        # loop through the remaining characters
        for i in range(len(s1), len(s2)):
            if s1lookup == s2lookup:
                return True
            # remove the first char
            s2lookup[ord(s2[j]) - ord("a")] -= 1
            s2lookup[ord(s2[i]) - ord("a")] += 1
            # increase the leftmost index
            j+=1
        # check again if they are the equal
        return s1lookup == s2lookup
