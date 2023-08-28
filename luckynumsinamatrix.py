1380. Lucky Numbers in a Matrix
Solved
Easy
Topics
Companies
Hint
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= n, m <= 50

All elements in the matrix are distinct.
Accepted
90.6K
Submissions
127.9K
Acceptance Rate
70.8%


class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        rows = len(matrix)
        cols = len(matrix[0])

        lucky_numbers = []

        for r in range(rows):
            row_min = min(matrix[r])
            col_index = matrix[r].index(row_min)
            
            is_max_in_col = all(matrix[i][col_index] <= row_min for i in range(rows))
            
            if is_max_in_col:
                lucky_numbers.append(row_min)

        return lucky_numbers
