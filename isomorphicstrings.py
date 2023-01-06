# 205. Isomorphic Strings
# Easy

# 5359

# 1014

# Add to List

# Share
# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
    
       # if one length is greater than the other, return false as the chars cant be replace to make up s
       if len(s) > len(t):
           return False
        # create two empty objects
        sToT = {}
        tToS = {}

        # for element in s and element in t
        for x, y in zip(s,t):
            # if element x is in sTot and the x element doesnt map to y, return false
            if x in sToT and sToT[x] != y:
                return False
            # if element y is in tToS and the y element doesnt map to x, return false
            if y in tToS and tToS[y] != x:
                return False
            # if they haven't been added yet, add them to the objects
            sToT[x] = y
            tToS[y] = x
        # if the "if" statements above fail to execute, that means every letter maps to each other,
        # we must return true as the strings are isomorphic. 
        return True
# better solution 

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False
        
        s_store = {}
        t_store = {}
        
        for i in range(len(s)):
            s_store[s[i]] = t[i]
            t_store[t[i]] = s[i]
            
        for i in range(len(s)):
                if s_store[s[i]] != t[i] or t_store[t[i]] != s[i]:
                    return False
        return True
        
