# 452. Minimum Number of Arrows to Burst Balloons
# Medium

# 5618

# 154

# Add to List

# Share
# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

 

# Example 1:

# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
# Example 2:

# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
# Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
# Example 3:

# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
# - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
 

# Constraints:

# 1 <= points.length <= 105
# points[i].length == 2
# -231 <= xstart < xend <= 231 - 1

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
         # sort the points array 
        points.sort()

        # initialize the number of arrows and the xend value of the previous balloon
        arrows = 0
        prev_xend = float('-inf')

        # iterate over the sorted arrays in points
        for x,y in points:
            # if the arrow that burst the previous balloon cannot burst the current one,
            # shoot a new arrow and update the xend value of the previous balloon
            if x > prev_xend:
                arrows += 1
                prev_xend = y
            # otherwise, update the xend value of the previous balloon to the minimum between
            # its current value and the xend value of the current balloon
            else:
                prev_xend = min(prev_xend, y)

        return arrows
    
    
    """ 
    [[1, 6], [2, 8], [7, 12], [10, 16]]
    
    prev_xend = -inf    1 >-inf? YES.   arrow + 1.  prev_xend = 6
    prev_xend = 6.      2 > 6? NO.      prev_xend =  MIN OF 8 AND 6 = 6
    prev_xend = 6.      7 > 6? YES.     arrow + 1.  prev_xend = 12
    prev_xend = 12      10> 12? NO.     prev_xend =  MIN OF 12 AND 16 = 12
    """
