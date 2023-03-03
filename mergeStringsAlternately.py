# 1768. Merge Strings Alternately
# Easy
# 939
# 17
# Companies
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
 

# Constraints:

# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.
# Accepted
# 93.7K
# Submissions
# 121.4K
# Acceptance Rate
# 77.2%

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """


        res = ""

        for i in range(len(word1)):
            # if our index for word2 becomes out of bounds
            if i == len(word2):
                # add the char at index i of word1 to res
                res += word1[i:]
                # add the char at index i of word2 to res
                return res

            res += word1[i]
            res += word2[i]
        # we have ran through the entire word1 and there might be some letters from word2 left
        if i != len(word2)-1:
            # return the built word(res) with the rest of word2
            res+= word2[i+1:]
        return res


        #solution #2

        finalword = ""
        for i in range(min(len(word1), len(word2))): # pick smallest length
            finalword += word1[i] + word2[i]
        return finalword + word1[i + 1:] + word2[i + 1:] # will add any remaining characters left
