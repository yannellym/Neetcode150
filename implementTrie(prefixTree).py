# 208. Implement Trie (Prefix Tree)
# Medium
# 10.5K
# 119
# company
# Amazon
# company
# Google
# company
# Microsoft
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

# Example 1:

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
 

# Constraints:

# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.
# Accepted
# 845K
# Submissions
# 1.3M
# Acceptance Rate
# 63.3%

class Trie(object):

    def __init__(self):
        self.trie = {}
        self.unique = set()
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if word[0] not in self.trie:
            self.trie[word[0]] = []
        self.trie[word[0]].append(word)
        self.unique.add(word)

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word in self.unique
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        try:
            for subword in self.trie[prefix[0]]:
                if subword[:len(prefix)] == prefix:
                    return True
        except:
            return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
