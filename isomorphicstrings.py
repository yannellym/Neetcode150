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

# if one length is greater than the other, return false as the chars cant be replace to make up s
if len(s) > len(t):
    return False
        
        s_store = {}
        t_store = {}
        
        for i in range(len(s)):
        # add the chars and values to each dict.
            s_store[s[i]] = t[i]
            t_store[t[i]] = s[i]
        # loop nth amount of times, where nth equals the length of s.   
        for i in range(len(s)):
            # if the value of the ith char of s_store doesnt equal the value of the ith char in t_store:return false.
            if s_store[s[i]] != t[i] or t_store[t[i]] != s[i]:
                return False
         #if everything else fails, return true
        return True
        
