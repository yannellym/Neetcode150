Description
Editorial
Editorial
Solutions
Solutions
Submissions
Submissions

Code

Testcase
Testcase
Result

1886. Determine Whether Matrix Can Be Obtained By Rotation
Easy
Topics
Companies
Hint
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

 

Example 1:


Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
Example 2:


Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.
Example 3:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
 

Constraints:

n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] and target[i][j] are either 0 or 1.
Accepted
58.5K
Submissions
103.9K
Acceptance Rate
56.3%


class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """

        rows = len(mat)
        cols = len(mat[0])

        for _ in range(4):  # You only need to check for 4 rotations (0, 90, 180, 270 degrees)
            print(mat)
            if mat == target:
                return True
            # Rotate the matrix 90 degrees clockwise
            rotated_mat = []
            for col in range(cols):
                rotated_row = [mat[row][col] for row in range(rows - 1, -1, -1)]
                rotated_mat.append(rotated_row)
            mat = rotated_mat
           

        return False
