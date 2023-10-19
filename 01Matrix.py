542. 01 Matrix
Solved
Medium
Topics
Companies
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
Accepted
494.3K
Submissions
1M
Acceptance Rate
47.7%


  from collections import deque


class Solution(object):
    def updateMatrix(self, mat):
        if not mat:
            return []

        m, n = len(mat), len(mat[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        # Initialize a result matrix with maximum possible distance.
        result = [[float('inf') for _ in range(n)] for _ in range(m)]

        # Create a queue to perform BFS.
        queue = deque()

        # Find all 0s and set their distance to 0.
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append((i, j))

        print(result)

        # Perform BFS to update the distances.
        while queue:
            curr_i, curr_j = queue.popleft()

            for d_i, d_j in directions:
                new_i, new_j = curr_i + d_i, curr_j + d_j

                # Check if the new position is within bounds.
                if 0 <= new_i < m and 0 <= new_j < n:
                    # If the current distance + 1 is less than the previous distance, update it.
                    if result[new_i][new_j] > result[curr_i][curr_j] + 1:
                        result[new_i][new_j] = result[curr_i][curr_j] + 1
                        queue.append((new_i, new_j))

        return result

        '''
        If result[new_i][new_j] is initially inf, and result[curr_i][curr_j] 
        is initially 0 (for the starting cell), then result[curr_i][curr_j] + 1 
        would be 1. Since 1 is less than inf, we update result[new_i][new_j] to 1
         and enqueue the cell for exploration.

        As the BFS algorithm progresses, result[new_i][new_j] could have been updated 
        with a smaller distance from a different path, so this comparison keeps track 
        of the shortest distance found so far.

        So, the comparison is between the current known distance (possibly inf) and a potential new, 
        shorter distance. If the potential new distance is smaller, we update the cell's distance and 
        enqueue it for further exploration.
        '''
