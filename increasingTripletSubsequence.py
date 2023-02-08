# 334. Increasing Triplet Subsequence
# Medium
# 6.2K
# 269
# Companies
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

# Constraints:

# 1 <= nums.length <= 5 * 105
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
# Accepted
# 374.6K
# Submissions
# 876.9K
# Acceptance Rate
# 42.7%


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s1 = float('inf')
        s2 = float('inf')

        # for every digit in nums
        for digit in nums:
            # if the digit is greater than s2:
            # return true because it means we found an increasing triplet subsequence
            if digit > s2:
                return True
            # if the digit is greater than s1:
            # have s2 equal whichever is less (the digit or s2)
            if digit > s1:
                s2 = min(digit,s2)
            # have s1 equal the min between the digit and s1
            s1 = min(digit, s1)
        # if the above doesnt execute, return False
        return False
