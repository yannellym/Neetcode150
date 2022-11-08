# 1832. Check if the Sentence Is Pangram
# Easy

# 1990

# 44

# Add to List

# Share
# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:

# Input: sentence = "leetcode"
# Output: false
 

# Constraints:

# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.


class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        reference = 'qwertyuiopasdfghjklzxcvbnm'
        store = {}
        for i in range(len(reference)):
            store[reference[i]] = 0 
        
        for i in range(len(sentence)):
            store[sentence[i]] = 1 + store.get(sentence[i], 0)
            
        return all(x > 0 for x in store.values())
