# 36. Valid Sudoku
# Medium
# 8.2K
# 885
# Companies
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.
# Accepted
# 1.1M
# Submissions
# 1.8M
# Acceptance Rate
# 58.1%


# more straight forward approach
def solution(grid):
    # a set to store our seen coordinates
    seen = set()
    
    # iterating the through the grid
    for i in range(9):
        for j in range(9):
            # lets name our current value we're looking at
            current_val = grid[i][j]
            # if its not a period
            if current_val != '.':
                # lets check  the row (each row must have a unique number)
                # we save the row and number in a tuple (with row serving 
                # as first value)
                # ex (row1, value 5)
                if (i, current_val) in seen:
                    return False
                seen.add((i, current_val))
                
                # lets check  the column (each column must have a unique number)
                # we save the column and number in a tuple (with the value serving
                #  as the first value)
                # ex (value 2, column 5)
                if (current_val, j) in seen:
                    return False
                seen.add((current_val, j))
                
                # Check subgrid (each subgrid must have a unique number)
                # i// 3 j //3 will map it to the right subsquare
                # 0//3 = 0 1//3 
                if (i // 3, j // 3, current_val) in seen:
                    return False
                seen.add((i // 3, j // 3, current_val))
    
    return True

from collections import defaultdict

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # will not assume anything for quares not filled in 
        # go through each row and make sure there arent any duplicates(can use hashset)
        # go through each col and make sure there arent any duplicates(can use hashset)

        # create dicts that will holds values in a set:
        # one dict for cols, one for rows, and one for each sub 3x3 square in the board
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        # for all rows in the board (9 rows)
        for r in range(9):
            # for all columns in the board(9 columns)
            for c in range(9):
                # if the digit at this column and row is ".", continue
                # we don't have to check it because its empty
                if board[r][c] == '.':
                    continue
                # else, if there is a value here
                else:
                    # if the digit at this column and row is in the set of values of this column
                    if (board[r][c] in cols[c] or 
                    # or if the digit at this column and row is in the set of values of this row
                    board[r][c] in rows[r] or 
                    # or if the digit at this column and row is in the set of values this subsquare
                    # here r//3 and c//3 will get us the subsquare we are in(either 0, 1, or 2)
                    # this will refer to the set
                    board[r][c] in squares[(r//3 , c//3)]):
                    # return false because its a duplicate
                        return False
                # if its not a duplicate, add the digit at this column and row to:
                # the col set of values of this column 
                # the row set of values of this row
                # the set of values of this subsquare
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        print(cols)
        # if everything else executes, it means we haven't found a duplicated. Return true
        return True

# https://www.youtube.com/watch?v=TjFXEUCMqI8

'''
CHECKS TO SEE IF AT THAT SET(COLUMN OR ROW) THERE IS THE VALUE ALREADY ADDED. 
# squares set - defaultdict(<type 'set'>, 
{
    (0, 1): set([u'1', u'9', u'5', u'7']), 
    (1, 2): set([u'1', u'3', u'6']), 
    (0, 0): set([u'9', u'8', u'3', u'5', u'6']), 
    (2, 1): set([u'1', u'9', u'4', u'8']), 
    (1, 1): set([u'8', u'3', u'2', u'6']), 
    (2, 0): set([u'6']),
    (2, 2): set([u'9', u'8', u'2', u'5', u'7']),
    (1, 0): set([u'8', u'4', u'7']), 
    (0, 2): set([u'6'])
}

cols set = defaultdict(<type 'set'>, 
{
    0: set([u'8', u'5', u'4', u'7', u'6']), 
    1: set([u'9', u'3', u'6']), 2: set([u'8']),
    3: set([u'1', u'8', u'4']), 
    4: set([u'1', u'2', u'7', u'6', u'9', u'8']), 
    5: set([u'9', u'3', u'5']), 
    6: set([u'2']), 
    7: set([u'8', u'7', u'6']), 
    8: set([u'1', u'9', u'3', u'5', u'6'])
}

'''
