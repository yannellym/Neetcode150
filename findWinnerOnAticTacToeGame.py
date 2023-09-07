1275. Find Winner on a Tic Tac Toe Game
Solved
Easy
Topics
Companies
Hint
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

 

Example 1:


Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.
Example 2:


Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.
Example 3:


Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
 

Constraints:

1 <= moves.length <= 9
moves[i].length == 2
0 <= rowi, coli <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.
Accepted
109.6K
Submissions
202.5K
Acceptance Rate
54.1%



class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        matrix = [[""] * 3 for _ in range(3)]
        
        def checkWin(matrix, player):
 
            # Check rows and columns.
            for i in range(3):
                # check rows
                # check columns
                if all(matrix[i][j] == player for j in range(3)) or \
                all(matrix[j][i] == player for j in range(3)):
                    return True
            # Check both diagonals.
            #diagonal left to right 
            # diagonal right to let
            if all(matrix[i][i] == player for i in range(3)) or \
            all(matrix[i][2 - i] == player for i in range(3)):
                return True
            return False


        # enumerate the moves arr to get the index and tuple with coordinates
        for i, (r, c) in enumerate(moves):
            # if even, player == X, if odd. player == O 
            player = "X" if i % 2 == 0 else "O"
            matrix[r][c] = player
            
            # if the players have made a total of 3 moves(combined) (indexed 0) and
            # checkwin comes back as true, return A if the player is X else, B
            if i >= 2 and checkWin(matrix, player):
                return "A" if player == "X" else "B"
        # if we don't return anything above, and the len of moves is 9,
        # the players have played all their moves, return "draw"
        if len(moves) == 9:
            return "Draw"
        
        # if nothing else is returned, there are still moves to play,
        return "Pending"
            
