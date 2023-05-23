# 16. 3Sum Closest
# Medium
# 9.2K
# 478
# company
# Adobe
# company
# Amazon
# company
# Facebook
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

# Constraints:

# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104
# Accepted
# 1M
# Submissions
# 2.3M
# Acceptance Rate
# 45.6%

import bisect

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()  # Sort the array in ascending order
        # [-4, -1, 1, 2]
        closest_sum = float('inf')  # Initialize the closest sum with infinity

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                # Calculate the current sum
                curr_sum = nums[i] + nums[left] + nums[right]

                # Update the closest sum if the current sum is closer to the target
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return curr_sum  # Found an exact match, return the sum

        return closest_sum
