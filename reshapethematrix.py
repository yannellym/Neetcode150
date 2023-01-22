# 566. Reshape the Matrix
# Easy
# 3K
# 337
# Companies
# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

 

# Example 1:


# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]
# Example 2:


# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# -1000 <= mat[i][j] <= 1000
# 1 <= r, c <= 300

class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # get the length of the rows and columns
        rows = len(mat)
        cols = len(mat[0])
        # flattten the array 
        temp = [mat[row][col] for row in range(rows) for col in range(cols)]
   
        # will hold our answer
        res = []

        # if the mat arr has the same dimensions give by r, and c, just return the mat arr
        if rows == r and cols == c:
            return mat

        # if the product of the dimensions of mat do not equal the product of the dimensions given, return mat
        if rows * cols != r * c:
            return mat


        idx = 0
        # loop r amount of times, this will create the amount of rows we will have
        for row in range(r):
            # create a temporary sublist to hold our rows
            sub_list = []
            # loop c amount of times, this will create our columns
            for col in range(c):
                # append the digit from our flat array to the sublist
                sub_list.append(temp[idx])
                # increment the index
                idx += 1
            # append the sublist
            res.append(sub_list)
        
        return res
                
