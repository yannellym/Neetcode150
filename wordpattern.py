# 290. Word Pattern
# Easy

# 4228

# 478

# Add to List

# Share
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
 

# Constraints:

# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        # split the s array to turn it into separate words
        words = s.split(" ")
        
        # if the length of the pattern is not the length of the new array of words:return false
        if len(pattern) != len(words):
            return False
        
        # create two objects:
           # 1: map the pattern char to the array's word
           # 2: map the array's word to the pattern's char
        charToWord = {}
        wordToChar = {}
        # zip the both objects together and loop through them:
        for char, word in zip(pattern, words):
            # if the char is in chartoword already, and the value of the char 
            # in the chartoword doesnt equal the word, return false
            if char in charToWord and charToWord[char] != word:
                return False
            # if the word is in wordtochar already, and the value of the word 
            # in the wordtochar doesnt equal the char, return false
            if word in wordToChar and wordToChar[word] != char:
                return False
            # add the char to the object and set the value to be the word
            charToWord[char] = word
            # add the wordtothechar the object and set the value to be the char
            wordToChar[word] = char
        # if everything matches, return true
        return True
         
  
