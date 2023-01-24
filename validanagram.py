# 242. Valid Anagram
# Easy
# 8.1K
# 261
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# Accepted
# 1.9M
# Submissions
# 3.1M
# Acceptance Rate
# 62.9%


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        
        """

        # if the length of t is less than the length of s:
        # that means its automatically not an anagram. Return False
        if len(s) > len(t):
            return False
        
        # create two dicts
        dict1 = {}
        dict2 = {}
        
        # Add each char to its dict
        for i in s:
            dict1[i] = 1 + dict1.get(i, 0)

        # Add each char to its dict
        for j in t:
            dict2[j] = 1 + dict2.get(j, 0)

        # if the dicts are the same, return true because they are anagrams
        # they have the same letter count  
        return dict1 == dict2

        # Alternative 

        # # if the length of t is less than the length of s:
        # # that means its automatically not an anagram. Return False
        # if len(t) < len(s):
        #     return False
        # # create two dicts
        # tcount = Counter(t)
        # scount = Counter(s)

        # # for every letter in t
        # for letter in t:
        #     # if the letter is in s'dict and the count of it is greater than 0 
        #     if letter in scount and scount[letter] >0:
        #         # subtract 1 from the s'dict' count
        #         # this mean that we were able to get another letter
        #         scount[letter] -= 1
        #     # if its not in scount or the value is less than 0
        #     # this means we dont have enough letters or its not in scount
        #     else:
        #         # return false because its not an anagram
        #         return False
        # # check if all are true in : return true for every value in sdict if the value equals 0
        # return all([True for x in scount if scount[x] == 0])
