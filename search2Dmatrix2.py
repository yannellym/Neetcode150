# 240. Search a 2D Matrix II
# Medium
# 9.9K
# 167
# Companies
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
 

# Example 1:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true
# Example 2:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -109 <= matrix[i][j] <= 109
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -109 <= target <= 109
# Accepted
# 759.9K
# Submissions
# 1.5M


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # get the length and width of the matrix
        L = len(matrix)
        W = len(matrix[0])

        # ROWS WILL BE THE LENGTH OF THE MATRIX - 1 (to be within bounds)
        r = L-1
        # COLUMNS WILL BE 0 so we look at the first column
        c = 0

        # while the row is greater than or equal to 0 
        # (we start from the last one so we need to make sure we stay within bounds)
        # AND while the column is less than the with 
        # (we start at 0 and need to make sure we stay within bounds)
        while r >= 0 and c < W:
            # if the current point equals the target, return True
            if matrix[r][c] == target:
                return True
            # if the current point is less than the target, 
            # increase c so we look at another column
            elif matrix[r][c] < target:
                c += 1
            # if the current point is more than the target, 
            # decrease r so we look at the row above
            else:
                r -= 1
        # if the return statement doesnt execute, return False
        return False

