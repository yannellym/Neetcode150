# 523. Continuous Subarray Sum
# Medium

# 4236

# 410

# Add to List

# Share
# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

# Example 1:

# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
# Example 2:

# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
# Example 3:

# Input: nums = [23,2,6,4,7], k = 13
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 0 <= sum(nums[i]) <= 231 - 1
# 1 <= k <= 231 - 1
# Accepted
# 374,894
# Submissions
# 1,313,164

# example of visualization

# [23,2,6,4,7] k =12

# (23)%12 = 11
# (23+2)%12=1
# (23+2+6)%12 = 7
# (23+2+6+4)%12=11 -> seen before, so return true because:

# (23+2+6+4) - (23) = 12 -> 12 % 12 = 0

class Solution(object):
    def checkSubarraySum(self, nums, k):
        # initialize the hash map with index 0 for sum 0
        hash_map = {0: -1}
        total = 0
        # enumerate nums to get the index and the value of each digit
        for index, value in enumerate(nums):
            # add each digit to the total
            total += value
            # find the remainder of the total by k 
            remain = total % k
            # if the remainder has not been added to the hash map yet,
            if remain not in hash_map:
                # add it to the hash map and make its value equal to the index
                hash_map[remain] = index
            # if the result of current index - the index of the remainer is greater than 1:
            elif index - hash_map[remain] > 1:
                # that means we have a subarray of length greater than 1, we can return true
                return True
        # if all fails, return False
        return False
