1329. Sort the Matrix Diagonally
Solved
Medium
Topics
Companies
Hint
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

 

Example 1:


Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
Example 2:

Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
Accepted
151.6K
Submissions
182.6K
Acceptance Rate
83.0%
Seen this question in a real interview before?
1/4

class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        m, n = len(mat), len(mat[0])
        diagonals = {}
        
        # Iterate through the matrix and store elements in diagonals
        for i in range(m):
            for j in range(n):
                # this will get each diagonal value and store it in the corresponding diagonal
                if (i - j) not in diagonals:
                    diagonals[i - j] = []
                diagonals[i - j].append(mat[i][j])
        # each diagonal ends up being having an index in the dic of  2, 1, 0, -1, -2, -3
   
        
        # Sort and update the matrix with diagonal elements
        for key in diagonals:
            diagonals[key].sort()
       
        for i in range(m):
            for j in range(n):
                # you'll end up going through the mat, and in your dict, you search for the corresponding
                # diagonal index and pop the last element. The last element should be the biggest one and so on.
                mat[i][j] = diagonals[i - j].pop(0)
        
        return mat


        # i - j is to obtain the numbers diagonally going from left to righgt
        # i + j is for numbers right to left
