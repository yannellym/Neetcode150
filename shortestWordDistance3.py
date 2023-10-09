# 245. Shortest Word Distance III
# Solved
# Medium
# Topics
# Companies
# Given an array of strings wordsDict and two strings that already exist in the array word1 and word2, return the shortest distance between the occurrence of these two words in the list.

# Note that word1 and word2 may be the same. It is guaranteed that they represent two individual words in the list.

 

# Example 1:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
# Output: 1
# Example 2:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
# Output: 3
 

# Constraints:

# 1 <= wordsDict.length <= 105
# 1 <= wordsDict[i].length <= 10
# wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.


class Solution(object):
    def shortestWordDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Initialize variables to store the last positions of word1 and word2
        A = -1
        B = -1

        # Get the total number of words in the list
        n = len(wordsDict)

        # Initialize the answer to the maximum possible value
        ans = n

        # Iterate through the list of words along with their indices
        for i, word in enumerate(wordsDict):
            # Check if the current word is equal to word1
            if word == word1:
                # If word1 is equal to word2, set B to A (same position)
                if word1 == word2:
                    B = A
                # Update A with the current index
                A = i
            # Check if the current word is equal to word2
            elif word == word2:
                # Update B with the current index
                B = i

            # Check if both A and B have valid positions
            if A >= 0 and B >= 0:
                # Calculate the absolute difference between A and B
                distance = abs(A - B)
                # Update ans with the minimum distance found so far
                ans = min(ans, distance)

        # Return the minimum distance found
        return ans
