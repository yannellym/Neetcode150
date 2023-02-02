# 953. Verifying an Alien Dictionary
# Easy
# 4.4K
# 1.4K
# Companies
# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.
# Accepted
# 441.3K
# Submissions
# 812.9K
# Acceptance Rate
# 54.3%

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        # create a dictionary with the indexes and values of alien alphabet
        store = { c : i for i,c in enumerate(order)}
        # loops through the length of words -1 to make sure you have a pair always
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            # loop j amount of times with j being the length of word1
            for j in range(len(word1)):
                # if j reach the length of word2,
                # j was a prefix of word1, that is not allowed, return False
                if j == len(word2):
                    return False
                # if the chars are not the same,
                if word1[j] != word2[j]:
                    # check in the store dict for letters and their indexes 
                    # to see if the char at word2 is less than char at word1
                    # if this char is less, return false because they need to be in order
                    # char at word2 cannot be greater than char at word1
                    if store[word2[j]] < store[word1[j]]: 
                        return False
                    # here we dont return true because we are not done yet
                    # we might still have some words to go through 
                    # break to exit this iteration
                    break
        # if we go through all iterations and none of the negatives above execute,
        # the words are in alphabetical order according to the aliens.
        return True
