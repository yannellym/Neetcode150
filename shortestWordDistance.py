# 243. Shortest Word Distance
# Solved
# Easy
# Topics
# Companies
# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

 

# Example 1:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
# Output: 3
# Example 2:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
# Output: 1
 

# Constraints:

# 2 <= wordsDict.length <= 3 * 104
# 1 <= wordsDict[i].length <= 10
# wordsDict[i] consists of lowercase English letters.
# word1 and word2 are in wordsDict.
# word1 != word2
# Accepted
# 205.7K
# Submissions
# 315.9K
# Acceptance Rate
# 65.1% 

class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(wordsDict)
        A = -1
        B = -1
        res = n
        
        for i, word in enumerate(wordsDict):
            if word == word1:
                A = i
            elif word == word2:
                B = i
            # check the min distance so far if both A and B have a valid index
            # this works in the case that we have an arr like this ["a","a","b","b"]
            # abs(1-2) will be better than abs(1-3)
            if A >= 0 and B >= 0:
                res = min(res, abs(A-B))
        return res
