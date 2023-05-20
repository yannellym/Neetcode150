# 1099. Two Sum Less Than K
# Easy

# 863

# 97

# Add to List

# Share
# Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

 

# Example 1:

# Input: nums = [34,23,1,24,75,33,54,8], k = 60
# Output: 58
# Explanation: We can use 34 and 24 to sum 58 which is less than 60.
# Example 2:

# Input: nums = [10,20,30], k = 15
# Output: -1
# Explanation: In this case it is not possible to get a pair sum less that 15.
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 1000
# 1 <= k <= 2000

class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # sort the array
        nums.sort()
        # Ex. [1, 8, 23, 24, 33, 34, 54, 75]

        # two pointers at each end
        l = 0
        r = len(nums)-1
        # lets set the max to -1 
        maxSum = -1


        # while the pointers do not meet
        while l < r:
            # get the sum of the numbers
            currSum = nums[l] + nums[r]
            # if the sum is greater than or equal to k
            if currSum >= k:
                # decremenet the right side so we get a smaller sum next time
                r -= 1
            else:
                # else, take the max sum so far, and increment the left to look for a bigger sum.
                maxSum = max(currSum, maxSum)
                l +=1
        # return the maxsum which will either be the maxsum or -1 
        return maxSum 


   
      
      
      
"""
Sliding window problem:

- 2 pointer solution

Approach 1:
- Sort array 
- This will help because when we move through the array we know the value are increasing which will meet the i < j condition
- Then, as we add nums[i] + nums[j] = result
  - if result < max_sum < k, then max_sum = result
  return max_sum if max_sum > 0 else -1
  Run time: Big O(n log n) because of the sorting
  Space: Big O(1) if the sort is in place or if we use another variable to not alter input then Big O(n)
"""
