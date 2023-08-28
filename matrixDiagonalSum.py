1572. Matrix Diagonal Sum
Solved
Easy
Topics
Companies
Hint
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5
 

Constraints:

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
Accepted
288.1K
Submissions
348.1K
Acceptance Rate
82.8%


class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        primary_sum = 0
        secondary_sum = 0
        
        for i in range(n):
            primary_sum += mat[i][i] # primary diagonal
            secondary_sum += mat[i][n - i - 1] # secondary diagonal
            # the - i - 1 helps to loop in reverse ( seving as -1 -1 -1)
        
        # If n is odd, subtract the duplicate middle element
        if n % 2 == 1:
            middle = n // 2
            total_sum = primary_sum + secondary_sum - mat[middle][middle]
        else:
            total_sum = primary_sum + secondary_sum
        
        return total_sum
