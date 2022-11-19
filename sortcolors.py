# 75. Sort Colors
# Medium

# 13029

# 477

# Add to List

# Share
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
 

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

# Accepted
# 1,253,042
# Submissions
# 2,184,222

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) -1 
        i = 0

        def swap(index, digit ):
            tmp = nums[index]
            nums[index] = nums[digit]
            nums[digit] = tmp

        # this will make sure to iterate through each num
        # without repeating it 
        while i <= right:
            # if the number at the ith index is 0, swap it with  the num on the left
            # increase the left
            if nums[i] == 0:
                swap(left, i)
                left += 1
            # if the number at the ith index is 2, swap it with the num on the right
            # decrease the right
            elif nums[i] == 2:
                swap(i, right)
                right -= 1
                # this is so i can cancel out when we increase it in the following line
                # you dont accidently replace the left numbers with the right ones
                i -= 1
            i += 1
