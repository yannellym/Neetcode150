# 74. Search a 2D Matrix
# Medium
# 11.1K
# 326
# Companies
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        '''
        approach:

        step 1: get the num of cols and rows
        step 2: flatten the array with help of cols and rows
        step 3: perform a binary search on the array -> O(log(m*n))
        step 4: return true if the target is in the array, false otherwise
        '''

        rows = len(matrix)
        cols = len(matrix[0])

        sub = [matrix[r][c] for r in range(rows) for c in range(cols)]
        
        length = len(sub)
        i = 0
        j = length - 1

        while i <= j:
            mid = (j + i)//2
           
            if target == sub[mid]:
                return True
            else:
                if sub[mid] > target:
                    j = mid-1
                elif sub[mid] < target:
                    i = mid+1
                else:
                    return True
        return False


        # Alternative

        # temp=[]
        # for i in matrix:
        #     for j in i:
        #         temp.append(j)
        # if target in temp:
        #     return True
        # else:
        #     return False
