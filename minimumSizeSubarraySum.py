# 209. Minimum Size Subarray Sum
# Medium
# 10.9K
# 300
# company
# Apple
# company
# Citadel
# company
# Amazon
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
# Accepted
# 787.9K
# Submissions
# 1.7M
# Acceptance Rate
# 46.4%

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        win_s = 0
        t_sum = 0
        res = float('inf')
        # iterate through the nums arr
        for win_e in range(len(nums)):
            # add each digit to the t_sum
            t_sum += nums[win_e]

            # while the t_sum amount is >= to target
            while t_sum >= target:
                # lets set res to the min between res and the window length 
                res = min(res, (win_e - win_s + 1)) # the size of the subarray
                # remove the the digit at index win_s of nums from t_sum
                t_sum -= nums[win_s]
                # increment win_s to make our window smaller
                win_s +=1
        # if the res is still infinity, that means we didnt find a value to match our target, return 0
         # if its not infinity, just return the value of res
        return 0 if res == float('inf') else res 
