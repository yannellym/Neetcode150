# 1941. Check if All Characters Have Equal Number of Occurrences
# Easy
# 633
# 15
# Companies
# Given a string s, return true if s is a good string, or false otherwise.

# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

 

# Example 1:

# Input: s = "abacbc"
# Output: true
# Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
# Example 2:

# Input: s = "aaabb"
# Output: false
# Explanation: The characters that appear in s are 'a' and 'b'.
# 'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.
# Accepted
# 59.5K
# Submissions
# 77.5K
# Acceptance Rate
# 76.8%

class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        store = {}
        for char in s:
            store[char] = 1 + store.get(char, 0)
        value = store.values()[0]
        
        for count in store.values():
            if count != value:
                return False
        return True
