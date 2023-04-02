508 Swing Sort
algorithm
medium

Given an unsorted array, please rearrange the original array in place to satisfy the following properties

nums[0] <= nums[1] >= nums[2] <= nums[3]....
For questions that may have more than one answer, you only need to consider one of the possibilities .


Please sort the array in-place, do not define the array additionally.

sample
Example 1:

输入: [3, 5, 2, 1, 6, 4]
输出: [1, 6, 2, 5, 3, 4]
解释: 这个问题可能有多种答案, [2, 6, 1, 5, 3, 4] 同样可以.
Example 2:

输入: [1, 2, 3, 4]
输出: [1, 4, 2, 3]
  
  
  class Solution:
    """
    @param nums: A list of integers
    @return: nothing
    """
    def wiggle_sort(self, nums):
        # write your code here
        for i in range(1, len(nums)):
            # if index is odd
            if i % 2 == 1:
                if nums[i] <= nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
            if i % 2 == 0:
                if nums[i] >= nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
        return nums

# the idea is that depending if the index is even or odd, we are going to check if t=he number is the opposite of the condition we are given.
# ex, if index is even, check if the number is >= to the previous one
# if the index is odd, check if the number is <= to the previous one 
