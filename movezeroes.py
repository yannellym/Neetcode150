# 283. Move Zeroes
# Easy

# 11952

# 301

# Add to List

# Share
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # keeps tracks of our nums array order
        j = 0
        # for every index in nums
        for i in range(len(nums)):
            # if the number is not a 0 
            if nums[i]:
                # swap them
                nums[j], nums[i] = nums[i], nums[j]
                # increment j
                j +=1
        

#https://www.youtube.com/watch?v=aayNRwUN3Do&t=1s
