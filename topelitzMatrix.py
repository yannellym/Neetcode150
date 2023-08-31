766. Toeplitz Matrix
Solved
Easy
Topics
Companies
Hint
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

 

Example 1:


Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:


Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99
 

Follow up:

What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?
Accepted
285.7K
Submissions
417.6K
Acceptance Rate
68.4%

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        

        rows = len(matrix)
        cols = len(matrix[0])

        res = [[] for _ in range(cols) ]
        

        for r in range(rows):
            for c in range(cols):
                if c == 0:
                    res.insert(0, [matrix[r][c]])
                else:
                    res[c].append(matrix[r][c])
        print(res)
        for subarray in res:
            first_element = subarray[0] if subarray else 0 # Get the first element of the subarray
            for element in subarray:
                if element != first_element:
                    return False  # If any element is different, return False
        return True 




# alternative 

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        for r in range(1, rows):
            for c in range(1, cols):
                print(matrix[r][c])
                if matrix[r][c] != matrix[r - 1][c - 1]:
                    return False  # If any element is not equal to its top-left neighbor, return False
        
        return True  # All elements are equal to their top-left neighbors
