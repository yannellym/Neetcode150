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
        # gives you the position of the letter
        # where each letter represents a = 0 to z=26
        lookup1 = [ord(x) - ord("a") for x in s1]
        lookup2 = [ord(y) - ord("a") for y in s2]

        # create two arrays of 26 0s to position the letters we will be looking at

        # will hold our letters from s1 and their corresponding positions
        target = [0] * 26
        # will serve as the window to hold the current letters from s2
        window = [0] * 26

        # go through each index(digit) in lookup1, add to the target array how often it appears
        for index in lookup1:
            target[index] +=1

        # loop through lookup2, by looking at its index, and value
        for index, value in enumerate(lookup2):
            # add 1 to the window's value 
            window[value] += 1
            # if the current index is greater than or equal to the length of s1:
            if index >= len(s1):
                # create a remaining variable by subtracting the length of s1 from 1
                # this will let you know the position of the character you need to subtract from in the window
                remaining = index - len(s1)
                # look for the letter in lookup2 by its index
                # look up the letter in the window with the letter from above, 
                # subtract 1
                window[lookup2[remaining]] -=1
            # if this window equals the target window, return true
            if window == target:
                return True
        # if the true statement above fails to execute, return false 
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
        
    
        
