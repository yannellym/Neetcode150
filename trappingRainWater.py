# 42. Trapping Rain Water
# Hard
# 25.9K
# 355
# Companies
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105
# Accepted
# 1.5M
# Submissions
# 2.5M
# Acceptance Rate
# 59.3%

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # Time Complexity: O(N)
        # Space Complexity: O(1)    
        ans, minHeight, mxMinHeight  = 0, 0, 0
        l = 0
        r = len(height) -1
        # two pointers 
        # pointer i from the left
        # pointer j from the right
        while l <= r:
            # take the min height
            minHeight = min(height[l], height[r])
            # find the max min height
            mxMinHeight = max(mxMinHeight, minHeight)
            # the units of water being tapped is the diffence between max height and min height
            ans +=  mxMinHeight - minHeight 
            # move the pointer i if height[i] is smaller
            if height[l] < height[r]: 
                l += 1
            # else move pointer j
            else: 
               r -= 1
        return ans
