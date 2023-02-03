# 189. Rotate Array
# Medium
# 13K
# 1.5K
# Companies
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
 

# Follow up:

# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
# Accepted
# 1.4M
# Submissions
# 3.6M
# Acceptance Rate
# 39.3%

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # if k equals 0, just return because we don't need to do anything
        if k == 0:
            return 
        # k is divided by the length of nums, NOT 10, to make sure we are always within bounds
        k = k % len(nums)
        lenght = len(nums)
        

        # reverse the entire array
        # partition the array 
        # reverse each partition itself
        # this takes the portion of the nums array and replaces it by the given values
        nums[lenght-k:], nums[:lenght-k] = nums[:lenght-k],nums[lenght-k:]
        # we dont return anything as it is in place
        
