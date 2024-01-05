300. Longest Increasing Subsequence
Solved
Medium
Topics
Companies
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

Seen this question in a real interview before?
1/4

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # start an array with all 1s * the length of nums
        in_memory = [1] * len(nums)

        # iterate in reverse through nums:
        for i in range(len(nums)-1, -1, -1):
            # iterate from i +1 until the end
            for j in range(i+1, len(nums)):
                # check if nums i is less than nums j(only then you can form a correct sequence)
                if nums[i] < nums[j]:
                    # have in_memory i be the max of 1 or 1 plus the in_memory(max) of j
                    in_memory[i] = max(in_memory[i], 1 + in_memory[j])
        # at the end, we will have the max value compounded in the array
        return max(in_memory)
