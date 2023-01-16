
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
 

# Constraints:

# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.

# https://www.youtube.com/watch?v=G8xtZy0fDKg&list=PLot-Xpze53leOBgcVsJBEGrHPd_7x_koV&index=5
def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # if th elength of p is greater than the legth of s:
         # this means it can't possible be an anagram in s
         # return an empty array
        if len(p) > len(s):
            return []
        # create two empty dictionaries
        sDict = {}
        pDict = {}
        # declare win_Start as 0. It will be the beginning of our window.
        win_start = 0
        # res will store our answer with indexes
        res = []
       
        # loop j amount of times with j being the length of p
        for j in range(len(p)):
            # add each char to its prospective dictionary.
            # if its in there already, add 1. Else, set it to 0
            sDict[s[j]] = 1 + sDict.get(s[j], 0)
            pDict[p[j]] = 1 + pDict.get(p[j], 0)
        # the two dictionaries are the same, append 0 to the res array
          # this mean that index 0 is the beginning of an anagram
        if sDict == pDict:
            res.append(0)
        # loop until the length of s, starting at the length of p 
         # (we already checked the first j chars)
        for win_end in range(len(p), len(s)):
            # subtract from the char at the beginning of the window
            # add the char at the end of our window to the dict
            sDict[s[win_start]] -= 1
            sDict[s[win_end]] =  1 + sDict.get(s[win_end], 0)
            # if the char we subtracted from now equals 0, just pop it
            if sDict[s[win_start]] == 0:
                sDict.pop(s[win_start])
            # update the start of our window by 1
            win_start += 1
            # if both the dictionaries are the same again, that means it's an anagram
            if sDict == pDict:
                # append the index to the res array
                res.append(win_start)
        return res
