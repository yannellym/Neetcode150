# 890. Find and Replace Pattern
# Medium
# 3.6K
# 161
# Companies
# Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

# Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

 

# Example 1:

# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
# Example 2:

# Input: words = ["a","b","c"], pattern = "a"
# Output: ["a","b","c"]
 

# Constraints:

# 1 <= pattern.length <= 20
# 1 <= words.length <= 50
# words[i].length == pattern.length
# pattern and words[i] are lowercase English letters.
# Accepted
# 167.6K
# Submissions
# 215.9K
# Acceptance Rate
# 77.6%


class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        # for every word in words
        for word in words:
            # create two maps
            wstore = {}
            pstore = {}
            # set a flag
            match = True
            # for every w, and p when you zip word and pattern together
            for w, p in zip(word, pattern):
                # if the w is not in wstore, add it with its value being p
                if w not in wstore:
                    wstore[w] = p
                # if the p is not in pstore, add it with its value being w
                if p not in pstore:
                    pstore[p] = w
                # if the value of w in wstore is not p or the vlaue of p in pstore is not w
                if wstore[w] != p or pstore[p] != w:
                    # set the flag to be false and break
                    match = False
                    break
            # if the flag (match) is true:
            # append the word to the res
            if match:
                res.append(word)
        # return the list of the words appended to the res
        return res

