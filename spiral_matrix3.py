885. Spiral Matrix III
Solved
Medium
Topics
Companies
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.

 

Example 1:


Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]
Example 2:


Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
 

Constraints:

1 <= rows, cols <= 100
0 <= rStart < rows
0 <= cStart < cols
Seen this question in a real interview before?
1/5
Yes
No
Accepted
140.1K
Submissions
166.3K
Acceptance Rate
84.2%


class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        
        result = []  # List to store the coordinates in the spiral order
        total_cells = rows * cols  # Total number of cells to be visited
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Directions: Right, Down, Left, Up
        step = 1  # Initial number of steps to take in a given direction
        x, y = rStart, cStart  # Start position

        # Add the starting position to the result
        result.append([x, y])
        
        # Continue until we've visited all cells in the grid
        while len(result) < total_cells:
            # Iterate over the four possible directions (right, down, left, up)
            for i in range(4):
                dx, dy = directions[i]  # Get the direction vector
                # Move `step` times in the current direction
                for _ in range(step):
                    x += dx  # Update the x-coordinate
                    y += dy  # Update the y-coordinate
                    # Check if the new position is within the grid boundaries
                    if 0 <= x < rows and 0 <= y < cols:
                        result.append([x, y])  # Add the valid position to the result list
                # Increase the step count after moving in horizontal (right/left) or vertical (down/up) directions
                if i % 2 == 1:  # Increase step after moving down or up (every two directions)
                    step += 1
                    
        return result  # Return the list of coordinates in spiral order
