# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        r = 0
        sum = 0
        min_len = float('inf')

        # while r is less than the length of nums
        while r < len(nums):
            # add the rth element of nums to our sum
            sum += nums[r]
            # while the sum is greater than or equal to the target 
            while sum >= target:
                # choose the min between the min_len and the window length
                min_len = min(min_len, r-left + 1)  
                # subtract the left digit from the sum (the digit at start of window)
                sum -= nums[left]
                # increment the left variable
                left += 1
            # increase the right variable to keep making our window larger
            r += 1
        # if the min len is 0, we return infinity. Else, we return the min_len
        return 0 if min_len == float('inf') else min_len
