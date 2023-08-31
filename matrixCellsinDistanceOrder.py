1030. Matrix Cells in Distance Order
Solved
Easy
Topics
Companies
You are given four integers row, cols, rCenter, and cCenter. There is a rows x cols matrix and you are on the cell with the coordinates (rCenter, cCenter).

Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter) from the smallest distance to the largest distance. You may return the answer in any order that satisfies this condition.

The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.

 

Example 1:

Input: rows = 1, cols = 2, rCenter = 0, cCenter = 0
Output: [[0,0],[0,1]]
Explanation: The distances from (0, 0) to other cells are: [0,1]
Example 2:

Input: rows = 2, cols = 2, rCenter = 0, cCenter = 1
Output: [[0,1],[0,0],[1,1],[1,0]]
Explanation: The distances from (0, 1) to other cells are: [0,1,1,2]
The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.
Example 3:

Input: rows = 2, cols = 3, rCenter = 1, cCenter = 2
Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
Explanation: The distances from (1, 2) to other cells are: [0,1,1,2,2,3]
There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].
 

Constraints:

1 <= rows, cols <= 100
0 <= rCenter < rows
0 <= cCenter < cols
Accepted
52.6K
Submissions
75.2K
Acceptance Rate
70.0%


class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """

        # Return the coordinates of all cells in the matrix sorted by their distance from (rCenter, cCenter)
         # from the smallest distance to the largest distance.


        distances = []
        
        # Step 1: Iterate through all cells in the matrix
        for r in range(rows):
            for c in range(cols):
                # Step 2: Calculate the distance from the center point
                distance = abs(r - rCenter) + abs(c - cCenter)
                # Store the coordinates and distance in a tuple
                distances.append((r, c, distance))
        
        # Step 4: Sort the list of tuples based on the distance
        distances.sort(key=lambda x: x[2])
        
        # Step 5: Extract the sorted coordinates
        result = [[r, c] for r, c, _ in distances]
        return result
