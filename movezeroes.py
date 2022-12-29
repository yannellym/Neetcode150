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
        j = 0
        i = 0
        # run through each digit in nums
        while i < len(nums):
            # if the digit at index i is greater than 0
            if nums[i]:
                # swap digit at index i with digit at index j and viseversa
                nums[i], nums[j] = nums[j], nums[i]
                # increase the j so you have the new placement in the array
                j += 1
            # increase i so we're not in an infite loop
            i += 1

