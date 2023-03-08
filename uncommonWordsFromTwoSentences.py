# 884. Uncommon Words from Two Sentences
# Easy
# 1.1K
# 153
# Companies
# A sentence is a string of single-space separated words where each word consists only of lowercase letters.

# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

# Example 1:

# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]
# Example 2:

# Input: s1 = "apple apple", s2 = "banana"
# Output: ["banana"]
 

# Constraints:

# 1 <= s1.length, s2.length <= 200
# s1 and s2 consist of lowercase English letters and spaces.
# s1 and s2 do not have leading or trailing spaces.
# All the words in s1 and s2 are separated by a single space.
# Accepted
# 115.2K
# Submissions
# 173.8K
# Acceptance Rate
# 66.3%

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """

        # approach 1: put both in a dic, return keys with value of 1

        store = dict()
        res =  []

        for word in s1.split(" "):
            store[word] = 1 + store.get(word, 0)
        
        for word in s2.split(" "):
            store[word] = 1 + store.get(word, 0)

        for k, v in store.items():
            if v == 1:
                res.append(k)

        return res
        
