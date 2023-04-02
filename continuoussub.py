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
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # initialize the store to 0: -1 
        # this means that we have a subarray of sum 0 that starts at -1
        # this will help us take care of the edge case that the first val in the arr is a multiple of k
        # we need an arr of length 2 at least 
        store  = {0: -1}
        summ = 0

        # iterate through nums to get the index and the key
        for i, j in enumerate(nums):
            # add the key to the sum
            # this will create another subarray 
            summ += j
            # find the remainer
            remainder = summ % k 
            # if we dont have this remainder in the store
            if remainder not in store:
                # add the remainer and add the index. This index is where the remainder sub ENDS
                store[remainder] = i  
                # else if the remainder is in the store, and the result from subtracting the current index minus
                # the index in the store is greater than 1 (this means our sub is greater than length one)
            elif i - store[remainder] > 1:
                # return true because we have found our sub
                return True
        # if the above doesnt execute, we dont have a continuous subarray sum 
        return False
