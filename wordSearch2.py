212. Word Search II
Hard
8.8K
410
company
Uber
company
Google
company
Amazon
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
Accepted
576.6K
Submissions
1.6M
Acceptance Rate
36.1%
Seen this question in a real interview before?
1/4

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addToTrie(self, word):
        curr = self
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr =  curr.children[char]
        curr.isWord = True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # create the Trie root
        root = TrieNode()
        
        # for every word in words, add it to the Trie
        for word in words:
            root.addToTrie(word) 

        # get measurements of our board
        rows = len(board)
        cols = len(board[0])
        # we dont want to repeat the same char in an answer, we also dont want to repeat a word in the res
        res, visited = set(), set()


        def dfs(r,c,node, word):
            # if the coordinates are out of bounds OR the coordinate is in visited OR 
            # the curr letter not in the trie
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
            (r, c) in visited or board[r][c] not in node.children):
                return 

            # add it to the visited set so we know we visited
            visited.add((r,c))
            # update our node to be the curr char we're looking at
            node = node.children[board[r][c]]
            # add the char to the word
            word += board[r][c]
            # check if it was one of the words in our words arr
            if node.isWord:
                res.add(word)

            # search its neighbors
            dfs(r+1, c, node , word)
            dfs(r-1, c, node , word)
            dfs(r, c+1, node , word)
            dfs(r, c-1, node , word)
            # remember to remove the node from visited as we are backracking
            visited.remove((r,c))


        # search through the board
        for r in range(rows):
            for c in range(cols):
                # call dfs
                dfs(r, c, root, "")
        return list(res)
