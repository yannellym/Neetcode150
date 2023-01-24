# 383. Ransom Note
# Easy
# 3.6K
# 396
# Companies
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # create two dicts 
        mag = {}
        ran = {}

        # input the the count of the letters in the mag dict
        for i in magazine:
            # if the value is in mag, add 1
            # if its not in mag, add it, and add 1
            mag[i] = 1 + mag.get(i, 0)
        # for every letter in ransomNote
        for letter in ransomNote:
            # if the letter is in mag dict, and 
            # the value is greater than 0 (means we can subtract from it)
            if letter in mag and mag[letter] >0:
                # subtract 1 from the letter in mag
                mag[letter] -= 1
                # add it to the count of the letter in ran
                ran[letter] = 1 + ran.get(letter, 0)
            # if its not in mag or the count is <= 0
            else:
                # return false because its not there or we cant subtract from it
                return False
        # if we get to this point, return true because we have the letters we need
        return True
      
      
         # Alternative solution
        # # for every letter in ransomnote
        # for char in ransomNote:
        #     # if the letter is in the magazine
        #     if char in magazine:
        #         # set the magazine to equal the result of replacing the char 1 time
        #         magazine = magazine.replace(char, "", 1)
        #     # if its not there
        #     else:    
        #         # return false because we cant make our ransomnote
        #         return False
        # # if we were able to replace all chars we saw from ransomnote, we have enough
        # # return true as we can build our ransom note
        # return True
            
