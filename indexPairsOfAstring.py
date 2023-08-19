1065. Index Pairs of a String
Easy
357
105
company
Amazon
Given a string text and an array of strings words, return an array of all index pairs [i, j] so that the substring text[i...j] is in words.

Return the pairs [i, j] in sorted order (i.e., sort them by their first coordinate, and in case of ties sort them by their second coordinate).

 

Example 1:

Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
Output: [[3,7],[9,13],[10,17]]
Example 2:

Input: text = "ababa", words = ["aba","ab"]
Output: [[0,1],[0,2],[2,3],[2,4]]
Explanation: Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].
 

Constraints:

1 <= text.length <= 100
1 <= words.length <= 20
1 <= words[i].length <= 50
text and words[i] consist of lowercase English letters.
All the strings of words are unique.
Accepted
25.8K
Submissions
38.7K
Acceptance Rate
66.7%


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Solution(object):
    def indexPairs(self, text, words):
        # Helper function to insert a word into the trie
        def insert_word(root, word):
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end_of_word = True

        # Helper function to search the trie for matches starting from a given index
        def search_trie(root, text, start):
            node = root
            result = []
            
            for i in range(start, len(text)):
                char = text[i]
                if char not in node.children:
                    break
                node = node.children[char]
                if node.is_end_of_word:
                    result.append(i)
                    
            return result

        # Create the root of the trie
        root = TrieNode()
        # Insert words into the trie
        for word in words:
            insert_word(root, word)
        
        result = []
        # Iterate through each character in the text
        for i in range(len(text)):
            # Search for matches starting from the current index
            matches = search_trie(root, text, i)
            # For each match, add the index pair to the result
            for j in matches:
                result.append([i, j])
        
        # Sort and return the result
        result.sort()
        return result
