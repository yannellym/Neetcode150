
# Testcase
# Testcase
# Result

# Code

# 244. Shortest Word Distance II
# Solved
# Medium
# Topics
# Companies
# Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

# Implement the WordDistance class:

# WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
# int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.
 

# Example 1:

# Input
# ["WordDistance", "shortest", "shortest"]
# [[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
# Output
# [null, 3, 1]

# Explanation
# WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
# wordDistance.shortest("coding", "practice"); // return 3
# wordDistance.shortest("makes", "coding");    // return 1
 

# Constraints:

# 1 <= wordsDict.length <= 3 * 104
# 1 <= wordsDict[i].length <= 10
# wordsDict[i] consists of lowercase English letters.
# word1 and word2 are in wordsDict.
# word1 != word2
# At most 5000 calls will be made to shortest.

# class WordDistance:

#     def __init__(self, wordsDict: List[str]):
#         self.word_positions = {}
#         for i, word in enumerate(wordsDict):
#             if word in self.word_positions:
#                 self.word_positions[word].append(i)
#             else:
#                 self.word_positions[word] = [i]

#     def shortest(self, word1: str, word2: str) -> int:
#         positions1 = self.word_positions[word1]
#         positions2 = self.word_positions[word2]
#         i, j = 0, 0
#         min_distance = float('inf')
        
#         # Merge the two sorted lists of positions to find the minimum distance
#         while i < len(positions1) and j < len(positions2):
#             # compute the min absolute distance between (position1, and 2)
#             min_distance = min(min_distance, abs(positions1[i] - positions2[j]))
#             # if the val at positions1[i] is less:
#             # increase that value so we can get a min distance
#             if positions1[i] < positions2[j]:
#                 i += 1
#             else:
#                 j += 1
        
#         return min_distance

        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
