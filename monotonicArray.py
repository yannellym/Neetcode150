896. Monotonic Array
Solved
Easy
Topics
Companies
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
Accepted
283.2K
Submissions
483.3K
Acceptance Rate
58.6%  

class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        

        return all(nums[x] <= nums[x+1] for x in range(len(nums) - 1)) or all(nums[x] >=nums[x+1] for x in range(len(nums) - 1)) 
