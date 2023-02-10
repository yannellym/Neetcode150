# 54. Spiral Matrix
# Medium
# 10.4K
# 1K
# Companies
# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        while matrix:
            # TOP
            # pop the first row and append it to the result
            result += matrix.pop(0) # 1

            # RIGHT
            # if there's a matrix, and theres a row:
            if matrix and matrix[0]: # 2 
                # # for each line in the matrix, append the last digit to the result
                for line in matrix:
                    result.append(line.pop())
            # BOTTOM
            # if the're a matrix: 
            if matrix: # 3
                # reverse the row, pop it, and append it to the result
                result += matrix.pop()[::-1]
           
            # LEFT
            # if there is a matrix and a row
            if matrix and matrix[0]: # 4
                # for each line in the matrix(reversed)
                for line in matrix[::-1]:
                    # append the last digit to the result
                    result.append(line.pop(0))
        return result

        # https://leetcode.com/problems/spiral-matrix/solutions/3039684/python-solution-explained-step-by-step-with-illustrations/
       
