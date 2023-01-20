# 53. Maximum Subarray
# Medium
# 27.6K
# 1.2K
# Companies
# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
  
  class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max sub so far will be the first subarray
        max_sub = nums[0]
        # current sum equals 0
        currSum = 0
        # for every number in nums
        for num in nums:
            # if the sum is less than 0, it wont contribute anything to the our computation
            if currSum < 0:
                # so just let currSum equal 0
                currSum = 0
                
            # add the number to the sum
            currSum += num
            # take the max of sub or currSum and set this as the max_sub
            max_sub = max(max_sub, currSum)
        return max_sub
