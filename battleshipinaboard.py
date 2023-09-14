# 419. Battleships in a Board
# Solved
# Medium
# Topics
# Companies
# Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

# Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

 

# Example 1:


# Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
# Output: 2
# Example 2:

# Input: board = [["."]]
# Output: 0
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is either '.' or 'X'.
 

# Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?

# Accepted
# 189.8K
# Submissions
# 253.1K
# Acceptance Rate
# 75.0%
  
  
  class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        
        rows = len(board)
        cols = len(board[0])
        ships = 0


        def checkNeighbors(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "X":
                return False

            temp = board[r][c]

            board[r][c] = "."
            # same row but column to right - horizontally
            checkNeighbors(r, c +1)

            # same row but column to left - horizontally
            checkNeighbors(r, c-1)

            # same col but one row up - vertically
            checkNeighbors(r - 1 , c )

            # same col but one row down  - vertically
            checkNeighbors(r + 1, c)
            
            
            return True




        for r in range(rows):
            for c in range(cols):

                if checkNeighbors(r,c):
                    ships +=1
        return ships 


        # optimized

        class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        
        count = 0
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    # If i is equal to 0, the current cell is in the first row, there cannot be a cell above it.
                    # checks if the cell immediately above the current cell (i.e., the cell at (i - 1, j)) is 
                    # empty ('.'). If it is empty, there is no battleship directly above the current cell.  

                    # If j is equal to 0, it means the current cell is in the first column, 
                    # and there cannot be a cell to its left. 
                    # checks if the cell immediately to the left of the current cell (i.e., the cell at (i, j - 1)
                    # ) is empty ('.'). If it is empty, it means there is no battleship directly to the left of 
                    # the current cell. 
                    if (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.'):
                        count += 1

        return count

        # checks whether both of the following conditions are true for the current cell:

        # There is no battleship above it (or it's in the top row).
        # There is no battleship to the left of it (or it's in the leftmost column).
