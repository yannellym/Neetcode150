# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
# Example 2:

# Input: nums = [5], k = 9
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# 2 <= k <= 104
# Accepted
# 181.2K
# Submissions
# 332K
# Acceptance Rate
# 54.6%


class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        res = 0
        currSum = 0
        # create a dictionary with 0 having a count of 1
        # this is because there is a prefix of 0 right before the first element
        sumPrefix = { 0:1 }
        # for every digit in nums
        for n in nums:
            # add it to the current sum
            currSum += n
            # check if the sum of current subarray is divisible by k
            # save that remainder in variable remainder
            remainder = currSum % k
            # if we have seen this value of remainder before
            # increment the result by the count of such remainder
            # if not there, just return 0
            res += sumPrefix.get(remainder,0)
            # increment the count of this remainder in the sumPrefix dict
            # by 1. If its not there, add it, and add 1
            sumPrefix[remainder] = 1 + sumPrefix.get(remainder, 0)
        return res

        # link: https://www.youtube.com/watch?v=WySQG-7BepA
        # link: https://www.youtube.com/watch?v=fFVZt-6sgyo&t=20s
