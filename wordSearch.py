# 79. Word Search
# Medium
# 14.1K
# 577
# company
# TikTok
# company
# Bloomberg
# company
# Uber
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
 

# Follow up: Could you use search pruning to make your solution faster with a larger board?

# Accepted
# 1.3M
# Submissions
# 3.3M
# Acceptance Rate
# 40.5%

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def findLetters(r, c, index):
            # Base case: If the entire word has been found, return True
            if index == len(word):
                return True
            
            # Check if the current cell is out of bounds or doesn't match the current letter
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False
            
            # Store the original cell content and mark the cell as visited
            temp = board[r][c]
            board[r][c] = '#'  # Mark the cell as visited
            
            # Recursively check neighboring cells
            found = (findLetters(r + 1, c, index + 1) or
                     findLetters(r - 1, c, index + 1) or
                     findLetters(r, c + 1, index + 1) or
                     findLetters(r, c - 1, index + 1))
            
            # Restore the original cell content
            board[r][c] = temp  # Restore the cell
            
            return found
        
        rows = len(board)
        cols = len(board[0])
        
        # Iterate through each cell in the board
        for r in range(rows):
            for c in range(cols):
                # If the first letter matches, start searching from this cell
                if board[r][c] == word[0] and findLetters(r, c, 0):
                    return True
        
        return False








class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def checkBoard(r,c,idx):
          if idx == len(word):
            return True 

          if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
            return 

          temp = board[r][c]
          board[r][c] = "."

          found = (checkBoard(r+1, c, 1 +idx) or checkBoard(r, c+1, 1 +idx) or checkBoard(r-1, c, 1 +idx) or checkBoard(r, c-1, 1 +idx) )

          board[r][c] = temp
          return found

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
          for c in range(cols):
            if board[r][c] == word[0] and checkBoard(r,c, 0):
              return True
        return False
