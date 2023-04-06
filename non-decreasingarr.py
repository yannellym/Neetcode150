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
        # set a flag to see if we have any changes left
        changes_left = True
        # iterate through every number in nums len(nums) -1 so we can have a pair
        for i in range(len(nums)-1):
            # if the num at position i is less than or equal to num i + 1, continue
            if nums[i] <= nums[i+1]:
                continue
            # if there are no changes left, return false
            if not changes_left:
                return False
            # if i is 0, meaning that theres only two chars in the array ex. [0, 4], change the num at position i to be nums i+1
            # OR if the number at position i +1 is greater than or equal to nums i - 1, change nums i to be equal to numsi +1  
            if i == 0 or nums[i+1] >= nums[i-1]:
                nums[i] = nums[i+1]
            else:
                # else if nums i +1 is less than or equal to numsi - 1, just change numsi+1 to be equal to numsi
                nums[i+1] = nums[i]
            # change the flag to equal false
            changes_left = False
        # if we made it here, it means we sucessfully have a non decreasing array
        return True

        # basically we look at i, compare i +1 to i-1, if i + 1 is >= to i-1 change i to be i+1
        # if i +1 is <= to i-1, change i +1 to equal nums1
        # set the false flag

                
                        
