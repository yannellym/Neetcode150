# 665. Non-decreasing Array
# Medium

# 5146

# 743

# Add to List

# Share
# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

# Example 1:

# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:

# Input: nums = [4,2,1]
# Output: false
# Explanation: You cannot get a non-decreasing array by modifying at most one element.
 

# Constraints:

# n == nums.length
# 1 <= n <= 104
# -105 <= nums[i] <= 105
# Accepted
# 232.9K
# Submissions

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        changed = False
        # this makes sure that a number always has a pair
        # by ignoring the last digit
        for i in range(len(nums) - 1):
            # if the current digit is less than or equal to the nest digit
            # continue because this is the right ordering
            if nums[i] <= nums[i+1]:
                continue
            # if the variable changed is now True:
            # we have already changed 1 element and reached our limit
            # of changes
            if changed:
                return False
            # if the index is 0 or the right number is greater than or
            # equal to the number on the left:
            if i == 0 or nums[i+1] >= nums[i-1]:
                # make the middle number equal the right number
                nums[i] = nums[i+1]
            else:
                # if not, change the right one equal the middle one
                nums[i+1] = nums[i]
            # set the changed variable to true
            changed = True 
        # return true if the array is in increasing order
        return True

                
                        
