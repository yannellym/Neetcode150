1198. Find Smallest Common Element in All Rows
Solved
Medium
Topics
Companies
Hint
Given an m x n matrix mat where every row is sorted in strictly increasing order, return the smallest common element in all rows.

If there is no common element, return -1.

 

Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5
Example 2:

Input: mat = [[1,2,3],[2,3,4],[2,3,5]]
Output: 2
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 500
1 <= mat[i][j] <= 104
mat[i] is sorted in strictly increasing order.
Accepted
41K
Submissions
53.6K
Acceptance Rate
76.5%

class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows = len(mat)
        cols = len(mat[0])
        store = set()
        common = {}

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] in store:
                    common[(mat[r][c])] = 1 + common.get((mat[r][c]), 1)

                    if common[mat[r][c]] == rows:
                        return mat[r][c]

                else:
                    store.add(mat[r][c])
    
        return -1

