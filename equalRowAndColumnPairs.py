2352. Equal Row and Column Pairs
Solved
Medium
Topics
Companies
Hint
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
Accepted
137.8K
Submissions
188K
Acceptance Rate
73.3%  

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        score = 0
        colstore = []

        for i in range(rows):
            # for each row in the grid
            singlerow = grid[i]
           
            # match every row to every every col.
            for r in range(rows):
                # save the values of our col 
                singlecol = []
                for c in range(cols):
                    singlecol.append(grid[c][r])

                # print(singlerow, singlecol)
                # if the row matches the col, add 1 to our score 
                if singlerow == singlecol:
                    score +=1

        return score


# alternative and faster

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """


        n = len(grid)
        count = 0

        # Iterate through each row
        for ri in range(n):
            # Iterate through each column
            for cj in range(n):
                is_equal = True
                # Check if elements in the row and column are equal for all elements
                for k in range(n):
                    if grid[ri][k] != grid[k][cj]:
                        is_equal = False
                        break
                # If the row and column are equal, increment the count
                if is_equal:
                    count += 1

        return count
