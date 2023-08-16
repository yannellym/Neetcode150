# 211. Design Add and Search Words Data Structure
# Medium
# 7K
# 395
# company
# Amazon
# company
# Google
# company
# Bloomberg
# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
 

# Constraints:

# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 104 calls will be made to addWord and search.
# Accepted
# 538.6K
# Submissions
# 1.2M
# Acceptance Rate
# 44.2%

class TrieNode:
    def __init__(self):
        self.children = {}  # a : TrieNode
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root # Start from the root node
        # go through the word
        for c in word:
            # if the letter is not in the curr node's children add it
            if c not in cur.children:
                cur.children[c] = TrieNode()  # Create a new node if the character is not present
            # make the current node, the last child you entered
            # ex curr(b) -> () -> (),     (b) -> curr(a) -> (d) , (b) -> (a) -> curr(d)
            cur = cur.children[c]
        # if it gets here, it'll maark the end of the word
        cur.word = True

    def search(self, word: str) -> bool:
        # pass in the word, and self.root
        return self.searchHelper(word, self.root)

    def searchHelper(self, word: str, node: TrieNode) -> bool:
        # get the index and the curr char of the word
        for i, char in enumerate(word):
            # if its a ., we have a lot of paths to go in
            if char == '.':
                # for every child value in the node
                for child in node.children.values():
                    # recursively go down that path 
                    # If any of these recursive calls returns True, then 
                    # the entire search should return True, indicating that a 
                    # match was found somewhere down the line.
                    if self.searchHelper(word[i + 1:], child):  # Recursively search all child nodes
                        return True
                # If none of the recursive calls return True (i.e., no match was found in any child node),
                # the function returns False to indicate that there is no match.
                return False
            if char not in node.children:
                return False  # Return False if the character is not found
            node = node.children[char]  # Move to the next node
        return node.word  # Return True if the end of the word is reached


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# https://www.youtube.com/watch?v=BTf05gs_8iU
