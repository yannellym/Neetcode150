# 1861. Rotating the Box
# Medium
# 828
# 46
# company
# Uber
# company
# Capital One
# company
# Netflix
# You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

# A stone '#'
# A stationary obstacle '*'
# Empty '.'
# The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

# It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

# Return an n x m matrix representing the box after the rotation described above.

 

# Example 1:



# Input: box = [["#",".","#"]]
# Output: [["."],
#          ["#"],
#          ["#"]]
# Example 2:



# Input: box = [["#",".","*","."],
#               ["#","#","*","."]]
# Output: [["#","."],
#          ["#","#"],
#          ["*","*"],
#          [".","."]]
# Example 3:



# Input: box = [["#","#","*",".","*","."],
#               ["#","#","#","*",".","."],
#               ["#","#","#",".","#","."]]
# Output: [[".","#","#"],
#          [".","#","#"],
#          ["#","#","*"],
#          ["#","*","."],
#          ["#",".","*"],
#          ["#",".","."]]
 

# Constraints:

# m == box.length
# n == box[i].length
# 1 <= m, n <= 500
# box[i][j] is either '#', '*', or '.'.
# Accepted
# 41.3K
# Submissions
# 63.2K
# Acceptance Rate
# 65.4%


class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        # Ex, box = [["#",".","*","."],
                   # ["#","#","*","."]]
        # num of rows
        m = len(box) # -> 2
        # num of cols  # -> 4
        n = len(box[0])
        
        newBox =[[None]*m for _ in range(n)]
        # ex, [[None, None], [None, None], [None, None], [None, None]]
        
		# rotate matrix
        for i in range(m):
            for j in range(n):
                newBox[j][m-i-1] = box[i][j]
                '''
                [[None, u'#'], [None, None], [None, None], [None, None]]
                [[None, u'#'], [None, u'.'], [None, None], [None, None]]
                [[None, u'#'], [None, u'.'], [None, u'*'], [None, None]]
                [[None, u'#'], [None, u'.'], [None, u'*'], [None, u'.']]
                [[u'#', u'#'], [None, u'.'], [None, u'*'], [None, u'.']]
                [[u'#', u'#'], [u'#', u'.'], [None, u'*'], [None, u'.']]
                [[u'#', u'#'], [u'#', u'.'], [u'*', u'*'], [None, u'.']]
                [[u'#', u'#'], [u'#', u'.'], [u'*', u'*'], [u'.', u'.']]
                '''
        # [['#', '#'], ['#', '.'], ['*', '*'], ['.', '.']]
        
		#gravity

        # iterate through ech column of newBox
        for j in range(m):
            curr = n-1
            # iterate through each row of current column from botton to top
            for i in range(n-1,-1,-1):
                # if it contains an obstacle, 
                if newBox[i][j] == "*":
                    # update curr to equal i-1
                    curr = i-1
                # if it contains a stone, 
                elif newBox[i][j] == "#":
                    # set the curr space to equal empty
                    newBox[i][j] = "."
                    # move thr stone down to the curr row
                    newBox[curr][j] = "#"
                    # decrement the curr var
                    curr-=1
        
        return newBox
