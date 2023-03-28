# 554. Brick Wall
# Medium
# 2.2K
# 123
# Companies
# There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

# Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

# Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

 

# Example 1:


# Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
# Output: 2
# Example 2:

# Input: wall = [[1],[1],[1]]
# Output: 3
 

# Constraints:

# n == wall.length
# 1 <= n <= 104
# 1 <= wall[i].length <= 104
# 1 <= sum(wall[i].length) <= 2 * 104
# sum(wall[i]) is the same for each row i.
# 1 <= wall[i][j] <= 231 - 1
# Accepted
# 114.9K
# Submissions
# 214.6K
# Acceptance Rate
# 53.5%
# Seen this question in a real interview before?

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        # Approach
        # Create an empty dictionary called edge_counts.
        # Loop through each row in the wall list:
        # a. Create a variable called edge_pos and set it to 0.
        # b. Loop through each brick width in the current row up to the second to last brick (since the last brick cannot form an edge).
        # i. Add the current brick width to edge_pos.
        # ii. Add 1 to the value in the edge_counts dictionary at the key of edge_pos, or add a new key-value pair with key edge_pos and value 1 if it doesn't exist.
        # Return the difference between the length of the wall list and the maximum value in the edge_counts dictionary. If the edge_counts dictionary is empty, return the length of the wall list.
  
        edge_counts = {}
        for row in wall:
            edge_pos = 0
            for brick_width in row[:-1]:
                edge_pos += brick_width
                edge_counts[edge_pos] = edge_counts.get(edge_pos, 0) + 1
        # for example 1, the maximum number of bricks that are crossed is 4
        # the length of the wall is 6
        # 6-4 = 2 meaning that there are 2 bricks the are left uncrossed. This is the min amount left uncrossed.
        return len(wall) - (max(edge_counts.values()) if edge_counts else 0)

