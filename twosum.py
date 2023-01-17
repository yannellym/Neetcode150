
# G1. Two Sum
# Easy
# 42.3K
# 1.4K
# Companies
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
# Accepted
# 8.7M
# Submissions
# 17.7M
# Acceptance Rate
# 49.3%

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # map will store the values along its indexes
        store = {}
        # enumerate nums in order to get the value and the index
        for index, value in enumerate(nums):
            # get the diff between the target and value
            diff = target - value
            # if the diff is in the store already
            if diff in store:
                # return the index of the current value
                # AND the index stored in the store
                return [index, store[diff]]
            # if the value is not in the store, add it and set the val as its index
            store[value] = index
