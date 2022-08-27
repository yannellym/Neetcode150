# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
  

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        
        temp = defaultdict(list)

        for string in strs:
           temp[str(sorted(string))].append(string)
        
        response = list(temp.values())
        return response
        
        
