# 11. Container With Most Water
# Medium

# 20312

# 1074

# Add to List

# Share
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
    

        res = 0
        l = 0
        r = len(height)-1
        # iterate through height while l < r
        while l < r :
            # we get the area of the container
            # this would be width * height
            #              r-l     *  (we want the min height because we dont want the water to spill)
            area = (r-l) * min(height[l], height[r])
            # choose the max area thus far
            res = max(res, area)

            # see which pointer is smaller, and increment it. We want a max area!
            # if the left pointer is smaller, increment it
            if height[l] < height[r]:
                l +=1
            else:
                # if the right pointer is smaller, decrement it.
                r -=1
        
        return res
