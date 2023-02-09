# 48. Rotate Image
# Medium
# 13.7K
# 631
# Companies
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 
  
  
  class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # here we convert the matrix into its transpose

        # loop n - 1 times
        for i in range(n-1):
            # loops the remaining amount of times ater i

            for j in range(i+1,n):
                # switch the values 
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        # now we reverse all the rows

        # loop n amount of times
        for i in range(n):
            # fill the matrix with the current matrix section but reversed.
            matrix[i] = matrix[i][::-1]
