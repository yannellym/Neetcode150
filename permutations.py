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

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        lookup1 = [ord(i) - ord('a') for i in s1]
        lookup2 = [ord(i) - ord('a') for i in s2]
        
        '''
        lookup1 = [0,1]
        lookup2[4,8,3,1,0,14,14,14]
        '''
        
        #set up the arrays of 26
        target = [0] * 26
        window = [0] * 26
        
        #look up each char in lookup1 and increase that char(index) in target array
        for freq in lookup1:
            target[freq] += 1
        '''target = [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'''
        
        for i, freq in enumerate(lookup2):
            # add it to the current window
            window[freq] += 1
            #if the window size (i) is exceeded
            if i >= len(s1):
                remaining = i - len(s1)
                window[lookup2[remaining]] -=1
            if window == target:
                return True
        return False
    
    # round 1: 
    '''
    remaining = 0
    lookup2[remaining] = 4
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    '''
     # round 2: 
    '''
    remaining = 1
    lookup2[remaining] = 8
    [0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    '''
     # round 3: 
    '''
    remaining = 2
    lookup2[remaining] = 3
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    '''
        
    
        
                
    
