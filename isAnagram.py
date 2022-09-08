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

#try
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
    
#try.  O(s + t)
class Solution(object):
    def isAnagram(self, s, t):
    
        def dicted(l):
            count = {}
            for x in l:
                if x not in count:
                    count[x] = 0
                count[x] += 1
            return count

        return dicted(s) == dicted(t)
      
 #optimal solution
 
 def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
       
       
  #optional solution
  
     def isAnagram(self, s, t):
        tracker = collections.defaultdict(int)
        for x in s: tracker[x] += 1
        for x in t: tracker[x] -= 1
        return all(x == 0 for x in tracker.values())

