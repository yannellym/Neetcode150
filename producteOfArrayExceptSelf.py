# 238. Product of Array Except Self
# Medium

# 15385

# 864

# Add to List

# Share
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
  
 class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # the prefix will be 1 to start with
        prefix = 1
        # loop through nums
        for i in range(len(nums)):
            # update the index in res to equal the prefix
            res[i] = prefix
            # set the prefix to prefix multiplied by nums i 
            prefix *= nums[i]
        # postfix will equal one
        postfix = 1
        # loop through nums but backwards
        for i in range(len(nums)-1,-1,-1):
            # the value at index in res will be multiplied by the postfix
            res[i] *= postfix
            # the postfix will now be multiplied by nums i 
            postfix *= nums[i]
        return res
       
       
      # solution 2
      # step 1: create res array of -1 values the length of nums
        # step 2: set a prefix equal to 1. iterate length of nums. 
            # have res[i] equal the prefix
            # update the prefix to be equal to prefix times nums[i]
        # step 3: set a postfix equal to 1. Iterate in reverse the length of nums.
            # update res[i] to equal res[i] times the postfix
            # update the postfix to be equal to postfix times nums[i]
        # step 4: return the product


        res = [-1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]
        return res
