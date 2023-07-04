# 137. Single Number II
# Medium
# 6.9K
# 616
# company
# Google
# company
# Amazon
# company
# Apple
# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:

# Input: nums = [0,1,0,1,0,1,99]
# Output: 99
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each element in nums appears exactly three times except for one element which appears once.
# Accepted
# 484K
# Submissions
# 794K
# Acceptance Rate
# 61.0%

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort the nums array to every digit in sorted in a group
        nums.sort()

        # start at 0, until the len of nums-1, and go up by 3 each iteration.
        for i in range(0, len(nums)-1, 3):
            # nums[i] (the number in the middle of the "sorted" group) equals the number next to it, 
              # lets continue searching as this is a sorted group
            if nums[i] == nums[i+1]:
                continue
            else:
                # if it doesn't equal, we must be in a value that is not repeated, return 
                return nums[i]
        # it might be that the single value is in the last place of the array so we need to check
        # return the last value because we are guaranteed an answer if its none of the above
        return nums[-1]
        

